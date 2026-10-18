"""Scripted effects for the Promo_SWSH (Sword & Shield Black Star Promos) set.

The shared factories (attacks_common / passives_common / support_common /
pokemon) cover the straightforward patterns; this module holds the behaviors
that needed hand-writing, plus the small predicate helpers the card texts
reference (Leon cards in the discard pile, "Basic with a Rule Box", the
Mad Party attack name, ...).

Engine-model notes carried through this file:
  * An Attack is an Ability subclass: `effect=` is the coroutine,
    `locks_next_turn=True` covers "can't use this attack next turn", and
    `vstar=True` flips the once-per-game VSTAR marker.
  * "During your next turn, this Pokemon can't attack" (all attacks, not just
    this one) is attacks_common.lock_all_attacks(ctx, attacker).
  * `count_energy("mine", T)` counts PROVIDED energy across your whole board,
    `count_energy("self", T)` on the attacker only.
  * Bench-only damage ignores Weakness/Resistance automatically (the engine
    auto-detects non-Active targets), so "Don't apply W/R for Benched" needs
    no extra flag.
  * Damage-counter placement is raw (as_counters): no W/R, no prevention
    except an attack-effect shield on the target.
  * Promo reprints repeat heavily (Eevee x4, CrobatV x2, ...): the same
    factory call is reused verbatim per reprint.
"""

from typing import Optional

from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.game.content.definitions import (
    Activations,
    Attack,
    Triggers,
    has_rule_box,
    is_pokemon_v,
    subtypes_for,
)
from spirit.game.data_utils import def_for
from spirit.game.models.board import PokemonEntity
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import (
    count_bench,
    count_energy,
    count_hand,
    count_in_play,
    count_prizes_taken,
    damage_counters_on,
    lock_all_attacks,
)
from spirit.game.card_effects.passives_common import (
    is_in_active_spot,
    takes_less_passive,
    team_damage_boost_passive,
    prevent_damage_when,
)
from spirit.game.card_effects.pokemon import (
    is_pokemon_gx,
    is_pokemon_vmax,
    is_energy_card,
    energy_provides_type,
)
from spirit.game.card_effects.support_common import (
    search_attach_energy,
    search_to_bench,
    search_to_hand,
    attach_from_discard,
    draw_attack,
    draw_until_effect,
    look_at_top,
)


# ----------------------------------------------------------------------
# Predicates / helpers
# ----------------------------------------------------------------------

def is_named(card, name: str) -> bool:
    """Card predicate: the card's display name matches (Leon, VSTAR Power)."""
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return getattr(definition, "display_name", None) == name


def is_basic_energy_card(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return bool(getattr(definition, "is_basic_energy", False))


def has_attack_titled_predicate(title: str):
    """Card predicate over the DISCARD PILE: a Pokemon whose definition
    carries an attack named `title` (Mad Party)."""
    def pred(card) -> bool:
        definition = def_for(getattr(card, "archetype_id", None) or "")
        return any(getattr(a, "title", None) == title
                   for a in getattr(definition, "abilities", []) or [])
    return pred


def is_pokemon_without_rule_box(pokemon) -> bool:
    return not has_rule_box(getattr(pokemon, "archetype_id", None) or "")


def is_pokemon_v_predicate(pokemon) -> bool:
    return is_pokemon_v(getattr(pokemon, "archetype_id", None) or "")


def is_pokemon_vmax_predicate(pokemon) -> bool:
    return is_pokemon_vmax(getattr(pokemon, "archetype_id", None) or "")


def is_basic_pokemon_predicate(pokemon) -> bool:
    return "Basic" in subtypes_for(getattr(pokemon, "archetype_id", None) or "")


def _pokemon_types(pokemon) -> list:
    return list(pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def is_type(pokemon_type) -> "callable":
    """Entity predicate: the Pokemon's live type list includes `type`."""
    value = getattr(pokemon_type, "value", pokemon_type)

    def pred(pokemon) -> bool:
        return value in _pokemon_types(pokemon)
    return pred


def energy_provides(card, pokemon_type) -> bool:
    """Card predicate: an energy card that provides `pokemon_type`."""
    value = getattr(pokemon_type, "value", pokemon_type)
    if not is_energy_card(card):
        return False
    return energy_provides_type(card, value)


def has_special_condition(pokemon) -> bool:
    return bool(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS))


# ----------------------------------------------------------------------
# Alakazam V -- Zen Spoon / Mind Ruler
# ----------------------------------------------------------------------

async def zen_spoon(ctx):
    """Put 3 damage counters on your opponent's Pokemon in any way you like."""
    if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
        await ctx.deal_damage()
    await ctx.place_damage_counters(3, ctx.opponent_pokemon_in_play())


def mind_ruler():
    """30x for each card in your opponent's hand."""
    return _scaled(count_hand("opponent"), 30)


def _scaled(count_fn, per, base=0):
    from spirit.game.card_effects.attacks_common import damage_per
    return damage_per(count_fn, per, base=base)


# ----------------------------------------------------------------------
# Alcremie -- Decorate / Draining Kiss
# ----------------------------------------------------------------------

def decorate():
    """Attach as many basic Energy cards as you like from your hand to your
    Pokemon in any way you like (attack; no damage)."""
    from spirit.game.card_effects.support_common import distribute_energy

    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, len(pool), minimum=0,
            prompt="Choose any number of basic Energy cards to attach",
        )
        if not picks:
            return
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        await distribute_energy(ctx, picks, candidates)
    return effect


def draining_kiss(amount=30):
    from spirit.game.card_effects.support_common import heal_attack
    return heal_attack(amount=amount)


# ----------------------------------------------------------------------
# Alolan Exeggutor V -- Growing Tall / Head Swing
# ----------------------------------------------------------------------

def growing_tall():
    """Flip a coin. If heads, search your deck for up to 5 Grass Energy cards
    and attach them to your Pokemon in any way you like."""
    from spirit.game.card_effects.attacks_common import flip_or_nothing

    def is_grass_energy(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.GRASS)

    return flip_or_nothing(then=search_attach_energy(
        predicate=is_grass_energy, count=5,
        prompt="Choose up to 5 Grass Energy cards to attach",
    ))


def head_swing(per=30):
    """30 damage to 1 of your opponent's Pokemon for each Grass Energy
    attached to this Pokemon."""
    from spirit.game.card_effects.attacks_common import snipe_attack

    def grass_on_self(ctx):
        return sum(1 for c in ctx.attached_energies(ctx.attacker)
                   if energy_provides(c, PokemonTypes.GRASS))

    async def effect(ctx):
        amount = per * grass_on_self(ctx)
        if amount > 0:
            await ctx.deal_damage(amount, apply_modifiers=None)
    return effect


# ----------------------------------------------------------------------
# Arceus V / VSTAR -- Trinity Charge / Trinity Nova / Starbirth
# ----------------------------------------------------------------------

def trinity_charge():
    """Search your deck for up to 3 basic Energy cards and attach them to
    your Pokemon V in any way you like."""
    return search_attach_energy(
        predicate=is_basic_energy_card, count=3,
        target_pred=lambda p: is_pokemon_v(p.archetype_id),
        prompt="Choose up to 3 basic Energy cards to attach",
    )


def starbirth():
    """[VSTAR Power] Search your deck for up to 2 cards and put them into
    your hand."""
    return search_to_hand(count=2, reveal=False,
                          prompt="Choose up to 2 cards to put into your hand")


# ----------------------------------------------------------------------
# Ditto VMAX -- Max Transform
# ----------------------------------------------------------------------

def max_transform():
    """Choose 1 of the opponent's Active Pokemon's attacks and use it as this
    attack: full effect and printed damage, with "can't attack next turn"
    locks carried over onto Ditto VMAX's own attack."""
    async def effect(ctx):
        active = ctx.opponent_active()
        if active is None:
            return
        definition = def_for(active.archetype_id)
        candidates = [
            (active, ability) for ability in getattr(definition, "abilities", [])
            if isinstance(ability, Attack)
        ]
        if not candidates:
            return
        picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
        if picked is None:
            return
        _, chosen = picked
        if not await ctx.use_attack(chosen):
            return
        if getattr(chosen, "locks_next_turn", False):
            for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
                if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                    ctx.session.turn_state.lock_attack(
                        ctx.attacker.entity_id, entry["abilityID"]
                    )
    return effect


# ----------------------------------------------------------------------
# Archeops -- Primal Turbo
# ----------------------------------------------------------------------

def primal_turbo():
    """Once during your turn, search your deck for up to 2 Special Energy
    cards and attach them to 1 of your Pokemon."""
    def is_special_energy(card):
        definition = def_for(getattr(card, "archetype_id", None) or "")
        return bool(getattr(definition, "is_special_energy", False))

    return search_attach_energy(
        predicate=is_special_energy, count=2, distribute=False,
        prompt="Choose up to 2 Special Energy cards to attach",
    )


# ----------------------------------------------------------------------
# Arctozolt -- Biting Whirlpool
# ----------------------------------------------------------------------

async def biting_whirlpool(ctx):
    """[ON_ENERGY_ATTACHED] Whenever your opponent attaches an Energy card
    from their hand to 1 of their Pokemon, put 2 damage counters on that
    Pokemon."""
    if ctx.attaching_player_id != ctx.opponent_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None:
        return
    await ctx.deal_damage(20, target=receiver, apply_modifiers=False,
                          as_counters=True)


# ----------------------------------------------------------------------
# Arrokuda -- Flock
# ----------------------------------------------------------------------

def flock(name: str, count: int = 2):
    """Search your deck for up to `count` Pokemon named `name` and put them
    onto your Bench."""
    def is_named_pokemon(card):
        return is_named(card, name)

    return search_to_bench(predicate=is_named_pokemon, count=count,
                           prompt=f"Choose up to {count} {name} to put onto your Bench")


# ----------------------------------------------------------------------
# Bibarel -- Tail Smash / Industrious Incisors
# ----------------------------------------------------------------------

def tail_smash():
    from spirit.game.card_effects.attacks_common import flip_or_nothing
    return flip_or_nothing()


def industrious_incisors(hand_size=5):
    return draw_until_effect(hand_size)


# ----------------------------------------------------------------------
# Blastoise V / VMAX -- Torrential Cannon / Grand Falls / G-Max Bombard
# ----------------------------------------------------------------------

def torrential_cannon():
    """Printed damage, then locks every attack for the next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        lock_all_attacks(ctx, ctx.attacker)
    return effect


def grand_falls():
    """Search your deck for up to 3 Water Energy cards and attach them to
    your Benched Pokemon in any way you like."""
    def is_water_energy(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.WATER)

    return search_attach_energy(
        predicate=is_water_energy, count=3,
        target_pred=is_benched,
        prompt="Choose up to 3 Water Energy cards to attach to your Benched Pokemon",
    )


def is_benched(pokemon) -> bool:
    """Entity predicate: a top-level Pokemon on its owner's Bench."""
    return not is_in_active_spot(pokemon)


def g_max_bombard(bench_damage=30, count=2):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(bench_damage, pool="bench", count=count,
                        also_base=True)


# ----------------------------------------------------------------------
# Blitzle -- Thunder Spear / Boltund V -- Smash Turn / Electrify / Bolt Storm
# ----------------------------------------------------------------------

def thunder_spear(amount=10):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(amount, pool="any")


def smash_turn():
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack(optional=True)


def electrify():
    def is_lightning(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.LIGHTNING)

    return search_attach_energy(
        predicate=is_lightning, count=2,
        prompt="Choose up to 2 Lightning Energy cards to attach to your Benched Pokemon",
    )


def bolt_storm(per=30):
    """30 more for each Lightning Energy attached to all of your Pokemon."""
    from spirit.game.card_effects.attacks_common import bonus_if, count_energy
    return bonus_if(lambda ctx: True, 0, base=0) if False else \
        _scaled(count_energy("mine", PokemonTypes.LIGHTNING), per)


# ----------------------------------------------------------------------
# Bronzong -- Metal Transfer
# ----------------------------------------------------------------------

def metal_transfer():
    """As often as you like during your turn, move a Metal Energy from 1 of
    your Pokemon to another of your Pokemon."""
    async def effect(ctx):
        holders = [p for p in ctx.my_pokemon_in_play()
                   if any(energy_provides(e, PokemonTypes.METAL)
                          for e in ctx.attached_energies(p))]
        if not holders:
            return
        source = await ctx.choose_pokemon(
            holders, "Choose 1 of your Pokemon with a Metal Energy attached")
        if source is None:
            return
        movable = [e for e in ctx.attached_energies(source)
                   if energy_provides(e, PokemonTypes.METAL)]
        if not movable:
            return
        pick = await ctx.choose_cards(
            movable, 1, prompt="Choose a Metal Energy to move")
        if not pick:
            return
        others = [p for p in ctx.my_pokemon_in_play() if p is not source]
        if not others:
            return
        target = await ctx.choose_pokemon(
            others, "Choose a Pokemon to move the Metal Energy to")
        if target is None:
            return
        await ctx.move_energy(pick[0], target)
    return effect


# ----------------------------------------------------------------------
# Mad Party family (Bunnelby / Dedenne / Galarian Mr. Rime / Polteageist)
# ----------------------------------------------------------------------

def mad_party(per=20):
    """20x for each Pokemon in your discard pile that has the Mad Party
    attack."""
    from spirit.game.card_effects.attacks_common import count_discard
    return _scaled(count_discard("mine", has_attack_titled_predicate("Mad Party")), per)


def tea_break():
    """You must discard a Pokemon that has the Mad Party attack from your
    hand to use this Ability. Once during your turn, you may draw 2 cards."""
    async def effect(ctx):
        pool = [c for c in ctx.hand()
                if has_attack_titled_predicate("Mad Party")(c)]
        if not pool:
            return
        pick = await ctx.choose_cards(
            pool, 1, minimum=1,
            prompt="Choose a Pokemon with the Mad Party attack to discard")
        if not pick:
            return
        await ctx.discard_cards(pick)
        await ctx.draw_cards(2)
    return effect


# ----------------------------------------------------------------------
# Centiskorch -- Hundred Foot Flames / Searing Flame
# ----------------------------------------------------------------------

def hundred_foot_flames():
    """For each Fire Energy attached to this Pokemon, discard the top card of
    your opponent's deck."""
    async def effect(ctx):
        if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
            await ctx.deal_damage()
        n = sum(1 for c in ctx.attached_energies(ctx.attacker)
                if energy_provides(c, PokemonTypes.FIRE))
        for _ in range(n):
            top = ctx.deck_top(1, player_id=ctx.opponent_id)
            if top:
                await ctx.discard_cards(top)
    return effect


def searing_flame():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.BURNED)


# ----------------------------------------------------------------------
# Charizard -- Royal Blaze / Battle Sense
# ----------------------------------------------------------------------

def royal_blaze(per=50):
    """50 more for each Leon card in your discard pile."""
    from spirit.game.card_effects.attacks_common import count_discard
    return _scaled(count_discard("mine", lambda c: is_named(c, "Leon")), per)


def battle_sense():
    """Look at the top 3 cards of your deck and put 1 of them into your hand.
    Discard the other cards."""
    return look_at_top(3, take=1, rest="discard")


# ----------------------------------------------------------------------
# Charizard V / VMAX / VSTAR
# ----------------------------------------------------------------------

def incinerate():
    """Before doing damage, discard all Pokemon Tools from your opponent's
    Active Pokemon."""
    async def effect(ctx):
        defender = ctx.opponent_active()
        if defender is not None and not ctx.effects_blocked(defender):
            tools = [c for c in defender.children if _is_tool_card(c)]
            if tools:
                await ctx.discard_cards(tools)
        await ctx.deal_damage()
    return effect


def _is_tool_card(card) -> bool:
    from spirit.game.card_effects.attacks_common import _TOOL_TYPES as TOOL_TYPES
    return card.get_attribute(AttrID.TRAINER_TYPE) in TOOL_TYPES


def fire_spin(count=2):
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=count)


def explosive_fire(bonus=100):
    from spirit.game.card_effects.attacks_common import bonus_if, has_damage
    return bonus_if(has_damage("self"), bonus)


def star_blaze():
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=2, then_damage=320)


# ----------------------------------------------------------------------
# Charmander -- Tail on Fire / Collect
# ----------------------------------------------------------------------

def tail_on_fire():
    def is_fire(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.FIRE)

    return search_attach_energy(predicate=is_fire, count=1, to_self=True,
                                prompt="Choose a Fire Energy card to attach")


def collect(count=1):
    return draw_attack(count)


# ----------------------------------------------------------------------
# Cherrim -- Spring Bloom
# ----------------------------------------------------------------------

def spring_bloom():
    """As often as you like during your turn, attach a Grass Energy card from
    your hand to 1 of your Pokemon that doesn't have a Rule Box."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_energy_card(c)
                and energy_provides(c, PokemonTypes.GRASS)]
        if not pool:
            return
        candidates = [p for p in ctx.my_pokemon_in_play()
                      if is_pokemon_without_rule_box(p)]
        if not candidates:
            return
        pick = await ctx.choose_cards(pool, 1, prompt="Choose a Grass Energy card to attach")
        if not pick:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokemon without a Rule Box to attach to")
        if target is None:
            return
        await ctx.attach_energy(pick[0], target)
    return effect


# ----------------------------------------------------------------------
# Cinccino -- Energy Assist / Make Do
# ----------------------------------------------------------------------

def energy_assist():
    """Attach a basic Energy card from your discard pile to 1 of your
    Benched Pokemon."""
    return attach_from_discard(
        predicate=is_basic_energy_card, count=1, target=is_benched,
        prompt="Choose a basic Energy card from your discard pile",
    )


def make_do(draw=2):
    """You must discard a card from your hand to use this Ability. Once during
    your turn, you may draw 2 cards."""
    from spirit.game.card_effects.support_common import discard_then_draw
    return discard_then_draw(1, draw, optional=False)


# ----------------------------------------------------------------------
# Cinderace -- Fireball Shot / Crisis Power
# ----------------------------------------------------------------------

def fireball_shot():
    async def effect(ctx):
        await ctx.deal_damage()
        lock_all_attacks(ctx, ctx.attacker)
    return effect


def crisis_power(per=30):
    """This Pokemon's attacks do 30 more damage to your opponent's Active
    Pokemon for each Prize card your opponent has taken."""
    return team_damage_boost_passive(
        per, attacker_pred=None,
        target_pred=lambda t, c: t is c,
    ) if False else _prize_scaled_boost(per, opponent=True)


def _prize_scaled_boost(per, opponent=True):
    class PrizeScaledDamagePassive(Passive):
        """+N damage to the opponent's Active for each Prize that player has
        taken (Crisis Power / Revenge Blast share the shape)."""

        def modify_damage_dealt(self, calc, carrier):
            if not (calc.is_attack and calc.is_opposing):
                return
            attacker = calc.attacker
            if attacker is None or \
                    carrier_pokemon(carrier) is not attacker:
                return
            if calc.target is None or calc.target is not calc.board.active_pokemon(
                    calc.target.owning_player_id):
                return
            from spirit.game.session.legal_actions import TurnState
            state = getattr(calc.board, "turn_state", None)
            if state is None:
                return
            pid = attacker.owning_player_id
            opponent_id = next((p for p in calc.board.player_ids if p != pid), None)
            if opponent_id is None:
                return
            taken = state.prizes_taken.get(opponent_id, 0)
            calc.amount += per * taken

    return PrizeScaledDamagePassive()


def crisis_power_attack(per=30):
    """Attack form: +30 per Prize card your opponent has taken."""
    from spirit.game.card_effects.attacks_common import damage_per
    from spirit.game.card_effects.attacks_common import count_prizes_taken
    return damage_per(count_prizes_taken("opponent"), per)


# ----------------------------------------------------------------------
# Coalossal -- Tar Generator
# ----------------------------------------------------------------------

def tar_generator():
    """Once during your turn, attach a Fire Energy, a Fighting Energy, or 1
    of each from your discard pile to your Pokemon in any way you like."""
    async def effect(ctx):
        def is_fire(card):
            return is_energy_card(card) and energy_provides(card, PokemonTypes.FIRE)

        def is_fighting(card):
            return is_energy_card(card) and energy_provides(card, PokemonTypes.FIGHTING)

        pool = [c for c in ctx.discard_pile() if is_fire(c) or is_fighting(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 2, minimum=0,
            prompt="Choose a Fire Energy, a Fighting Energy, or 1 of each to attach")
        if not picks:
            return
        fire = [c for c in picks if is_fire(c)][:1]
        fighting = [c for c in picks if is_fighting(c)][:1]
        chosen = fire + fighting
        if not chosen:
            return
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        from spirit.game.card_effects.support_common import distribute_energy
        await distribute_energy(ctx, chosen, candidates)
    return effect


# ----------------------------------------------------------------------
# Comfey -- Flower Selecting (reuse pokemon.flower_selecting)
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Copperajah V -- Adamantine Press
# ----------------------------------------------------------------------

def adamantine_press(reduce=30):
    from spirit.game.card_effects.passives_common import protect_next_turn
    return protect_next_turn(reduce=reduce)


# ----------------------------------------------------------------------
# Corviknight V -- Clutch / Sky Hurricane
# ----------------------------------------------------------------------

def clutch():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(no_retreat=True)


def sky_hurricane():
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.session.turn_state.lock_attack(
            ctx.attacker.entity_id,
            ctx.ability.ability_id,
        )
    return effect


# ----------------------------------------------------------------------
# Cramorant V -- Beak Catch / Spit Shot
# ----------------------------------------------------------------------

def beak_catch(count=2):
    return search_to_hand(count=count, reveal=False,
                          prompt="Choose up to 2 cards to put into your hand")


def spit_shot(damage=160):
    from spirit.game.card_effects.attacks_common import (
        self_energy_discard_attack, snipe_attack)
    return self_energy_discard_attack(
        all_energy=True, before_damage=True, then_damage=damage)


# ----------------------------------------------------------------------
# Cranidos -- Stone Edge
# ----------------------------------------------------------------------

def stone_edge(bonus=40):
    from spirit.game.card_effects.attacks_common import flip_bonus
    return flip_bonus(bonus)


# ----------------------------------------------------------------------
# Cresselia -- Crescent Glow / Photon Laser
# ----------------------------------------------------------------------

def crescent_glow():
    """Search your deck for a Psychic Energy card and attach it to 1 of your
    Pokemon. If you go second and it's your first turn, instead search for up
    to 3 Psychic Energy cards."""
    def is_psychic(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.PSYCHIC)

    async def effect(ctx):
        count = 3 if _going_second_first_turn(ctx) else 1
        await search_attach_energy(
            predicate=is_psychic, count=count,
            prompt="Choose up to %d Psychic Energy card(s) to attach" % count,
        )(ctx)
    return effect


def _going_second_first_turn(ctx) -> bool:
    state = ctx.session.turn_state
    if state.turn_number != 2:
        return False
    return ctx.session.first_player_id != ctx.player_id


def photon_laser(bonus=90, threshold=5):
    """If you have at least 5 Energy in play, this attack does 90 more
    damage."""
    from spirit.game.card_effects.attacks_common import bonus_if

    def five_energy_in_play(ctx):
        return count_energy("mine")(ctx) >= threshold

    return bonus_if(five_energy_in_play, bonus)


# ----------------------------------------------------------------------
# Crobat V / VMAX -- Venomous Fang / Dark Asset / Stealth Poison
# ----------------------------------------------------------------------

def venomous_fang():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.POISONED)


def dark_asset(hand_size=6):
    return draw_until_effect(hand_size)


def stealth_poison():
    from spirit.game.card_effects.attacks_common import condition_attack
    from spirit.game.card_effects.support_common import switch_self_attack
    return condition_attack(SpecialConditions.POISONED,
                            also=switch_self_attack(optional=True))


# ----------------------------------------------------------------------
# Cyndaquil -- Charge Energy
# ----------------------------------------------------------------------

def charge_energy():
    """Search your deck for up to 2 basic Energy cards, reveal them, and put
    them into your hand."""
    return search_to_hand(predicate=is_basic_energy_card, count=2,
                          reveal=True,
                          prompt="Choose up to 2 basic Energy cards")


# ----------------------------------------------------------------------
# Dark Sylveon V -- Disarming Voice / Tricky Ribbon
# ----------------------------------------------------------------------

def disarming_voice():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.CONFUSED)


def tricky_ribbon():
    """Choose a random card from your opponent's hand. Your opponent reveals
    that card and shuffles it into their deck."""
    import random

    async def effect(ctx):
        if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
            await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        card = random.choice(hand)
        await ctx.reveal_cards([card], to_player=ctx.player_id)
        await ctx.shuffle_into_deck([card], ctx.opponent_id)
    return effect


# ----------------------------------------------------------------------
# Decidueye -- Splitting Arrow / Deep Forest Camo
# ----------------------------------------------------------------------

def splitting_arrow(bench_damage=20, count=2):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(bench_damage, pool="bench", count=count,
                        also_base=True)


def deep_forest_camo():
    """Prevent all damage done to this Pokemon by attacks from your opponent's
    Pokemon V and Pokemon GX."""
    def pred(calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        return is_pokemon_v_predicate(calc.attacker) \
            or is_pokemon_gx(getattr(calc.attacker, "archetype_id", None) or "")
    return prevent_damage_when(pred)


# ----------------------------------------------------------------------
# Deoxys -- Photon Boost / Deoxys V -- Psychic / Deoxys VMAX --
# Max Drain / Protective DNA / Deoxys VSTAR -- Psychic Javelin / Star Force
# ----------------------------------------------------------------------

def photon_boost(bonus=80):
    """If this Pokemon has any Fusion Strike Energy attached, this attack
    does 80 more damage."""
    from spirit.game.card_effects.attacks_common import bonus_if

    def has_fusion_strike_energy(ctx):
        return any(is_named(e, "Fusion Strike Energy")
                   for e in ctx.attached_energies(ctx.attacker))

    return bonus_if(has_fusion_strike_energy, bonus)


def psychic(per=30):
    """This attack does 30 more damage for each Energy attached to your
    opponent's Active Pokemon."""
    from spirit.game.card_effects.attacks_common import count_energy
    return _scaled(count_energy("opponent_active"), per)


def max_drain(heal=30):
    from spirit.game.card_effects.support_common import heal_attack
    return heal_attack(amount=heal)


def protective_dna(reduce=30):
    """All of your Pokemon take 30 less damage from attacks from your
    opponent's Pokemon VSTAR."""
    def attacker_is_vstar(attacker):
        return attacker is not None and \
            "VSTAR" in subtypes_for(getattr(attacker, "archetype_id", None) or "")
    return takes_less_passive(reduce, protects="team", attacker_pred=attacker_is_vstar)


def psychic_javelin(bench_damage=60):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(bench_damage, pool="bench", also_base=True)


def star_force(per=60):
    """60x for each Energy attached to both Active Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_per

    def energy_on_both_actives(ctx):
        mine = count_energy("self")(ctx)
        theirs = count_energy("opponent_active")(ctx)
        return mine + theirs

    return damage_per(energy_on_both_actives, per)


# ----------------------------------------------------------------------
# Donphan -- Earthquake
# ----------------------------------------------------------------------

def earthquake(bench_damage=20):
    from spirit.game.card_effects.attacks_common import spread_damage
    return spread_damage(bench_damage, side="mine", also_base=True)


# ----------------------------------------------------------------------
# Dragapult -- Mach Turn / Diving Swipe /
# Dragapult V -- Jet Assault / Dragapult VMAX -- Shred / Max Phantom
# ----------------------------------------------------------------------

def mach_turn():
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack(optional=True)


def diving_swipe():
    """Discard a random card from your opponent's hand."""
    from spirit.game.card_effects.attacks_common import discard_random_from_hand

    async def effect(ctx):
        if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
            await ctx.deal_damage()
        await discard_random_from_hand(ctx, ctx.opponent_id, 1)
    return effect


def jet_assault(bonus=80):
    """If this Pokemon moved from your Bench to the Active Spot this turn,
    this attack does 80 more damage."""
    from spirit.game.card_effects.attacks_common import bonus_if

    def moved_this_turn(ctx):
        return ctx.entered_active_this_turn(ctx.attacker)

    return bonus_if(moved_this_turn, bonus)


def max_phantom(counters=5):
    """Put 5 damage counters on your opponent's Benched Pokemon in any way
    you like."""
    async def effect(ctx):
        if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
            await ctx.deal_damage()
        await ctx.place_damage_counters(counters, ctx.opponent_bench())
    return effect


# ----------------------------------------------------------------------
# Dragonite V -- Hyper Beam / Dragonite VSTAR -- Giga Impact / Draconic Star
# ----------------------------------------------------------------------

def hyper_beam():
    from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
    return discard_opponent_energy_attack(1)


def giga_impact():
    async def effect(ctx):
        await ctx.deal_damage()
        lock_all_attacks(ctx, ctx.attacker)
    return effect


def draconic_star():
    """[VSTAR Power] Look at the top 12 cards of your deck and attach any
    number of Water or Lightning Energy cards you find there to your Pokemon
    in any way you like. Shuffle the other cards back into your deck."""
    def is_water_or_lightning(card):
        if not is_energy_card(card):
            return False
        return (energy_provides(card, PokemonTypes.WATER)
                or energy_provides(card, PokemonTypes.LIGHTNING))

    from spirit.game.card_effects.support_common import look_top_attach_energy
    return look_top_attach_energy(12, predicate=is_water_or_lightning,
                                  rest="shuffle")


# ----------------------------------------------------------------------
# Drednaw -- Vise Bite / Jaw Lock
# ----------------------------------------------------------------------

def vise_bite(per=30):
    """30 more for each Colorless in your opponent's Active Pokemon's Retreat
    Cost."""
    from spirit.game.card_effects.attacks_common import damage_per

    def defender_retreat_cost(ctx):
        defender = ctx.defender
        if defender is None:
            return 0
        return int(defender.get_attribute(AttrID.RETREAT_COST, 0) or 0)

    return damage_per(defender_retreat_cost, per)


def jaw_lock():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(no_retreat=True)


# ----------------------------------------------------------------------
# Dubwool V -- Revenge Blast / Soft Wool
# ----------------------------------------------------------------------

def revenge_blast(per=30):
    from spirit.game.card_effects.attacks_common import damage_per
    from spirit.game.card_effects.attacks_common import count_prizes_taken
    return damage_per(count_prizes_taken("opponent"), per)


def soft_wool(reduce=30):
    return takes_less_passive(reduce)


# ----------------------------------------------------------------------
# Duraludon -- Steel Beam / Metal Sharpener
# ----------------------------------------------------------------------

def steel_beam(self_damage=40):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_damage)


def metal_sharpener():
    def is_metal(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.METAL)

    return attach_from_discard(predicate=is_metal, count=1, target="choice",
                               prompt="Choose a Metal Energy card to attach")


# ----------------------------------------------------------------------
# Eevee -- Signs of Evolution / Wild Kick / Be Prepared / First Step
# ----------------------------------------------------------------------

def signs_of_evolution():
    """Search your deck for a card that evolves from Eevee, reveal it, and put
    it into your hand."""
    def evolves_from_eevee(card):
        definition = def_for(getattr(card, "archetype_id", None) or "")
        return getattr(definition, "evolves_from", None) == "Eevee"

    return search_to_hand(predicate=evolves_from_eevee, count=1, reveal=True,
                          prompt="Choose a card that evolves from Eevee")


def wild_kick():
    from spirit.game.card_effects.attacks_common import flip_or_nothing
    return flip_or_nothing()


def be_prepared():
    """Attach a basic Energy card from your hand to this Pokemon."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
        if not pool:
            return
        pick = await ctx.choose_cards(
            pool, 1, prompt="Choose a basic Energy card to attach to this Pokemon")
        if pick:
            await ctx.attach_energy(pick[0], ctx.source)
    return effect


# ----------------------------------------------------------------------
# Eevee V -- Brave Buddies / Eevee VMAX -- G-Max Cuddle
# ----------------------------------------------------------------------

def brave_buddies(bonus=80):
    from spirit.game.card_effects.attacks_common import bonus_if

    def played_supporter(ctx):
        return ctx.supporters_played_this_turn() > 0

    return bonus_if(played_supporter, bonus)


def g_max_cuddle():
    from spirit.game.card_effects.attacks_common import smokescreen_attack
    return smokescreen_attack()


# ----------------------------------------------------------------------
# Eiscue -- Ice Bonus
# ----------------------------------------------------------------------

def ice_bonus(draw=3):
    """Discard a Water Energy card from your hand. If you do, draw 3 cards."""
    from spirit.game.card_effects.support_common import discard_then_draw

    def is_water(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.WATER)

    return discard_then_draw(1, draw, optional=True, predicate=is_water)


# ----------------------------------------------------------------------
# Eldegoss -- Blessing of Fluff / Eldegoss V -- Float Up / Happy Match
# ----------------------------------------------------------------------

def blessing_of_fluff():
    def is_grass(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.GRASS)

    return search_attach_energy(
        predicate=is_grass, count=3,
        target_pred=is_benched,
        prompt="Choose up to 3 Grass Energy cards to attach to your Benched Pokemon",
    )


def float_up():
    from spirit.game.card_effects.support_common import remove_self_from_play
    return remove_self_from_play(destination="deck", optional=True)


def happy_match():
    """When you play this Pokemon from your hand onto your Bench during your
    turn, you may put a Supporter card from your discard pile into your hand."""
    from spirit.game.card_effects.support_common import recover_from_discard
    from spirit.game.session.effects import is_supporter_card
    return recover_from_discard(predicate=is_supporter_card, count=1,
                                to="hand", reveal=True,
                                prompt="Choose a Supporter card to put into your hand")


# ----------------------------------------------------------------------
# Empoleon V -- Swirling Slice / Emperor's Eyes
# ----------------------------------------------------------------------

def swirling_slice():
    """Deal the attack's damage, then move an Energy from this Pokemon to
    1 of your Benched Pokemon."""
    async def effect(ctx):
        await ctx.deal_damage()
        attached = ctx.attached_energies(ctx.attacker)
        if not attached:
            return
        pick = await ctx.choose_cards(
            attached, 1, prompt="Choose an Energy card to move")
        if not pick:
            return
        bench = ctx.my_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your Benched Pokemon to move the Energy to")
        if target is None:
            return
        await ctx.move_energy(pick[0], target)
    return effect


def emperors_eyes():
    """As long as this Pokemon is in the Active Spot, your opponent's Basic
    Pokemon in play have no Abilities, except for Pokemon with a Rule Box."""
    from spirit.game.card_effects.passives_common import (
        ability_lock_passive, is_in_active_spot, opposing_pokemon,
    )

    # Ability locks read target_pred(pokemon, carrier); gate the whole lock on
    # the carrier sitting Active by folding the check into target_pred.
    def combined(pokemon, carrier):
        if not opposing_pokemon(pokemon, carrier):
            return False
        if not is_basic_pokemon_predicate(pokemon):
            return False
        if not is_pokemon_without_rule_box(pokemon):
            return False
        holder = carrier_pokemon(carrier) or carrier
        return is_in_active_spot(holder)

    return ability_lock_passive(combined)


# ----------------------------------------------------------------------
# Espeon -- Psy Bolt / Psychic / Espeon V -- Zen Shot
# ----------------------------------------------------------------------

def psy_bolt():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.PARALYZED, flip=True)


def zen_shot(amount=60):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(amount, pool="any")


# ----------------------------------------------------------------------
# Eternatus V -- Power Accelerator / Dynamax Cannon /
# Eternatus VMAX -- Dread End / Eternal Zone
# ----------------------------------------------------------------------

def power_accelerator():
    """You may attach a Darkness Energy card from your hand to 1 of your
    Benched Pokemon."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_energy_card(c)
                and energy_provides(c, PokemonTypes.DARKNESS)]
        if not pool:
            return
        bench = ctx.my_bench()
        if not bench:
            return
        pick = await ctx.choose_cards(
            pool, 1, prompt="Choose a Darkness Energy card to attach")
        if not pick:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your Benched Pokemon to attach to")
        if target is None:
            return
        await ctx.attach_energy(pick[0], target)
    return effect


def dynamax_cannon(bonus=120):
    from spirit.game.card_effects.attacks_common import bonus_if, defender_is_v
    return bonus_if(defender_is_v, bonus)


def dread_end(per=30):
    """30x for each of your Darkness Pokemon in play."""
    from spirit.game.card_effects.attacks_common import damage_per, count_in_play
    return damage_per(count_in_play("mine", is_type(PokemonTypes.DARKNESS)), per)


def eternal_zone(capacity=8):
    """If all of your Pokemon in play are Darkness type, you can have up to 8
    Pokemon on your Bench."""
    class EternalZonePassive(Passive):
        def bench_capacity(self, player_id, carrier):
            holder = carrier_pokemon(carrier)
            if holder is None or holder.owning_player_id != player_id:
                return None
            board = _board_of(carrier)
            if board is None:
                return None
            mine = board.pokemon_in_play(player_id)
            if not mine:
                return None
            if all(is_type(PokemonTypes.DARKNESS)(p) for p in mine):
                return capacity
            return None
    return EternalZonePassive()


def _board_of(entity):
    node = entity
    while node is not None:
        if hasattr(node, "pokemon_in_play"):
            return node
        node = getattr(node, "parent", None)
    return None


# ----------------------------------------------------------------------
# Finneon -- Oceanic Accompaniment
# ----------------------------------------------------------------------

def oceanic_accompaniment():
    """As often as you like during your turn, attach a Water Energy card from
    your hand to 1 of your Pokemon that has the Swim Freely attack."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_energy_card(c)
                and energy_provides(c, PokemonTypes.WATER)]
        if not pool:
            return
        candidates = [p for p in ctx.my_pokemon_in_play()
                      if _pokemon_has_attack(p, "Swim Freely")]
        if not candidates:
            return
        pick = await ctx.choose_cards(
            pool, 1, prompt="Choose a Water Energy card to attach")
        if not pick:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokemon with the Swim Freely attack")
        if target is None:
            return
        await ctx.attach_energy(pick[0], target)
    return effect


def _pokemon_has_attack(pokemon, title: str) -> bool:
    definition = def_for(getattr(pokemon, "archetype_id", None) or "")
    return any(getattr(a, "title", None) == title
               for a in getattr(definition, "abilities", []) or [])


# ----------------------------------------------------------------------
# Flaaffy -- Dynamotor
# ----------------------------------------------------------------------

def dynamotor():
    """Once during your turn, attach a Lightning Energy card from your
    discard pile to 1 of your Benched Pokemon."""
    def is_lightning(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.LIGHTNING)

    return attach_from_discard(predicate=is_lightning, count=1,
                               target=is_benched,
                               prompt="Choose a Lightning Energy card to attach")


# ----------------------------------------------------------------------
# Flapple -- Flight Up / Corrosive Acid / Acid Spray / Apple Drop
# ----------------------------------------------------------------------

def flight_up(count=3):
    """Attach up to 3 basic Energy cards from your discard pile to 1 of your
    Benched Pokemon."""
    return attach_from_discard(predicate=is_basic_energy_card, count=count,
                               target=is_benched,
                               prompt="Choose basic Energy cards to attach")


def corrosive_acid():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.BURNED)


def acid_spray():
    """Flip a coin. If heads, discard an Energy from your opponent's Active
    Pokemon."""
    from spirit.game.card_effects.attacks_common import (
        discard_opponent_energy_attack, flip_or_nothing)
    return discard_opponent_energy_attack(1, after_damage=True)


def apple_drop(counters=2):
    """Once during your turn, put 2 damage counters on 1 of your opponent's
    Pokemon. If you placed any damage counters this way, shuffle this Pokemon
    and all attached cards into your deck."""
    from spirit.game.card_effects.support_common import remove_self_from_play

    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose 1 of your opponent's Pokemon")
        if target is None:
            return
        await ctx.deal_damage(counters * 10, target=target, as_counters=True)
        await remove_self_from_play(destination="deck")(ctx)
    return effect


# ----------------------------------------------------------------------
# Flareon -- Singe / Kindle / Flareon V -- Flaming Breath / Scorching Column /
# Flareon VMAX -- Max Detonate
# ----------------------------------------------------------------------

def singe():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.BURNED)


def kindle():
    """Discard an Energy from this Pokemon. If you do, discard an Energy from
    your opponent's Active Pokemon."""
    async def effect(ctx):
        await ctx.deal_damage()
        attached = ctx.attached_energies(ctx.attacker)
        if not attached:
            return
        pick = await ctx.choose_cards(
            attached, 1, prompt="Choose an Energy card to discard from this Pokemon")
        if not pick:
            return
        await ctx.discard_cards(pick)
        defender = ctx.opponent_active()
        if defender is None or ctx.effects_blocked(defender):
            return
        await ctx.discard_energy_from(
            defender, 1, prompt="Choose an Energy to discard from the Defending Pokemon")
    return effect


def flaming_breath():
    def is_fire(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.FIRE)

    return search_attach_energy(predicate=is_fire, count=1, to_self=True,
                                prompt="Choose a Fire Energy card to attach")


def scorching_column():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.BURNED)


def max_detonate(per=100, mill_count=5):
    """Discard the top 5 cards of your deck. This attack does 100 damage for
    each Energy card you discarded this way."""
    from spirit.game.card_effects.attacks_common import mill_scaled_damage
    return mill_scaled_damage(mill_count, per, pred=is_energy_card)


# ----------------------------------------------------------------------
# Frosmoth -- Ice Dance
# ----------------------------------------------------------------------

def ice_dance():
    """As often as you like during your turn, attach a Water Energy card from
    your hand to 1 of your Benched Water Pokemon."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_energy_card(c)
                and energy_provides(c, PokemonTypes.WATER)]
        if not pool:
            return
        candidates = [p for p in ctx.my_bench()
                      if is_type(PokemonTypes.WATER)(p)]
        if not candidates:
            return
        pick = await ctx.choose_cards(
            pool, 1, prompt="Choose a Water Energy card to attach")
        if not pick:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose 1 of your Benched Water Pokemon")
        if target is None:
            return
        await ctx.attach_energy(pick[0], target)
    return effect


# ----------------------------------------------------------------------
# Galarian Articuno -- Psylaser / Cruel Charge
# ----------------------------------------------------------------------

def psylaser(damage=120):
    """Discard all Psychic Energy from this Pokemon. This attack does 120
    damage to 1 of your opponent's Pokemon."""
    from spirit.game.card_effects.attacks_common import (
        self_energy_discard_attack, snipe_attack)

    async def effect(ctx):
        await self_energy_discard_attack(
            all_energy=True, energy_type=PokemonTypes.PSYCHIC,
            before_damage=True, then_damage=damage)(ctx)
    return effect


def cruel_charge(energy_type=PokemonTypes.PSYCHIC, count=2):
    """When you play this Pokemon from your hand onto your Bench during your
    turn, attach up to 2 <type> Energy cards from your hand to this Pokemon."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_energy_card(c)
                and energy_provides(c, energy_type)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, count, minimum=0,
            prompt="Choose up to %d %s Energy cards to attach" % (
                count, getattr(energy_type, "name", str(energy_type))))
        if not picks:
            return
        for card in picks:
            await ctx.attach_energy(card, ctx.source)
    return effect


# ----------------------------------------------------------------------
# Galarian Moltres -- Fiery Wrath / Malevolent Charge
# ----------------------------------------------------------------------

def fiery_wrath(per=50):
    from spirit.game.card_effects.attacks_common import damage_per
    from spirit.game.card_effects.attacks_common import count_prizes_taken
    return damage_per(count_prizes_taken("opponent"), per)


def malevolent_charge():
    return cruel_charge(PokemonTypes.DARKNESS, 2)


# ----------------------------------------------------------------------
# Galarian Mr. Rime -- Shuffle Dance
# ----------------------------------------------------------------------

def shuffle_dance():
    """Once during your turn, switch 1 of your opponent's face-down Prize
    cards with the top card of their deck. (The cards stay face down.)"""
    import random

    async def effect(ctx):
        prize_area = ctx.board.find_player_area(
            ctx.opponent_id, "prizePile")
        prizes = list(prize_area.children) if prize_area else []
        if not prizes:
            return
        target = random.choice(prizes)
        top = ctx.deck_top(1, player_id=ctx.opponent_id)
        if not top:
            return
        await ctx.put_in_prizes([top[0]], player_id=ctx.opponent_id)
    return effect


# ----------------------------------------------------------------------
# Galarian Obstagoon -- Rampaging Kick / Obstruct / Untamed Shout
# ----------------------------------------------------------------------

def rampaging_kick(count=2):
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=count,
                                      energy_type=PokemonTypes.DARKNESS)


def obstruct():
    """During your opponent's next turn, prevent all damage done to this
    Pokemon by attacks from Basic Pokemon."""
    def attacker_is_basic(calc, carrier):
        return is_basic_pokemon_predicate(calc.attacker)

    async def effect(ctx):
        await ctx.deal_damage()
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, prevent_damage_when(attacker_is_basic))
    return effect


def untamed_shout(counters=3):
    """When you play this Pokemon from your hand to evolve 1 of your Pokemon
    during your turn, put 3 damage counters on 1 of your opponent's Pokemon."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose 1 of your opponent's Pokemon")
        if target is None:
            return
        await ctx.deal_damage(counters * 10, target=target, as_counters=True)
    return effect


# ----------------------------------------------------------------------
# Galarian Perrserker -- Steely Spirit
# ----------------------------------------------------------------------

def steely_spirit(amount=20):
    """Your Metal Pokemon's attacks do 20 more damage to your opponent's
    Active Pokemon."""
    return team_damage_boost_passive(
        amount, attacker_pred=is_type(PokemonTypes.METAL))


# ----------------------------------------------------------------------
# Galarian Ponyta -- Heal Pulse / Galarian Rapidash V -- Libra Horn
# ----------------------------------------------------------------------

def heal_pulse(amount=30):
    """Heal 30 damage from 1 of your Pokemon."""
    from spirit.game.card_effects.support_common import heal_targets
    return heal_targets(amount, scope="choice")


def libra_horn(hp_floor=100):
    """Put damage counters on 1 of your opponent's Pokemon until its remaining
    HP is 100."""
    async def effect(ctx):
        if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
            await ctx.deal_damage()
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose 1 of your opponent's Pokemon")
        if target is None:
            return
        current = int(target.get_attribute(AttrID.HP, 0) or 0)
        if current > hp_floor:
            await ctx.deal_damage(
                current - hp_floor, target=target, as_counters=True)
    return effect


# ----------------------------------------------------------------------
# Galarian Sirfetch'd V -- Meteor Smash / Resolute Spear
# ----------------------------------------------------------------------

def meteor_smash():
    async def effect(ctx):
        await ctx.deal_damage()
        lock_all_attacks(ctx, ctx.attacker)
    return effect


def resolute_spear():
    """Once during your turn, when this Pokemon moves from your Bench to the
    Active Spot, move any amount of Fighting Energy from your other Pokemon
    to it."""
    async def effect(ctx):
        others = [p for p in ctx.my_pokemon_in_play() if p is not ctx.source]
        holders = [p for p in others
                   if any(energy_provides(e, PokemonTypes.FIGHTING)
                          for e in ctx.attached_energies(p))]
        if not holders:
            return
        source = await ctx.choose_pokemon(
            holders, "Choose 1 of your other Pokemon with Fighting Energy")
        if source is None:
            return
        movable = [e for e in ctx.attached_energies(source)
                   if energy_provides(e, PokemonTypes.FIGHTING)]
        if not movable:
            return
        picks = await ctx.choose_cards(
            movable, len(movable), minimum=0,
            prompt="Choose any amount of Fighting Energy to move")
        for card in picks:
            await ctx.move_energy(card, ctx.source)
    return effect


# ----------------------------------------------------------------------
# Galarian Slowpoke -- Everyone Laze Around
# ----------------------------------------------------------------------

def everyone_laze_around(amount=10):
    """Heal 10 damage from each of your Pokemon."""
    from spirit.game.card_effects.support_common import heal_targets
    return heal_targets(amount, scope="each_own")


# ----------------------------------------------------------------------
# Galarian Zapdos -- Zapper Kick / Strong Legs Charge
# ----------------------------------------------------------------------

def zapper_kick():
    """You may discard all Energy from this Pokemon. If you do, your
    opponent's Active Pokemon is now Paralyzed."""
    async def effect(ctx):
        await ctx.deal_damage()
        if not ctx.attached_energies(ctx.attacker):
            return
        if not await ctx.ask_yes_no(
                "Discard all Energy from this Pokemon to Paralyze?"):
            return
        await ctx.discard_cards(ctx.attached_energies(ctx.attacker))
        defender = ctx.defender
        if defender is not None:
            await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    return effect


def strong_legs_charge():
    return cruel_charge(PokemonTypes.FIGHTING, 2)


# ----------------------------------------------------------------------
# Gallade V -- Rising Sword / Buster Swing
# ----------------------------------------------------------------------

def rising_sword(per=50):
    """50 more for each Prize card you have taken."""
    from spirit.game.card_effects.attacks_common import damage_per
    from spirit.game.card_effects.attacks_common import count_prizes_taken
    return damage_per(count_prizes_taken("mine"), per)


def buster_swing():
    """This attack's damage isn't affected by Resistance."""
    async def effect(ctx):
        await ctx.deal_damage(ignore_resistance=True)
    return effect


# ----------------------------------------------------------------------
# Garbodor -- Poisonous Puddle
# ----------------------------------------------------------------------

def poisonous_puddle():
    """Once during your turn, if a Stadium is in play, make your opponent's
    Active Pokemon Poisoned."""
    async def effect(ctx):
        if not ctx.stadium_in_play():
            return
        defender = ctx.opponent_active()
        if defender is None:
            return
        await ctx.apply_special_condition(defender, SpecialConditions.POISONED)
    return effect


# ----------------------------------------------------------------------
# Gardevoir V -- Swelling Pulse
# ----------------------------------------------------------------------

def swelling_pulse(bonus=80):
    """If this Pokemon was healed during this turn, this attack does 80 more
    damage."""
    from spirit.game.card_effects.attacks_common import bonus_if

    def healed_this_turn(ctx):
        return ctx.attacker.entity_id in ctx.session.turn_state.healed_entities

    return bonus_if(healed_this_turn, bonus)


# ----------------------------------------------------------------------
# Gengar -- Screaming Circle / Netherworld Gate / Hypnoblast / Life Shaker
# ----------------------------------------------------------------------

def screaming_circle(per=2):
    """Put 2 damage counters on your opponent's Active Pokemon for each of
    your opponent's Benched Pokemon."""
    from spirit.game.card_effects.attacks_common import place_counters

    def counters(ctx):
        return per * count_bench("opponent")(ctx)

    return place_counters(counters, target="opponent_active")


def netherworld_gate():
    """[usable_from discard] Once during your turn, if this Pokemon is in
    your discard pile, put it onto your Bench. If you do, put 3 damage
    counters on this Pokemon."""
    async def effect(ctx):
        if not await ctx.bench_pokemon(ctx.source):
            return
        await ctx.place_damage_counters(3, [ctx.source])
    return effect


def hypnoblast():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.ASLEEP)


def life_shaker():
    """As often as you like during your turn, move 1 damage counter from 1 of
    your Psychic Pokemon to another of your Psychic Pokemon."""
    async def effect(ctx):
        psychics = [p for p in ctx.my_pokemon_in_play()
                    if is_type(PokemonTypes.PSYCHIC)(p)]
        damaged = [p for p in psychics
                   if int(p.get_attribute(AttrID.HP, 0) or 0) < ctx.max_hp(p)]
        if len(damaged) < 2:
            return
        source = await ctx.choose_pokemon(
            damaged, "Choose 1 of your damaged Psychic Pokemon")
        if source is None:
            return
        others = [p for p in psychics if p is not source]
        if not others:
            return
        target = await ctx.choose_pokemon(
            others, "Choose a Psychic Pokemon to move the damage counter to")
        if target is None:
            return
        await ctx.deal_damage(10, target=target, as_counters=True)
        await ctx.heal(10, source)
    return effect


# ----------------------------------------------------------------------
# Giratina V -- Abyss Seeking / Shred
# ----------------------------------------------------------------------

def abyss_seeking(take=2, look=4):
    """Look at the top 4 cards of your deck and put 2 of them into your hand.
    Put the other cards in the Lost Zone."""
    async def effect(ctx):
        top = ctx.deck_top(look)
        if not top:
            return
        picks = await ctx.choose_cards(
            top, take, minimum=0, prompt="Choose 2 cards to put into your hand",
            display_cards=top)
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
        rest = [c for c in top if c not in picks]
        if rest:
            await ctx.move_to_lost_zone(rest)
    return effect


# ----------------------------------------------------------------------
# Glaceon -- Hail / Frosty Typhoon / Glaceon V -- Frost Charge /
# Glaceon VSTAR -- Icicle Shot / Crystal Star
# ----------------------------------------------------------------------

def hail(amount=20):
    """This attack does 20 damage to each of your opponent's Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_all_opponents
    return damage_all_opponents(amount)


def frosty_typhoon():
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.session.turn_state.lock_attack(
            ctx.attacker.entity_id,
            ctx.ability.ability_id,
        )
    return effect


def frost_charge():
    def is_water(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.WATER)

    return search_attach_energy(predicate=is_water, count=1, to_self=True,
                                prompt="Choose a Water Energy card to attach")


def icicle_shot():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(no_retreat=True)


def crystal_star():
    """[VSTAR Power] During your opponent's next turn, prevent all damage
    from and effects of attacks done to this Pokemon."""
    from spirit.game.card_effects.passives_common import protect_next_turn
    return protect_next_turn(prevent=True, effects_too=True)


# ----------------------------------------------------------------------
# Gossifleur -- Sing
# ----------------------------------------------------------------------

def sing():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.ASLEEP)


# ----------------------------------------------------------------------
# Greninja -- Mist Slash / Shadow Knife
# ----------------------------------------------------------------------

def mist_slash():
    """This attack's damage isn't affected by Weakness or Resistance, or by
    any effects on your opponent's Active Pokemon."""
    async def effect(ctx):
        await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True,
                              ignore_target_effects=True)
    return effect


def shadow_knife(counters=1):
    """When you play this Pokemon from your hand onto your Bench during your
    turn, put 1 damage counter on 1 of your opponent's Pokemon."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose 1 of your opponent's Pokemon")
        if target is None:
            return
        await ctx.deal_damage(counters * 10, target=target, as_counters=True)
    return effect


# ----------------------------------------------------------------------
# Grimmsnarl V -- Spiky Knuckle
# ----------------------------------------------------------------------

def spiky_knuckle(count=2):
    """Put 2 Darkness Energy attached to this Pokemon into your hand."""
    async def effect(ctx):
        attached = [e for e in ctx.attached_energies(ctx.attacker)
                    if energy_provides(e, PokemonTypes.DARKNESS)]
        if not attached:
            return
        picks = await ctx.choose_cards(
            attached, count, minimum=0,
            prompt="Choose Darkness Energy cards to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    return effect


# ----------------------------------------------------------------------
# Grookey -- Full On
# ----------------------------------------------------------------------

def full_on():
    from spirit.game.card_effects.attacks_common import flip_or_nothing
    return flip_or_nothing()


# ----------------------------------------------------------------------
# Hatenna -- Find a Friend
# ----------------------------------------------------------------------

def find_a_friend():
    def is_pokemon(card):
        definition = def_for(getattr(card, "archetype_id", None) or "")
        return getattr(definition, "card_type", None) == "Pokemon" or \
            hasattr(definition, "hp")

    return search_to_hand(predicate=is_pokemon, count=1, reveal=True,
                          prompt="Choose a Pokemon to put into your hand")


# ----------------------------------------------------------------------
# Hatterene V -- Confounding Pulse / Mental Crush
# ----------------------------------------------------------------------

def confounding_pulse():
    """Switch 1 of your opponent's Benched Pokemon with their Active Pokemon.
    The new Active Pokemon is now Confused."""
    from spirit.game.card_effects.support_common import gust_then

    async def confuse_new_active(ctx, new_active):
        if new_active is not None:
            await ctx.apply_special_condition(
                new_active, SpecialConditions.CONFUSED)

    return gust_then(confuse_new_active)


def mental_crush(bonus=90):
    """If your opponent's Active Pokemon is Confused, this attack does 90 more
    damage."""
    from spirit.game.card_effects.attacks_common import condition_bonus_attack
    return condition_bonus_attack(bonus, SpecialConditions.CONFUSED)


# ----------------------------------------------------------------------
# Hisuian Basculegion -- Grudge Dive
# ----------------------------------------------------------------------

def grudge_dive(bonus=90):
    """If any of your Pokemon were Knocked Out by damage from an attack from
    your opponent's Pokemon during their last turn, this attack does 90 more
    damage, and your opponent's Active Pokemon is now Confused."""
    from spirit.game.card_effects.attacks_common import bonus_if

    def ko_last_turn(ctx):
        return ctx.kos_suffered_last_turn(ctx.player_id) > 0

    async def effect(ctx):
        base = getattr(ctx.ability, "damage", 0) or 0
        amount = base + (bonus if ko_last_turn(ctx) else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        if ko_last_turn(ctx) and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    return effect


# ----------------------------------------------------------------------
# Hisuian Basculin -- Submerge Silently
# ----------------------------------------------------------------------

def submerge_silently():
    """You can use this attack only if you go second, and only during your
    first turn. During your opponent's next turn, prevent all damage done to
    this Pokemon by attacks."""
    from spirit.game.card_effects.passives_common import protect_next_turn

    async def effect(ctx):
        await protect_next_turn(prevent=True)(ctx)
    return effect


def submerge_silently_condition(board, player_id, pokemon=None) -> bool:
    """Only usable going second on the first turn."""
    state = getattr(board, "turn_state", None)
    return state is not None and state.turn_number == 2


# ----------------------------------------------------------------------
# Hisuian Decidueye V -- Mountain Hunt / Close-Quarters Shooting
# ----------------------------------------------------------------------

def mountain_hunt(count=2):
    return search_to_hand(count=count, reveal=False,
                          prompt="Choose up to 2 cards to put into your hand")


def close_quarters_shooting():
    async def effect(ctx):
        await ctx.deal_damage(ignore_target_effects=True)
    return effect


# ----------------------------------------------------------------------
# Hisuian Electrode V -- Tantrum Blast / Solar Shot
# ----------------------------------------------------------------------

def tantrum_blast(per=100):
    """100x for each Special Condition affecting this Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_per

    def condition_count(ctx):
        conds = ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        return len([c for c in conds if c not in (None, -1, "")])

    return damage_per(condition_count, per)


def solar_shot():
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(all_energy=True)


# ----------------------------------------------------------------------
# Hisuian Samurott -- Dark Mastery / Wily Stance /
# Hisuian Samurott V -- Basket Crash / Shadow Slash
# ----------------------------------------------------------------------

def dark_mastery(per=20):
    """20 more for each Energy attached to all of your Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_per
    return damage_per(count_energy("mine"), per)


def wily_stance(draw=3):
    """You must discard a card from your hand to use this Ability. Once during
    your turn, you may draw 3 cards."""
    from spirit.game.card_effects.support_common import discard_then_draw
    return discard_then_draw(1, draw, optional=False)


def basket_crash(count=2):
    """Discard up to 2 Pokemon Tools from your opponent's Pokemon."""
    async def effect(ctx):
        holders = [p for p in ctx.opponent_pokemon_in_play()
                   if any(_is_tool_card(c) for c in p.children)]
        if not holders:
            return
        holder = await ctx.choose_pokemon(
            holders, "Choose 1 of your opponent's Pokemon with a Pokemon Tool")
        if holder is None:
            return
        tools = [c for c in holder.children if _is_tool_card(c)]
        picks = await ctx.choose_cards(
            tools, count, minimum=0,
            prompt="Choose up to %d Pokemon Tools to discard" % count)
        if picks:
            await ctx.discard_cards(picks)
    return effect


def shadow_slash():
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=1)


# ----------------------------------------------------------------------
# Hisuian Typhlosion V -- Petrifying Flame / Singe
# ----------------------------------------------------------------------

def petrifying_flame():
    return tricky_ribbon()


# ----------------------------------------------------------------------
# Hisuian Zoroark V -- Void Return / Shadow Cyclone /
# Hisuian Zoroark VSTAR -- Ticking Curse / Phantom Star
# ----------------------------------------------------------------------

def void_return():
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack(optional=True)


def shadow_cyclone():
    return swirling_slice()


def ticking_curse(per=50):
    """50x for each of your Pokemon that has any damage counters on it."""
    from spirit.game.card_effects.attacks_common import damage_per

    def damaged_own(ctx):
        return sum(1 for p in ctx.my_pokemon_in_play()
                   if int(p.get_attribute(AttrID.HP, 0) or 0) < ctx.max_hp(p))

    return damage_per(damaged_own, per)


def phantom_star(draw=7):
    """[VSTAR Power] Discard your hand and draw 7 cards."""
    async def effect(ctx):
        await ctx.discard_cards(list(ctx.hand()))
        await ctx.draw_cards(draw)
    return effect


# ----------------------------------------------------------------------
# Hoopa V -- Shadow Impact / Two-Faced
# ----------------------------------------------------------------------

def shadow_impact(counters=3):
    """Put 3 damage counters on 1 of your Pokemon."""
    from spirit.game.card_effects.attacks_common import place_counters
    return place_counters(counters, target="choose_own")


def two_faced():
    """As long as this Pokemon is in play, it is Psychic and Darkness type."""
    class TwoFacedPassive(Passive):
        def modify_pokemon_types(self, types, pokemon, carrier):
            if carrier_pokemon(carrier) is not pokemon:
                return types
            return [PokemonTypes.PSYCHIC.value, PokemonTypes.DARKNESS.value]
    return TwoFacedPassive()


# ----------------------------------------------------------------------
# Houndoom -- Single Strike Roar
# ----------------------------------------------------------------------

def single_strike_roar():
    """Once during your turn, search your deck for a Single Strike Energy card
    and attach it to 1 of your Single Strike Pokemon. If you attached Energy,
    put 2 damage counters on that Pokemon."""
    def is_single_strike_energy(card):
        return is_named(card, "Single Strike Energy")

    def is_single_strike(pokemon):
        return "Single Strike" in subtypes_for(
            getattr(pokemon, "archetype_id", None) or "")

    async def effect(ctx):
        targets = [p for p in ctx.my_pokemon_in_play() if is_single_strike(p)]
        if not targets:
            return
        target = await ctx.choose_pokemon(
            targets, "Choose 1 of your Single Strike Pokemon")
        if target is None:
            return
        await search_attach_energy(
            predicate=is_single_strike_energy, count=1, to_self=False,
            prompt="Choose a Single Strike Energy card to attach")(ctx)
        await ctx.deal_damage(20, target=target, as_counters=True)
    return effect


# ----------------------------------------------------------------------
# Hydreigon -- Dark Squall
# ----------------------------------------------------------------------

def dark_squall():
    """As often as you like during your turn, attach a Darkness Energy card
    from your hand to 1 of your Pokemon."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_energy_card(c)
                and energy_provides(c, PokemonTypes.DARKNESS)]
        if not pool:
            return
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        pick = await ctx.choose_cards(
            pool, 1, prompt="Choose a Darkness Energy card to attach")
        if not pick:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokemon to attach the Darkness Energy to")
        if target is None:
            return
        await ctx.attach_energy(pick[0], target)
    return effect


# ----------------------------------------------------------------------
# Hydreigon C -- Berserker Blade
# ----------------------------------------------------------------------

def berserker_blade(bench_damage=20, count=2):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(bench_damage, pool="bench", count=count, also_base=True)


# ----------------------------------------------------------------------
# Ice Rider Calyrex V -- Blizzard
# ----------------------------------------------------------------------

def blizzard(bench_damage=10):
    from spirit.game.card_effects.attacks_common import spread_damage
    return spread_damage(bench_damage, side="opponent", also_base=True)


# ----------------------------------------------------------------------
# Infernape V -- Meteor Punch / Bright Flame
# ----------------------------------------------------------------------

def meteor_punch(per=30):
    """Flip a coin until you get tails. This attack does 30 damage for each
    heads."""
    from spirit.game.card_effects.attacks_common import flip_damage

    async def effect(ctx):
        heads = await ctx.flip_until_tails(
            ctx.ability.title if ctx.ability else "")
        amount = per * heads
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


def bright_flame(count=2):
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=count)


# ----------------------------------------------------------------------
# Inteleon -- Quick Shooting / Inteleon V -- Snipe Shot / Aqua Report
# ----------------------------------------------------------------------

def quick_shooting(counters=2):
    """Once during your turn, put 2 damage counters on 1 of your opponent's
    Pokemon."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose 1 of your opponent's Pokemon")
        if target is None:
            return
        await ctx.deal_damage(counters * 10, target=target, as_counters=True)
    return effect


def snipe_shot(amount=40):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(amount, pool="any")


def aqua_report():
    """Your opponent reveals their hand."""
    async def effect(ctx):
        if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
            await ctx.deal_damage()
        await ctx.reveal_cards(list(ctx.hand(ctx.opponent_id)),
                               to_player=ctx.player_id)
    return effect


# ----------------------------------------------------------------------
# Jirachi V -- Hypnostrike / Wish Connector
# ----------------------------------------------------------------------

def hypnostrike():
    """Both Active Pokemon are now Asleep."""
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.ASLEEP, both_actives=True)


async def wish_connector(ctx):
    """[ON_ALLY_KNOCKED_OUT] When 1 of your Basic Pokemon is Knocked Out by
    damage from an attack from your opponent's Pokemon, move a basic Energy
    card from that Pokemon to another of your Pokemon."""
    victim = ctx.ko_pokemon
    if victim is None or not is_basic_pokemon_predicate(victim):
        return
    energies = [c for c in getattr(victim, "children", [])
                if is_basic_energy_card(c)]
    if not energies:
        return
    others = [p for p in ctx.board.pokemon_in_play(ctx.player_id)
              if p is not victim]
    if not others:
        return
    target = await ctx.choose_pokemon(
        others, "Choose a Pokemon to move the basic Energy to")
    if target is not None:
        await ctx.move_energy(energies[0], target)


# ----------------------------------------------------------------------
# Jolteon -- Energize / Thunder / Jolteon V -- Thunder Spear / Pin Missile /
# Jolteon VMAX -- Max Thunder Rumble
# ----------------------------------------------------------------------

def energize():
    def is_lightning(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.LIGHTNING)

    return attach_from_discard(predicate=is_lightning, count=1, target="self",
                               prompt="Choose a Lightning Energy card to attach")


def thunder(self_damage=30):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_damage)


def pin_missile(per=60, coins=4):
    from spirit.game.card_effects.attacks_common import flip_damage
    return flip_damage(coins=coins, per_heads=per)


def max_thunder_rumble(bench_damage=100):
    """This attack also does 100 damage to 1 of your opponent's Benched
    Pokemon that has any damage counters on it."""
    from spirit.game.card_effects.attacks_common import snipe_attack

    def has_counters(pokemon):
        return int(pokemon.get_attribute(AttrID.HP, 0) or 0) < \
            _max_hp_of(pokemon)

    return snipe_attack(bench_damage, pool=has_counters, also_base=True)


def _max_hp_of(pokemon):
    from spirit.game.session.passives import effective_max_hp
    board = _board_of(pokemon)
    if board is None:
        return int(getattr(pokemon, "_base_max_hp", 0) or 0)
    return effective_max_hp(board, pokemon)


# ----------------------------------------------------------------------
# Kangaskhan -- Rally Back
# ----------------------------------------------------------------------

def rally_back(bonus=90):
    """If any of your Pokemon were Knocked Out by damage from an attack from
    your opponent's Pokemon during their last turn, this attack does 90 more
    damage."""
    from spirit.game.card_effects.attacks_common import bonus_if

    def ko_last_turn(ctx):
        return ctx.kos_suffered_last_turn(ctx.player_id) > 0

    return bonus_if(ko_last_turn, bonus)


# ----------------------------------------------------------------------
# Kirlia / Liepard -- Refinement / Trade
# ----------------------------------------------------------------------

def refinement(draw=2):
    from spirit.game.card_effects.support_common import discard_then_draw
    return discard_then_draw(1, draw, optional=False)


def trade(draw=2):
    return refinement(draw)


# ----------------------------------------------------------------------
# Kleavor V -- Axe Slash / Kleavor VSTAR -- Axe Break / Rampaging Star
# ----------------------------------------------------------------------

def axe_slash():
    """Discard an Energy from this Pokemon. If you do, discard an Energy from
    your opponent's Active Pokemon."""
    return kindle()


def axe_break(bench_damage=60):
    """Deals printed damage to the Active; also `bench_damage` to 1 of the
    opponent's Benched Pokemon V (no W/R)."""
    async def effect(ctx):
        await ctx.deal_damage()
        bench = [p for p in ctx.opponent_bench() if is_pokemon_v(p.archetype_id)]
        if bench:
            target = await ctx.choose_pokemon(
                bench, "Choose 1 of your opponent's Benched Pokémon V"
            )
            if target is not None:
                await ctx.deal_damage(bench_damage, target=target,
                                      apply_modifiers=False)
    return effect


def rampaging_star(per=30):
    """30x for each Pokemon in your discard pile."""
    from spirit.game.card_effects.attacks_common import damage_per, count_discard

    def pokemon_in_discard(ctx):
        return count_discard("mine", lambda c: _is_pokemon_card(c))(ctx)

    return damage_per(pokemon_in_discard, per)


def _is_pokemon_card(card):
    from spirit.game.session.effects import is_pokemon_card
    if getattr(card, "archetype_id", None) is None:
        return False
    return is_pokemon_card(card) or \
        getattr(def_for(card.archetype_id), "card_type", None) == "Pokemon"


# ----------------------------------------------------------------------
# Lance's Charizard V -- Flamethrower
# ----------------------------------------------------------------------

def flamethrower():
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=1)


# ----------------------------------------------------------------------
# Lapras -- Aqua Wash
# ----------------------------------------------------------------------

def aqua_wash(count=2):
    """You may put 2 Energy attached to your opponent's Active Pokemon into
    their hand."""
    async def effect(ctx):
        if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
            await ctx.deal_damage()
        defender = ctx.opponent_active()
        if defender is None or ctx.effects_blocked(defender):
            return
        attached = ctx.attached_energies(defender)
        if not attached:
            return
        picks = await ctx.choose_cards(
            attached, count, minimum=0,
            prompt="Choose up to %d Energy cards to put into your opponent's hand"
                   % count)
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    return effect


# ----------------------------------------------------------------------
# Latias -- Dyna Barrier / Red Assist
# ----------------------------------------------------------------------

def dyna_barrier():
    """During your opponent's next turn, prevent all damage done to this
    Pokemon by attacks from Pokemon V."""
    def attacker_is_v(calc, carrier):
        return is_pokemon_v_predicate(calc.attacker)

    async def effect(ctx):
        await ctx.deal_damage()
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, prevent_damage_when(attacker_is_v))
    return effect


def red_assist():
    """Once during your turn, attach a Psychic Energy card from your hand to
    1 of your Latios."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_energy_card(c)
                and energy_provides(c, PokemonTypes.PSYCHIC)]
        if not pool:
            return
        candidates = [p for p in ctx.my_pokemon_in_play()
                      if _pokemon_named(p, "Latios")]
        if not candidates:
            return
        pick = await ctx.choose_cards(
            pool, 1, prompt="Choose a Psychic Energy card to attach")
        if not pick:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose 1 of your Latios")
        if target is None:
            return
        await ctx.attach_energy(pick[0], target)
    return effect


def _pokemon_named(pokemon, name: str) -> bool:
    definition = def_for(getattr(pokemon, "archetype_id", None) or "")
    return getattr(definition, "display_name", None) == name


# ----------------------------------------------------------------------
# Leafeon -- Leaf Guard / Grass Knot / Slashing Strike /
# Leafeon VSTAR -- Ivy Star
# ----------------------------------------------------------------------

def leaf_guard(reduce=30):
    from spirit.game.card_effects.passives_common import protect_next_turn
    return protect_next_turn(reduce=reduce)


def grass_knot(per=30):
    """30 more for each Colorless in your opponent's Active Pokemon's Retreat
    Cost."""
    return vise_bite(per)


def slashing_strike():
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.session.turn_state.lock_attack(
            ctx.attacker.entity_id,
            ctx.ability.ability_id,
        )
    return effect


def ivy_star():
    """[VSTAR Power] Switch 1 of your opponent's Benched Pokemon with their
    Active Pokemon."""
    from spirit.game.card_effects.support_common import gust_attack
    return gust_attack()


# ----------------------------------------------------------------------
# Light Toxtricity -- Slow Ballad / Beatdown Smash
# ----------------------------------------------------------------------

def slow_ballad(heal=30):
    """Heal 30 damage from both Active Pokemon."""
    async def effect(ctx):
        if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
            await ctx.deal_damage()
        for pokemon in (ctx.my_active(), ctx.opponent_active()):
            if pokemon is not None:
                await ctx.heal(heal, pokemon)
    return effect


def beatdown_smash():
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.session.turn_state.lock_attack(
            ctx.attacker.entity_id,
            ctx.ability.ability_id,
        )
    return effect


# ----------------------------------------------------------------------
# Lucario -- Aura Sphere Volley / Roaring Resolve /
# Lucario V -- Crushing Punch / Lucario VSTAR -- Fighting Knuckle / Aura Star
# ----------------------------------------------------------------------

def aura_sphere_volley(per=60):
    """Discard all Fighting Energy from this Pokemon. This attack does 60
    more damage for each card you discarded this way."""
    from spirit.game.card_effects.attacks_common import discard_for_bonus

    def is_fighting(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.FIGHTING)

    return discard_for_bonus(source="self-energy", predicate=is_fighting,
                             max_count=99, per=per, optional=False)


def roaring_resolve(counters=2):
    """Once during your turn, put 2 damage counters on this Pokemon. If you
    do, search your deck for a Fighting Energy card and attach it to this
    Pokemon."""
    def is_fighting(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.FIGHTING)

    async def effect(ctx):
        await ctx.deal_damage(counters * 10, target=ctx.source, as_counters=True)
        await search_attach_energy(
            predicate=is_fighting, count=1, to_self=True,
            prompt="Choose a Fighting Energy card to attach")(ctx)
    return effect


def crushing_punch():
    """Discard a Special Energy from your opponent's Active Pokemon."""
    from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack

    def is_special(card):
        definition = def_for(getattr(card, "archetype_id", None) or "")
        return bool(getattr(definition, "is_special_energy", False))

    return discard_opponent_energy_attack(1, special_only=True)


def fighting_knuckle(bonus=120):
    from spirit.game.card_effects.attacks_common import bonus_if, defender_is_v
    return bonus_if(defender_is_v, bonus)


def aura_star(per=70):
    """70x for each Energy attached to all of your opponent's Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_per
    return damage_per(count_energy("opponent"), per)


# ----------------------------------------------------------------------
# Lugia -- Wind Pressure / Lugia V -- Read the Wind / Aero Dive
# ----------------------------------------------------------------------

def wind_pressure():
    """If your opponent has 5 or fewer cards in their hand, this attack does
    nothing."""
    from spirit.game.card_effects.attacks_common import bonus_if

    def opponent_has_more_than_five(ctx):
        return count_hand("opponent")(ctx) > 5

    return bonus_if(opponent_has_more_than_five, 0, else_nothing=True)


# ----------------------------------------------------------------------
# Lumineon V -- Luminous Sign (reuse pokemon.luminous_sign)
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Luxray -- Raid
# ----------------------------------------------------------------------

def raid(bonus=100):
    """If this Pokemon evolved from Luxio during this turn, this attack does
    100 more damage."""
    from spirit.game.card_effects.attacks_common import bonus_if

    def evolved_this_turn(ctx):
        state = ctx.session.turn_state
        evolved = state.evolved_entities if hasattr(state, "evolved_entities") else set()
        return ctx.attacker.entity_id in evolved

    return bonus_if(evolved_this_turn, bonus)


# ----------------------------------------------------------------------
# Lycanroc V -- Crashing Fangs
# ----------------------------------------------------------------------

def crashing_fangs():
    async def effect(ctx):
        await ctx.deal_damage()
        lock_all_attacks(ctx, ctx.attacker)
    return effect


# ----------------------------------------------------------------------
# Machamp -- Strong-Arm Lariat / Crisis Muscles / Macho Revenge / Dynamite Punch
# ----------------------------------------------------------------------

def strong_arm_lariat(bonus=100):
    """You may do 100 more damage. If you do, during your next turn, this
    Pokemon can't attack."""
    async def effect(ctx):
        base = getattr(ctx.ability, "damage", 0) or 0
        if await ctx.ask_yes_no("Do 100 more damage? (This Pokemon can't attack next turn)"):
            await ctx.deal_damage(base + bonus)
            lock_all_attacks(ctx, ctx.attacker)
        else:
            await ctx.deal_damage(base)
    return effect


def crisis_muscles(hp_bonus=150, prizes_threshold=3):
    """If your opponent has 3 or fewer Prize cards remaining, this Pokemon
    gets +150 HP."""
    from spirit.game.card_effects.passives_common import hp_bonus_tool

    def opponent_low_on_prizes(pokemon):
        carrier = pokemon
        board = _board_of(carrier)
        if board is None:
            return False
        opponent_id = next((p for p in board.player_ids
                            if p != carrier.owning_player_id), None)
        if opponent_id is None:
            return False
        state = getattr(board, "turn_state", None)
        if state is None:
            return False
        remaining = 6 - int(state.prizes_taken.get(opponent_id, 0))
        return remaining <= prizes_threshold

    return hp_bonus_tool(hp_bonus, holder_pred=opponent_low_on_prizes)


def macho_revenge(per=20):
    """20x for each Fighting Pokemon in your discard pile."""
    from spirit.game.card_effects.attacks_common import damage_per, count_discard

    def fighting_in_discard(ctx):
        return count_discard("mine", _is_fighting_pokemon_card)(ctx)

    return damage_per(fighting_in_discard, per)


def _is_fighting_pokemon_card(card):
    if not _is_pokemon_card(card):
        return False
    return PokemonTypes.FIGHTING.value in _pokemon_types(card)


def dynamite_punch(self_damage=50):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_damage)


# ----------------------------------------------------------------------
# Magnezone -- Giga Magnet
# ----------------------------------------------------------------------

def giga_magnet(look=6):
    """Once during your turn, look at the top 6 cards of your deck and attach
    any number of Metal Energy cards you find there to your Pokemon in any
    way you like. Shuffle the other cards back into your deck."""
    def is_metal(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.METAL)

    from spirit.game.card_effects.support_common import look_top_attach_energy
    return look_top_attach_energy(look, predicate=is_metal, rest="shuffle")


# ----------------------------------------------------------------------
# Manaphy -- Pulling Currents / Aqua Bullet
# ----------------------------------------------------------------------

def pulling_currents():
    """Your opponent reveals their hand. Put up to 2 Basic Pokemon you find
    there onto your opponent's Bench."""
    from spirit.game.session.effects import is_basic_pokemon

    async def effect(ctx):
        if ctx.is_attack_effect() and getattr(ctx.ability, "damage", 0) > 0:
            await ctx.deal_damage()
        hand = list(ctx.hand(ctx.opponent_id))
        await ctx.reveal_cards(hand, to_player=ctx.player_id)
        basics = [c for c in hand if is_basic_pokemon(c)]
        if not basics:
            return
        picks = await ctx.choose_cards(
            basics, 2, minimum=0,
            prompt="Choose up to 2 Basic Pokemon to put onto your opponent's Bench")
        for card in picks:
            await ctx.bench_pokemon(card)
    return effect


def aqua_bullet(bench_damage=20):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(bench_damage, pool="bench", also_base=True)


# ----------------------------------------------------------------------
# Mantine -- Water Reserve
# ----------------------------------------------------------------------

def water_reserve():
    """Search your deck for up to 3 Water Energy cards, reveal them, and put
    them into your hand."""
    def is_water(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.WATER)

    return search_to_hand(predicate=is_water, count=3, reveal=True,
                          prompt="Choose up to 3 Water Energy cards")


# ----------------------------------------------------------------------
# Melmetal V -- Arm Charge
# ----------------------------------------------------------------------

def arm_charge():
    """You may attach a Metal Energy card from your hand to this Pokemon."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_energy_card(c)
                and energy_provides(c, PokemonTypes.METAL)]
        if not pool:
            return
        pick = await ctx.choose_cards(
            pool, 1, prompt="Choose a Metal Energy card to attach to this Pokemon")
        if pick:
            await ctx.attach_energy(pick[0], ctx.source)
    return effect


# ----------------------------------------------------------------------
# Meowth V / VMAX -- Pay Day / G-Max Gold Rush
# ----------------------------------------------------------------------

def pay_day():
    return draw_attack(1)


def g_max_gold_rush():
    return draw_attack(3)


# ----------------------------------------------------------------------
# Mewtwo V -- Transfer Break
# ----------------------------------------------------------------------

def transfer_break():
    """Move an Energy from this Pokemon to 1 of your Benched Pokemon."""
    return swirling_slice()


# ----------------------------------------------------------------------
# Mimikyu -- Filch / Wet Claw
# ----------------------------------------------------------------------

def filch(count=2):
    return draw_attack(count)


def wet_claw(count=1):
    """Put an Energy attached to your opponent's Active Pokemon into their
    hand."""
    return aqua_wash(count)


# ----------------------------------------------------------------------
# Moltres -- Inferno Wings
# ----------------------------------------------------------------------

def inferno_wings(bonus=70):
    """If this Pokemon has any damage counters on it, this attack does 70 more
    damage. This attack's damage isn't affected by Weakness."""
    from spirit.game.card_effects.attacks_common import bonus_if, has_damage

    async def effect(ctx):
        base = getattr(ctx.ability, "damage", 0) or 0
        amount = base + (bonus if has_damage("self")(ctx) else 0)
        if amount > 0:
            await ctx.deal_damage(amount, ignore_weakness=True)
    return effect


# ----------------------------------------------------------------------
# Morpeko -- Famished / Thunder Shock / Morpeko V -- Spark / Electro Wheel
# ----------------------------------------------------------------------

def famished():
    return draw_attack(1)


def thunder_shock():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.PARALYZED, flip=True)


def spark(bench_damage=20):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(bench_damage, pool="bench", also_base=True)


def electro_wheel():
    """Discard an Energy from this Pokemon. If you do, switch it with 1 of
    your Benched Pokemon."""
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    from spirit.game.card_effects.support_common import switch_self_attack

    async def effect(ctx):
        await ctx.deal_damage()
        attached = ctx.attached_energies(ctx.attacker)
        if not attached:
            return
        pick = await ctx.choose_cards(
            attached, 1, prompt="Choose an Energy card to discard from this Pokemon")
        if not pick:
            return
        await ctx.discard_cards(pick)
        bench = ctx.my_bench()
        if bench:
            target = await ctx.choose_pokemon(
                bench, "Choose 1 of your Benched Pokemon to switch with")
            if target is not None:
                await ctx.switch_active(ctx.player_id, target)
    return effect


# ----------------------------------------------------------------------
# Morpeko V-UNION -- Union Gain / All You Can Eat / Burst Wheel
# ----------------------------------------------------------------------

def union_gain(energy_type, count=2):
    """Attach up to 2 <type> Energy cards from your discard pile to this
    Pokemon."""
    def is_typed(card):
        return is_energy_card(card) and energy_provides(card, energy_type)

    return attach_from_discard(predicate=is_typed, count=count, target="self",
                               prompt="Choose up to %d Energy cards to attach" % count)


def all_you_can_eat(hand_size=10):
    return draw_until_effect(hand_size)


def burst_wheel(per=100):
    """Discard all Energy from this Pokemon. This attack does 100 damage for
    each card you discarded in this way."""
    from spirit.game.card_effects.attacks_common import discard_for_bonus
    return discard_for_bonus(source="self-energy", max_count=99, per=per,
                             optional=False)


# ----------------------------------------------------------------------
# Noctowl -- Carry Off
# ----------------------------------------------------------------------

def carry_off():
    """Choose 1 of your opponent's Benched Pokemon. They shuffle that Pokemon
    and all attached cards into their deck. Then, shuffle this Pokemon and
    all attached cards into your deck."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokemon")
        if target is None:
            return
        from spirit.game.session.effects import full_stack
        await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)
        await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)
        if ctx.attacker is ctx.my_active():
            async def _promote():
                if not await ctx.session._promote_new_active(ctx.player_id):
                    screen_name = ctx.session.players[ctx.player_id].screen_name
                    await ctx.session.end_game(
                        ctx.opponent_id, f"{screen_name} has no Pokemon left")
            ctx.deferred_actions.append(_promote)
    return effect


# ----------------------------------------------------------------------
# Noivern V -- Boomburst / Synchro Loud
# ----------------------------------------------------------------------

def boomburst(amount=20):
    """This attack does 20 damage to each of your opponent's Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_all_opponents
    return damage_all_opponents(amount)


def synchro_loud(bonus=120):
    """If you have the same number of cards in your hand as your opponent,
    this attack does 120 more damage."""
    from spirit.game.card_effects.attacks_common import bonus_if

    def same_hand_size(ctx):
        return count_hand("mine")(ctx) == count_hand("opponent")(ctx)

    return bonus_if(same_hand_size, bonus)


# ----------------------------------------------------------------------
# Octillery -- Rapid Strike Search
# ----------------------------------------------------------------------

def rapid_strike_search():
    """Once during your turn, search your deck for a Rapid Strike card, reveal
    it, and put it into your hand."""
    def is_rapid_strike(card):
        return "Rapid Strike" in subtypes_for(
            getattr(card, "archetype_id", None) or "")

    return search_to_hand(predicate=is_rapid_strike, count=1, reveal=True,
                          prompt="Choose a Rapid Strike card to put into your hand")


# ----------------------------------------------------------------------
# Orbeetle V -- Strafe / Mysterious Wave
# ----------------------------------------------------------------------

def strafe():
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack(optional=True)


def mysterious_wave(per=30):
    return psychic(per)


# ----------------------------------------------------------------------
# Oricorio -- Glistening Droplets (reuse pokemon.glistening_droplets) /
# Lesson in Zeal / Mixed Call
# ----------------------------------------------------------------------

def lesson_in_zeal(reduce=20):
    """All of your Fusion Strike Pokemon take 20 less damage from attacks from
    your opponent's Pokemon. You can't apply more than 1 Lesson in Zeal
    Ability at a time."""
    def attacker_pred(attacker):
        return True

    def target_pred(target, carrier):
        return "Fusion Strike" in subtypes_for(
            getattr(target, "archetype_id", None) or "")

    return takes_less_passive(reduce, protects=target_pred,
                              stack_key="lesson_in_zeal")


def mixed_call():
    """Search your deck for a Pokemon and a Supporter card, reveal them, and
    put them into your hand."""
    from spirit.game.session.effects import is_supporter_card

    async def effect(ctx):
        def is_pokemon(card):
            return _is_pokemon_card(card)

        picks = await ctx.search_deck_groups([
            (is_pokemon, 1, "Choose a Pokemon"),
            (is_supporter_card, 1, "Choose a Supporter card"),
        ], prompt="Choose a Pokemon and a Supporter card")
        flat = [c for group in picks for c in group]
        if flat:
            await ctx.put_in_hand(flat, reveal=True)
        await ctx.shuffle_deck()
    return effect


# ----------------------------------------------------------------------
# Origin Forme Dialga V -- Metal Coating /
# Origin Forme Dialga VSTAR -- Metal Blast / Star Chronos
# ----------------------------------------------------------------------

def metal_coating(count=2):
    """Attach up to 2 Metal Energy cards from your discard pile to this
    Pokemon."""
    def is_metal(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.METAL)

    return attach_from_discard(predicate=is_metal, count=count, target="self",
                               prompt="Choose up to 2 Metal Energy cards to attach")


def metal_blast(per=40):
    """40 more for each Metal Energy attached to this Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_per
    return damage_per(count_energy("self", PokemonTypes.METAL), per)


# ----------------------------------------------------------------------
# Origin Forme Palkia V -- Rule the Region / Hydro Break /
# Origin Forme Palkia VSTAR -- Subspace Swell / Star Portal
# ----------------------------------------------------------------------

def rule_the_region():
    """Search your deck for a Stadium card, reveal it, and put it into your
    hand."""
    from spirit.game.attributes import TrainerType

    def is_stadium(card):
        definition = def_for(getattr(card, "archetype_id", None) or "")
        return getattr(definition, "trainer_type", None) == TrainerType.STADIUM

    return search_to_hand(predicate=is_stadium, count=1, reveal=True,
                          prompt="Choose a Stadium card to put into your hand")


def hydro_break():
    async def effect(ctx):
        await ctx.deal_damage()
        lock_all_attacks(ctx, ctx.attacker)
    return effect


def subspace_swell(per=20):
    """20 more for each Benched Pokemon (both yours and your opponent's)."""
    from spirit.game.card_effects.attacks_common import damage_per

    def all_bench(ctx):
        return count_bench("both")(ctx)

    return damage_per(all_bench, per)


def star_portal(count=3):
    """[VSTAR Power] Attach up to 3 Water Energy cards from your discard pile
    to your Water Pokemon in any way you like."""
    def is_water(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.WATER)

    return attach_from_discard(
        predicate=is_water, count=count, target=is_type(PokemonTypes.WATER),
        prompt="Choose up to 3 Water Energy cards to attach to your Water Pokemon")


# ----------------------------------------------------------------------
# Passimian -- Fling / Throwing Coach
# ----------------------------------------------------------------------

def fling(amount=20):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(amount, pool="any")


def throwing_coach(amount=30):
    """Your Rapid Strike Pokemon's attacks do 30 more damage to your
    opponent's Benched Pokemon. You can't apply more than 1 Throwing Coach
    Ability at a time."""
    class ThrowingCoachPassive(Passive):
        def modify_damage_dealt(self, calc, carrier):
            if not (calc.is_attack and calc.is_opposing):
                return
            attacker = calc.attacker
            if attacker is None or carrier_pokemon(carrier) is not attacker:
                return
            if "Rapid Strike" not in subtypes_for(
                    getattr(attacker, "archetype_id", None) or ""):
                return
            if calc.target is None:
                return
            if calc.target is calc.board.active_pokemon(
                    calc.target.owning_player_id):
                return
            if "throwing_coach" in calc.applied_once:
                return
            calc.applied_once.add("throwing_coach")
            calc.amount += amount
    return ThrowingCoachPassive()


# ----------------------------------------------------------------------
# Phanpy -- Strike Back
# ----------------------------------------------------------------------

def strike_back(per=30):
    """30x for each damage counter on this Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_per
    return damage_per(damage_counters_on("self"), per)


# ----------------------------------------------------------------------
# Pikachu -- Iron Tail / Gift Delivery / Tail Whip /
# Pikachu V -- Volt Tackle / Lightning Blast / Pika Drive / Charge /
# Thunderbolt / Circle Circuit / Pikachu VMAX -- G-Max Volt Tackle / Tail Charge
# ----------------------------------------------------------------------

def iron_tail(per=30):
    """Flip a coin until you get tails. This attack does 30 damage for each
    heads."""
    return meteor_punch(per)


def gift_delivery():
    """Flip a coin. If heads, search your deck for an Item card, reveal it,
    and put it into your hand."""
    from spirit.game.attributes import TrainerType
    from spirit.game.card_effects.attacks_common import flip_or_nothing

    def is_item(card):
        definition = def_for(getattr(card, "archetype_id", None) or "")
        return getattr(definition, "trainer_type", None) == TrainerType.ITEM

    async def _search(ctx):
        await search_to_hand(
            predicate=is_item, count=1, reveal=True,
            prompt="Choose an Item card to put into your hand")(ctx)

    return flip_or_nothing(then=_search)


def tail_whip():
    """Flip a coin. If heads, the Defending Pokemon can't attack during your
    opponent's next turn."""
    from spirit.game.card_effects.attacks_common import (
        flip_or_nothing, lock_defender_attacks)

    async def _lock(ctx):
        lock_defender_attacks(ctx)

    return flip_or_nothing(then=_lock)


def volt_tackle(self_damage=30):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_damage)


def lightning_blast(bonus=120):
    """You may discard all Lightning Energy from this Pokemon. If you do, this
    attack does 120 more damage."""
    async def effect(ctx):
        base = getattr(ctx.ability, "damage", 0) or 0
        attached = ctx.attached_energies(ctx.attacker)
        lightning = [e for e in attached
                     if energy_provides(e, PokemonTypes.LIGHTNING)]
        if lightning and await ctx.ask_yes_no(
                "Discard all Lightning Energy to do %d more damage?" % bonus):
            await ctx.discard_cards(lightning)
            await ctx.deal_damage(base + bonus)
        else:
            await ctx.deal_damage(base)
    return effect


def pika_drive():
    async def effect(ctx):
        await ctx.deal_damage()
        lock_all_attacks(ctx, ctx.attacker)
    return effect


def charge():
    def is_lightning(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.LIGHTNING)

    return search_attach_energy(predicate=is_lightning, count=2, to_self=True,
                                prompt="Choose up to 2 Lightning Energy cards to attach")


def thunderbolt():
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(all_energy=True)


def circle_circuit(per=30):
    """30x for each of your Benched Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_per
    return damage_per(count_bench("mine"), per)


def g_max_volt_tackle(bonus=150):
    """You may discard all Energy from this Pokemon. If you do, this attack
    does 150 more damage."""
    async def effect(ctx):
        base = getattr(ctx.ability, "damage", 0) or 0
        attached = ctx.attached_energies(ctx.attacker)
        if attached and await ctx.ask_yes_no(
                "Discard all Energy to do %d more damage?" % bonus):
            await ctx.discard_cards(attached)
            await ctx.deal_damage(base + bonus)
        else:
            await ctx.deal_damage(base)
    return effect


def tail_charge(count=3):
    """Attach up to 3 Lightning Energy cards from your discard pile to 1 of
    your Pokemon."""
    def is_lightning(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.LIGHTNING)

    return attach_from_discard(predicate=is_lightning, count=count,
                               target="choice",
                               prompt="Choose up to 3 Lightning Energy cards to attach")


# ----------------------------------------------------------------------
# Pikachu V-UNION -- Shocking Shock / Disconnect
# ----------------------------------------------------------------------

def shocking_shock():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.PARALYZED, flip=True)


def disconnect():
    """During your opponent's next turn, they can't play any Item cards from
    their hand."""
    from spirit.game.attributes import TrainerType

    async def effect(ctx):
        await ctx.deal_damage()
        opponent = ctx.opponent_id

        def is_item(card):
            definition = def_for(getattr(card, "archetype_id", None) or "")
            return getattr(definition, "trainer_type", None) == TrainerType.ITEM

        state = ctx.session.turn_state
        for entry in state.play_locks.setdefault(opponent, []):
            pass
        ctx.lock_plays(opponent, is_item,
                       through_turn=state.turn_number + 1)
    return effect


# ----------------------------------------------------------------------
# Polteageist V -- Mind Bend / Teapot of Surprises
# ----------------------------------------------------------------------

def mind_bend():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.CONFUSED)


async def teapot_of_surprises(ctx):
    """[ON_DAMAGED_BY_ATTACK] If this Pokemon is in the Active Spot and is
    damaged by an attack from your opponent's Pokemon (even if it is Knocked
    Out), choose a random card from your opponent's hand. Your opponent
    reveals that card and puts it on the bottom of their deck."""
    import random
    if not is_in_active_spot(ctx.source):
        return
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    card = random.choice(hand)
    await ctx.reveal_cards([card], to_player=ctx.player_id)
    await ctx.put_on_bottom_of_deck(card)


# ----------------------------------------------------------------------
# Pyukumuku -- Pitch a Pyukumuku
# ----------------------------------------------------------------------

def pitch_a_pyukumuku():
    """Once during your turn, if this Pokemon is in your hand, reveal it and
    put it on the bottom of your deck. If you do, draw a card."""
    async def effect(ctx):
        await ctx.reveal_cards([ctx.source], to_player=ctx.opponent_id)
        await ctx.put_on_bottom_of_deck(ctx.source)
        await ctx.draw_cards(1)
    return effect


# ----------------------------------------------------------------------
# Radiant Eevee -- Twinkle Gathering
# ----------------------------------------------------------------------

def twinkle_gathering():
    """Search your deck for a number of cards up to the number of different
    types of Pokemon you have in play and put them into your hand."""
    async def effect(ctx):
        types_seen = set()
        for p in ctx.my_pokemon_in_play():
            types_seen.update(_pokemon_types(p))
        count = len(types_seen)
        if count <= 0:
            return
        await search_to_hand(
            count=count, reveal=False,
            prompt="Choose up to %d cards to put into your hand" % count)(ctx)
    return effect


# ----------------------------------------------------------------------
# Rapidash -- Heat Boost
# ----------------------------------------------------------------------

def heat_boost(amount=30):
    """Once during your turn, discard a Fire Energy card from your hand to
    use this Ability. During this turn, your Fire Pokemon's attacks do 30
    more damage to your opponent's Active Pokemon."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_energy_card(c)
                and energy_provides(c, PokemonTypes.FIRE)]
        if not pool:
            return
        pick = await ctx.choose_cards(
            pool, 1, minimum=1,
            prompt="Choose a Fire Energy card to discard")
        if not pick:
            return
        await ctx.discard_cards(pick)
        ctx.add_turn_damage_modifier(_FireBoost(amount, ctx.player_id))
    return effect


class _FireBoost:
    """Turn-scoped +N for the player's Fire Pokemon vs the opponent's Active
    (Heat Boost)."""

    def __init__(self, amount, player_id):
        self.amount = amount
        self.player_id = player_id
        self.requires_subtype = None
        self.opposing_active_only = True
        self.expires_after_turn = None
        self.source_entity_id = None
        self.attack_title = None

        def source_predicate(attacker):
            return PokemonTypes.FIRE.value in \
                list(attacker.get_attribute(AttrID.POKEMON_TYPES) or [])
        self.source_predicate = source_predicate


# ----------------------------------------------------------------------
# Rapid Strike Urshifu V -- Sonic Legs
# ----------------------------------------------------------------------

def sonic_legs(bench_damage=20, count=2):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(bench_damage, pool="bench", count=count, also_base=True)


# ----------------------------------------------------------------------
# Rayquaza -- Jaw Lock / Power Blast / Rayquaza V -- Dragon Pulse / Spiral Burst
# ----------------------------------------------------------------------

def power_blast():
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=1)


def dragon_pulse(count=2):
    """Discard the top 2 cards of your deck."""
    from spirit.game.card_effects.attacks_common import mill_attack
    return mill_attack(count, opponent=False)


def spiral_burst(per=80, max_count=2):
    """You may discard up to 2 basic Fire Energy or up to 2 basic Lightning
    Energy from this Pokemon. This attack does 80 more damage for each card
    you discarded this way."""
    from spirit.game.card_effects.attacks_common import discard_for_bonus

    def is_fire_or_lightning(card):
        if not is_energy_card(card):
            return False
        return (energy_provides(card, PokemonTypes.FIRE)
                or energy_provides(card, PokemonTypes.LIGHTNING))

    return discard_for_bonus(source="self-energy",
                             predicate=is_fire_or_lightning,
                             max_count=max_count, per=per)


# ----------------------------------------------------------------------
# Regidrago V -- Celestial Roar / Dragon Laser
# ----------------------------------------------------------------------

def celestial_roar(count=3):
    """Discard the top 3 cards of your deck. If any of those cards are Energy
    cards, attach them to this Pokemon."""
    from spirit.game.card_effects.attacks_common import mill_attack

    async def effect(ctx):
        top = ctx.deck_top(count)
        if top:
            await ctx.discard_cards(top)
        energies = [c for c in top if is_energy_card(c)]
        for card in energies:
            await ctx.attach_energy(card, ctx.attacker)
    return effect


def dragon_laser(bench_damage=30):
    from spirit.game.card_effects.attacks_common import snipe_attack
    return snipe_attack(bench_damage, pool="bench", also_base=True)


# ----------------------------------------------------------------------
# Regieleki V -- Switching Bolt / Lightning Wall
# ----------------------------------------------------------------------

def switching_bolt():
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack()


def lightning_wall(reduce=100):
    from spirit.game.card_effects.passives_common import protect_next_turn
    return protect_next_turn(reduce=reduce)


# ----------------------------------------------------------------------
# Regigigas -- Limber Up / Double Impact
# ----------------------------------------------------------------------

def limber_up():
    """Attach a basic Energy card from your discard pile to this Pokemon."""
    return attach_from_discard(predicate=is_basic_energy_card, count=1,
                               target="self",
                               prompt="Choose a basic Energy card to attach")


def double_impact(per=120, coins=2):
    from spirit.game.card_effects.attacks_common import flip_damage
    return flip_damage(coins=coins, per_heads=per)


# ----------------------------------------------------------------------
# Rillaboom -- Wood Drain / Raging Repeated Strike /
# Rillaboom (swsh1promo) -- Voltage Beat / Rillaboom V -- Forest Feast /
# Wood Hammer
# ----------------------------------------------------------------------

def wood_drain(heal=30):
    from spirit.game.card_effects.support_common import heal_attack
    return heal_attack(amount=heal)


def raging_repeated_strike(per=30):
    """Discard any amount of Energy from your Pokemon. This attack does 30
    more damage for each card you discarded this way."""
    from spirit.game.card_effects.attacks_common import discard_for_bonus
    return discard_for_bonus(source="self-energy", max_count=99, per=per)


def voltage_beat():
    """Once during your turn, search your deck for up to 2 Grass Energy cards
    and attach them to 1 of your Pokemon."""
    def is_grass(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.GRASS)

    return search_attach_energy(
        predicate=is_grass, count=2, distribute=False,
        prompt="Choose up to 2 Grass Energy cards to attach to 1 of your Pokemon")


def forest_feast():
    """Search your deck for up to 2 Basic Grass Pokemon and put them onto your
    Bench."""
    def is_basic_grass(card):
        if not is_basic_pokemon_card(card):
            return False
        return PokemonTypes.GRASS.value in _pokemon_types(card)

    return search_to_bench(predicate=is_basic_grass, count=2,
                           prompt="Choose up to 2 Basic Grass Pokemon to put onto your Bench")


def is_basic_pokemon_card(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return "Basic" in subtypes_for(getattr(card, "archetype_id", None) or "") and \
        _is_pokemon_card(card)


def wood_hammer(self_damage=30):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_damage)


# ----------------------------------------------------------------------
# Rotom V -- Lost Hack / Extreme Current
# ----------------------------------------------------------------------

def lost_hack():
    """Put a Special Energy attached to 1 of your opponent's Pokemon in the
    Lost Zone."""
    async def effect(ctx):
        def is_special(card):
            definition = def_for(getattr(card, "archetype_id", None) or "")
            return bool(getattr(definition, "is_special_energy", False))

        holders = [p for p in ctx.opponent_pokemon_in_play()
                   if any(is_special(c) for c in ctx.attached_energies(p))]
        if not holders:
            return
        holder = await ctx.choose_pokemon(
            holders, "Choose 1 of your opponent's Pokemon with Special Energy")
        if holder is None:
            return
        specials = [c for c in ctx.attached_energies(holder) if is_special(c)]
        pick = await ctx.choose_cards(
            specials, 1, prompt="Choose a Special Energy card to put in the Lost Zone")
        if pick:
            await ctx.move_to_lost_zone(pick)
    return effect


def extreme_current():
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=1)


# ----------------------------------------------------------------------
# Rowlet -- Jump On / Scorbunny -- Super Singe / Flaring Dash / Me First
# ----------------------------------------------------------------------

def jump_on(bonus=10):
    from spirit.game.card_effects.attacks_common import flip_bonus
    return flip_bonus(bonus)


def super_singe():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.BURNED, flip=True)


def flaring_dash():
    """Flip a coin until you get tails. For each heads, draw a card."""
    async def effect(ctx):
        heads = await ctx.flip_until_tails(
            ctx.ability.title if ctx.ability else "")
        if heads > 0:
            await ctx.draw_cards(heads)
    return effect


def me_first():
    return draw_attack(1)


# ----------------------------------------------------------------------
# Shadow Rider Calyrex V -- Cloak in Shadows / Hollow Binding
# ----------------------------------------------------------------------

def cloak_in_shadows():
    """Attach a Psychic Energy card from your discard pile to this Pokemon."""
    def is_psychic(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.PSYCHIC)

    return attach_from_discard(predicate=is_psychic, count=1, target="self",
                               prompt="Choose a Psychic Energy card to attach")


def hollow_binding():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(no_retreat=True)


# ----------------------------------------------------------------------
# Single Strike Urshifu V -- Brawny Knuckle
# ----------------------------------------------------------------------

def brawny_knuckle():
    """This attack's damage isn't affected by Resistance."""
    return buster_swing()


# ----------------------------------------------------------------------
# Snorlax -- Single Strike Tackle / Body Slam / Gormandize
# ----------------------------------------------------------------------

def single_strike_tackle(self_damage=30):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_damage)


def body_slam():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.PARALYZED, flip=True)


def gormandize(hand_size=7):
    """Once during your turn, if this Pokemon is in the Active Spot, you may
    draw cards until you have 7 cards in your hand. If you use this Ability,
    your turn ends."""
    async def effect(ctx):
        if ctx.source is not ctx.my_active():
            return
        await ctx.draw_until(hand_size)
    return effect


# ----------------------------------------------------------------------
# Sobble -- Bind
# ----------------------------------------------------------------------

def bind():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.PARALYZED, flip=True)


# ----------------------------------------------------------------------
# Sunflora -- Bright Beam
# ----------------------------------------------------------------------

def bright_beam(per=70, max_count=3):
    """You may discard up to 3 Energy cards from your hand. This attack does
    70 more damage for each card you discarded this way."""
    from spirit.game.card_effects.attacks_common import discard_for_bonus
    return discard_for_bonus(source="hand", max_count=max_count, per=per)


# ----------------------------------------------------------------------
# Sylveon -- Time Out Kick / Symphony Whip / Sylveon V -- Dream Gift
# ----------------------------------------------------------------------

def time_out_kick(count=1):
    """You may put an Energy attached to your opponent's Active Pokemon into
    their hand."""
    return aqua_wash(count)


def symphony_whip(bonus=70):
    """If you played a Supporter card from your hand during this turn, this
    attack does 70 more damage."""
    from spirit.game.card_effects.attacks_common import bonus_if

    def played_supporter(ctx):
        return ctx.supporters_played_this_turn() > 0

    return bonus_if(played_supporter, bonus)


def dream_gift():
    """Once during your turn, search your deck for an Item card, reveal it,
    and put it into your hand. If you use this Ability, your turn ends."""
    from spirit.game.attributes import TrainerType

    def is_item(card):
        definition = def_for(getattr(card, "archetype_id", None) or "")
        return getattr(definition, "trainer_type", None) == TrainerType.ITEM

    return search_to_hand(predicate=is_item, count=1, reveal=True,
                          prompt="Choose an Item card to put into your hand")


# ----------------------------------------------------------------------
# Togetic -- Voice of Happiness
# ----------------------------------------------------------------------

def voice_of_happiness(heal=30):
    """When you play this Pokemon from your hand to evolve 1 of your Pokemon
    during your turn, heal 30 damage from your Active Pokemon."""
    async def effect(ctx):
        active = ctx.my_active()
        if active is None:
            return
        await ctx.heal(heal, active)
    return effect


# ----------------------------------------------------------------------
# Toxel -- Growl
# ----------------------------------------------------------------------

def growl(amount=20):
    """During your opponent's next turn, the Defending Pokemon's attacks do
    20 less damage (before applying Weakness and Resistance)."""
    from spirit.game.card_effects.passives_common import debuff_defender_attacks
    return debuff_defender_attacks(amount)


# ----------------------------------------------------------------------
# Toxtricity V -- Energize / Venom Slap
# ----------------------------------------------------------------------

def energize_lightning():
    return energize()


def venom_slap():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.POISONED)


# ----------------------------------------------------------------------
# Tyranitar V -- Cragalanche / Single Strike Crush
# ----------------------------------------------------------------------

def cragalanche(count=2):
    """Discard the top 2 cards of your opponent's deck."""
    from spirit.game.card_effects.attacks_common import mill_attack
    return mill_attack(count, opponent=True)


def single_strike_crush(count=4):
    """Discard the top 4 cards of your deck."""
    from spirit.game.card_effects.attacks_common import mill_attack
    return mill_attack(count, opponent=False)


# ----------------------------------------------------------------------
# Umbreon -- Blindside / Moon Mirage / Umbreon V -- Mean Look / Moonlight Blade
# ----------------------------------------------------------------------

def blindside(amount=60):
    """60 damage to 1 of your opponent's Pokemon that has any damage counters
    on it."""
    from spirit.game.card_effects.attacks_common import snipe_attack

    def has_counters(pokemon):
        return int(pokemon.get_attribute(AttrID.HP, 0) or 0) < _max_hp_of(pokemon)

    return snipe_attack(amount, pool="any", count=1)


def moon_mirage():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.CONFUSED)


def mean_look():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(no_retreat=True)


def moonlight_blade(bonus=80):
    from spirit.game.card_effects.attacks_common import bonus_if, has_damage
    return bonus_if(has_damage("self"), bonus)


# ----------------------------------------------------------------------
# Unown V -- Shady Stamp / Victory Symbol
# ----------------------------------------------------------------------

def shady_stamp():
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.CONFUSED)


def victory_symbol():
    """If you use this attack when you have only 1 Prize card remaining, you
    win this game."""
    async def effect(ctx):
        await ctx.deal_damage()
        remaining = 6 - ctx.prizes_taken(ctx.player_id)
        if remaining <= 1:
            await ctx.session.end_game(
                ctx.player_id, "Victory Symbol wins the game")
    return effect


# ----------------------------------------------------------------------
# Vaporeon -- Hydro Pump / Watery Shroud /
# Vaporeon V -- Triple Draw / Splash Jump /
# Vaporeon VMAX -- Bubble Pod / Max Torrent
# ----------------------------------------------------------------------

def hydro_pump(per=20):
    """20 more for each Water Energy attached to this Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_per
    return damage_per(count_energy("self", PokemonTypes.WATER), per)


def watery_shroud():
    """As long as this Pokemon is on your Bench, prevent all damage done to
    this Pokemon by attacks (both yours and your opponent's)."""
    def pred(calc, carrier):
        if not calc.is_attack:
            return False
        return carrier_pokemon(carrier) is calc.target
    return prevent_damage_when(pred, attacks_only=False)


def triple_draw():
    return draw_attack(3)


def splash_jump():
    from spirit.game.card_effects.support_common import switch_self_attack
    return switch_self_attack()


def bubble_pod():
    """Put a Water Pokemon from your discard pile onto your Bench. If you do,
    attach up to 3 Water Energy cards from your discard pile to that
    Pokemon."""
    def is_water_pokemon(card):
        return _is_pokemon_card(card) and \
            PokemonTypes.WATER.value in _pokemon_types(card)

    def is_water(card):
        return is_energy_card(card) and \
            energy_provides_type(card, PokemonTypes.WATER.value)

    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if is_water_pokemon(c)]
        if not pool:
            return
        pick = await ctx.choose_cards(
            pool, 1, minimum=1,
            prompt="Choose a Water Pokemon from your discard pile")
        if not pick:
            return
        if not await ctx.bench_pokemon(pick[0]):
            return
        await attach_from_discard(
            predicate=is_water, count=3, target=lambda p: p is pick[0],
            prompt="Choose up to 3 Water Energy cards to attach")(ctx)
    return effect


def max_torrent(bonus=100):
    from spirit.game.card_effects.attacks_common import bonus_if, has_damage
    return bonus_if(has_damage("defender"), bonus)


# ----------------------------------------------------------------------
# Venusaur V -- Leaf Drain / Double-Edge / Venusaur VMAX -- Forest Storm /
# G-Max Bloom
# ----------------------------------------------------------------------

def leaf_drain(heal=30):
    from spirit.game.card_effects.support_common import heal_attack
    return heal_attack(amount=heal)


def double_edge(self_damage=30):
    from spirit.game.card_effects.attacks_common import recoil_attack
    return recoil_attack(self_damage)


def forest_storm(per=30):
    """30x for each Grass Energy attached to all of your Pokemon."""
    from spirit.game.card_effects.attacks_common import damage_per
    return damage_per(count_energy("mine", PokemonTypes.GRASS), per)


def g_max_bloom(heal=30):
    from spirit.game.card_effects.support_common import heal_attack
    return heal_attack(amount=heal)


# ----------------------------------------------------------------------
# Victini V -- Spreading Flames / Energy Burst
# ----------------------------------------------------------------------

def spreading_flames(count=3):
    """Attach up to 3 Fire Energy cards from your discard pile to your Pokemon
    in any way you like."""
    def is_fire(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.FIRE)

    return attach_from_discard(
        predicate=is_fire, count=count, target="choice",
        prompt="Choose up to 3 Fire Energy cards to attach to your Pokemon")


def energy_burst(per=30):
    """30x for each Energy attached to both Active Pokemon."""
    return star_force(per)


# ----------------------------------------------------------------------
# Virizion V -- Emerald Blade / Verdant Wind
# ----------------------------------------------------------------------

def emerald_blade():
    async def effect(ctx):
        await ctx.deal_damage()
        lock_all_attacks(ctx, ctx.attacker)
    return effect


def verdant_wind():
    """Each of your Pokemon that has any Grass Energy attached recovers from
    all Special Conditions and can't be affected by any Special Conditions."""
    def has_grass(pokemon, carrier):
        board = _board_of(carrier)
        if board is None:
            return False
        # Attachments are the pokemon's children
        for child in getattr(pokemon, "children", []):
            if is_energy_card(child) and energy_provides(child, PokemonTypes.GRASS):
                return True
        return False

    from spirit.game.card_effects.passives_common import condition_immunity_passive
    return condition_immunity_passive(conditions=None, protects=has_grass)


# ----------------------------------------------------------------------
# Weavile -- Pursuit Claw
# ----------------------------------------------------------------------

def pursuit_claw(per=20):
    """20 damage to 1 of your opponent's Benched Pokemon for each damage
    counter on that Pokemon."""
    from spirit.game.card_effects.attacks_common import snipe_attack

    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokemon")
        if target is None:
            return
        counters = _damage_counters_on(target)
        amount = per * counters
        if amount > 0:
            await ctx.deal_damage(amount, target=target, apply_modifiers=None)
    return effect


def _damage_counters_on(pokemon) -> int:
    from spirit.game.session.passives import effective_max_hp
    board = _board_of(pokemon)
    if board is None:
        return 0
    current = int(pokemon.get_attribute(AttrID.HP, 0) or 0)
    return max(0, (effective_max_hp(board, pokemon) - current) // 10)


# ----------------------------------------------------------------------
# Wooloo -- Defense Curl
# ----------------------------------------------------------------------

def defense_curl():
    """Flip a coin. If heads, during your opponent's next turn, prevent all
    damage done to this Pokemon by attacks."""
    from spirit.game.card_effects.passives_common import flip_protection
    return flip_protection(prevent=True)


# ----------------------------------------------------------------------
# Wyrdeer -- Extrasensory / Hurried Gait
# ----------------------------------------------------------------------

def extrasensory(bonus=80):
    """If you have the same number of cards in your hand as your opponent,
    this attack does 80 more damage."""
    return synchro_loud(bonus)


def hurried_gait():
    return draw_attack(1)


# ----------------------------------------------------------------------
# Zacian -- Brave Blade / Bladed Armament / Crunch / Metal Blade
# ----------------------------------------------------------------------

def brave_blade():
    async def effect(ctx):
        await ctx.deal_damage()
        lock_all_attacks(ctx, ctx.attacker)
    return effect


def bladed_armament():
    """Damage from this Pokemon's attacks isn't affected by any effects on
    your opponent's Active Pokemon."""
    class BladedArmamentPassive(Passive):
        def modify_damage_dealt(self, calc, carrier):
            if not calc.is_attack:
                return
            if calc.attacker is None or \
                    carrier_pokemon(carrier) is not calc.attacker:
                return
            calc.ignore_target_effects = True
    return BladedArmamentPassive()


def crunch():
    """Flip a coin. If heads, discard an Energy from your opponent's Active
    Pokemon."""
    from spirit.game.card_effects.attacks_common import (
        flip_or_nothing, discard_opponent_energy_attack)

    async def _discard(ctx):
        defender = ctx.opponent_active()
        if defender is None or ctx.effects_blocked(defender):
            return
        await ctx.discard_energy_from(
            defender, 1,
            prompt="Choose an Energy to discard from the Defending Pokemon")

    return flip_or_nothing(then=_discard)


def metal_blade(count=3):
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=count)


# ----------------------------------------------------------------------
# Zacian V -- Intrepid Sword / Zacian V-UNION --
# Union Gain / Dance of the Crowned Sword / Master Blade
# ----------------------------------------------------------------------

def intrepid_sword(look=3):
    """Once during your turn, look at the top 3 cards of your deck and attach
    any number of Metal Energy cards you find there to this Pokemon. Put the
    other cards into your hand. If you use this Ability, your turn ends."""
    def is_metal(card):
        return is_energy_card(card) and energy_provides(card, PokemonTypes.METAL)

    from spirit.game.card_effects.support_common import look_top_attach_energy
    return look_top_attach_energy(look, predicate=is_metal, rest="hand")


def dance_of_the_crowned_sword(reduce=150):
    """During your opponent's next turn, the Defending Pokemon's attacks do
    150 less damage (before applying Weakness and Resistance)."""
    from spirit.game.card_effects.passives_common import debuff_defender_attacks
    return debuff_defender_attacks(reduce)


def master_blade(count=3):
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=count)


# ----------------------------------------------------------------------
# Zamazenta -- Sturdy Shield / Zamazenta V -- Assault Tackle / Dauntless Shield
# ----------------------------------------------------------------------

def sturdy_shield(reduce=20):
    return takes_less_passive(reduce)


def assault_tackle():
    """Discard a Special Energy from your opponent's Active Pokemon."""
    from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
    return discard_opponent_energy_attack(1, special_only=True)


def dauntless_shield():
    """Prevent all damage done to this Pokemon by attacks from your opponent's
    Pokemon VMAX."""
    def pred(calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        return is_pokemon_vmax_predicate(calc.attacker)
    return prevent_damage_when(pred)


# ----------------------------------------------------------------------
# Zeraora V -- Thunderous Bolt / Zeraora VMAX -- Reactive Pulse / Max Fist /
# Zeraora VSTAR -- Crushing Beat / Lightning Storm Star
# ----------------------------------------------------------------------

def thunderous_bolt():
    async def effect(ctx):
        await ctx.deal_damage()
        lock_all_attacks(ctx, ctx.attacker)
    return effect


def reactive_pulse(per=60):
    """60x for each of your opponent's Pokemon in play that has an Ability."""
    from spirit.game.card_effects.attacks_common import damage_per, count_in_play

    def has_ability(pokemon):
        definition = def_for(getattr(pokemon, "archetype_id", None) or "")
        return any(getattr(a, "effect", None) is not None
                   for a in getattr(definition, "abilities", []) or [])

    return damage_per(count_in_play("opponent", has_ability), per)


def max_fist(count=2):
    from spirit.game.card_effects.attacks_common import self_energy_discard_attack
    return self_energy_discard_attack(count=count)


def crushing_beat():
    """You may discard a Stadium in play."""
    from spirit.game.card_effects import pokemon as pokemon_effects
    return pokemon_effects.aero_dive


def lightning_storm_star(per=60, times=4):
    """[VSTAR Power] Choose 1 of your opponent's Pokemon 4 times. (You can
    choose the same Pokemon more than once.) For each time you chose a
    Pokemon, do 60 damage to it. This damage isn't affected by Weakness or
    Resistance."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        for _ in range(times):
            target = await ctx.choose_pokemon(
                candidates, "Choose 1 of your opponent's Pokemon (60 damage)")
            if target is None:
                return
            await ctx.deal_damage(per, target=target, apply_modifiers=False)
    return effect


def field_runner_passive():
    """If a Stadium is in play, this Pokemon has no Retreat Cost."""
    from spirit.game.card_effects.passives_common import retreat_free_when

    def stadium_in_play(pokemon, carrier):
        board = _board_of(pokemon)
        if board is None:
            return False
        area = board.find_global_area("activeStadium")
        return area is not None and bool(area.children)

    return retreat_free_when(stadium_in_play)


def feel_the_way():
    """Once during your turn, you may have your opponent reveal their hand."""
    async def effect(ctx):
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        await ctx.reveal_cards(hand, to_player=ctx.player_id)
    return effect


def in_active_spot_condition(board, player_id, pokemon):
    """Ability condition: this Pokemon is in the Active Spot."""
    return pokemon is board.active_pokemon(player_id)


def has_energy_in_play(energy_type=None):
    """Ability condition factory: any of my Pokemon has the given Energy
    attached (or any Energy when *energy_type* is None)."""
    type_value = getattr(energy_type, "value", energy_type)

    def condition(board, player_id, pokemon):
        for p in board.pokemon_in_play(player_id):
            for card in board.attached_energies(p):
                if type_value is None or energy_provides_type(card, type_value):
                    return True
        return False
    return condition


def crisis_power_passive(per=30):
    """This Pokemon's attacks do 30 more damage to your opponent's Active
    Pokemon for each Prize card your opponent has taken."""
    return _prize_scaled_boost(per, opponent=True)


def _board_of(entity):
    node = entity
    while node is not None:
        parent = getattr(node, "parent", None)
        if parent is None:
            break
        node = parent
    from spirit.game.models.board import BoardState
    return node if isinstance(node, BoardState) else None
