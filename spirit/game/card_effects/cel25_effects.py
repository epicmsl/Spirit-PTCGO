"""Scripted effects for the CEL25 (Celebrations 25th Anniversary) promos.

These are classic-era reprints (Base Set Poke-Powers, Team Rocket, LV.X
"Restore" cards, EX/GX hallmarks) mapped onto the SWSH client. The shared
factories cover the straightforward ones; this module holds the behaviors
that needed hand-writing.

Engine-model notes carried through the file:
  * A "Poke-Power"/"Poke-Body" is an Ability; activated ones carry an
    `activation` and offerability `condition(board, player_id, pokemon)`.
  * "As often as you like" = Activations.UNLIMITED, and MUST pair with a
    condition= that removes the offer once it would no-op.
  * Classic powers stop working while the carrier is Asleep/Confused/
    Paralyzed; "affected by a Special Condition" also counts Poisoned/Burned.
  * Effect attachments (ctx.attach_energy) never consume the once-per-turn
    manual attachment, which is exactly Rain Dance's clause.
  * LV.X cards are modeled as RESTORED-stage evolutions, so their "when you
    put the LV.X from your hand onto your Active <base>" is Triggers.ON_EVOLVE.
  * The engine has no "Imprison marker", no "Pokemon SP", and no persistent
    "Prizes face up" state; those three are approximated as noted below.
"""

from typing import Optional

from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.game.content.definitions import Activations, Triggers
from spirit.game.data_utils import Attack, def_for
from spirit.game.session.passives import Passive
from spirit.game.session.effects import is_supporter_card
from spirit.game.card_effects.attacks_common import (
    count_bench,
    count_energy,
    count_prizes_remaining,
    damage_counters_on,
)
from spirit.game.card_effects.passives_common import ability_lock_passive
from spirit.game.card_effects.pokemon import energy_provides_type, is_energy_card
from spirit.game.card_effects.support_common import search_to_hand


# ----------------------------------------------------------------------
# Predicates / helpers
# ----------------------------------------------------------------------

def _is_water_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.WATER.value)


def _is_grass_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.GRASS.value)


def _is_fire_energy(card) -> bool:
    return energy_provides_type(card, PokemonTypes.FIRE.value)


def _pokemon_has_type(pokemon, pokemon_type: PokemonTypes) -> bool:
    return pokemon_type.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _is_water_pokemon(pokemon) -> bool:
    return _pokemon_has_type(pokemon, PokemonTypes.WATER)


# Asleep/Confused/Paralyzed: the classic "this power can't be used if ..." trio.
_ACC_CONDITIONS = (
    SpecialConditions.ASLEEP.value,
    SpecialConditions.CONFUSED.value,
    SpecialConditions.PARALYZED.value,
)


def _acc_disabled(pokemon) -> bool:
    conditions = (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) \
        if pokemon is not None else []
    return any(c in _ACC_CONDITIONS for c in conditions)


def _any_special_condition(pokemon) -> bool:
    return bool(pokemon is not None
                and pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS))


async def _full_heal(ctx, pokemon) -> None:
    """Remove all damage counters from one Pokemon."""
    if pokemon is None:
        return
    current = pokemon.get_attribute(AttrID.HP, 0) or 0
    amount = (ctx.max_hp(pokemon) - current) // 10 * 10
    if amount > 0:
        await ctx.heal(amount, pokemon)


# ----------------------------------------------------------------------
# Count helpers for damage_per / bonus_if
# ----------------------------------------------------------------------

def hydro_pump_count(ctx) -> int:
    """Water Energy on Blastoise beyond the 3 paid for Hydro Pump; only the
    first two extras count ("Extra Water Energy after the 2nd doesn't count"
    is applied as the damage_per cap)."""
    return max(0, count_energy("self", PokemonTypes.WATER)(ctx) - 3)


def x_ball_count(ctx) -> int:
    """Energy attached to this Pokemon and to the Defending Pokemon."""
    return count_energy("self")(ctx) + count_energy("defender")(ctx)


def defender_has_two_counters(ctx) -> bool:
    return damage_counters_on("defender")(ctx) >= 2


# ----------------------------------------------------------------------
# Blastoise (CEL25 1) -- Rain Dance
# ----------------------------------------------------------------------

def rain_dance_condition(board, player_id, pokemon):
    if _acc_disabled(pokemon):
        return False
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(_is_water_energy(c) for c in hand.children):
        return False
    return any(_is_water_pokemon(p) for p in board.pokemon_in_play(player_id))


async def rain_dance(ctx):
    """As often as you like: attach 1 Water Energy from hand to 1 of your
    Water Pokemon. Effect attaches never burn the turn's manual attachment."""
    energies = [c for c in ctx.hand() if _is_water_energy(c)]
    picked = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose a Water Energy card to attach",
    )
    if not picked:
        return
    targets = [p for p in ctx.my_pokemon_in_play() if _is_water_pokemon(p)]
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your Water Pokémon to attach it to"
    )
    if target is not None:
        await ctx.attach_energy(picked[0], target)


# ----------------------------------------------------------------------
# Charizard (CEL25 2) -- Energy Burn
# ----------------------------------------------------------------------

class EnergyBurnPassive(Passive):
    """Every Energy attached to the carrier provides Fire until end of turn."""

    def __init__(self, carrier):
        self._carrier_id = carrier.entity_id if carrier is not None else None

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or holder.entity_id != self._carrier_id:
            return options
        return [[PokemonTypes.FIRE.value]]


def energy_burn_condition(board, player_id, pokemon):
    if _acc_disabled(pokemon) or pokemon is None:
        return False
    # The offer disappears once every attached Energy already provides Fire.
    return any(not energy_provides_type(e, PokemonTypes.FIRE.value)
               for e in board.attached_energies(pokemon))


async def energy_burn(ctx):
    """As often as you like: all Energy attached to Charizard becomes Fire
    Energy for the rest of the turn."""
    ctx.add_temporary_passive(
        ctx.source, EnergyBurnPassive(ctx.source),
        ctx.session.turn_state.turn_number,
    )


# ----------------------------------------------------------------------
# Venusaur (CEL25 3) -- Energy Trans
# ----------------------------------------------------------------------

def energy_trans_condition(board, player_id, pokemon):
    if _acc_disabled(pokemon):
        return False
    mine = board.pokemon_in_play(player_id)
    if len(mine) < 2:
        return False
    return any(any(_is_grass_energy(e) for e in board.attached_energies(p))
               for p in mine)


async def energy_trans(ctx):
    """As often as you like: move 1 Grass Energy from 1 of your Pokemon to a
    different one."""
    holders = [p for p in ctx.my_pokemon_in_play()
               if any(_is_grass_energy(e) for e in ctx.attached_energies(p))]
    if not holders:
        return
    source = await ctx.choose_pokemon(
        holders, "Choose 1 of your Pokémon with a Grass Energy attached"
    )
    if source is None:
        return
    energies = [e for e in ctx.attached_energies(source) if _is_grass_energy(e)]
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Grass Energy card to move",
    )
    if not picked:
        return
    others = [p for p in ctx.my_pokemon_in_play() if p is not source]
    if not others:
        return
    target = await ctx.choose_pokemon(
        others, "Choose a different Pokémon to attach it to"
    )
    if target is not None:
        await ctx.move_energy(picked[0], target)


# ----------------------------------------------------------------------
# Claydol (CEL25 16) -- Cosmic Power
# ----------------------------------------------------------------------

def cosmic_power_condition(board, player_id, pokemon):
    if _any_special_condition(pokemon):
        return False
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len(hand.children) > 0


async def cosmic_power(ctx):
    """Once per turn: put up to 2 cards from your hand on the bottom of your
    deck in any order. If you do, draw until you have 6 cards in hand."""
    picks = await ctx.choose_cards(
        ctx.hand(), 2, minimum=0,
        prompt="Choose up to 2 cards to put on the bottom of your deck",
    )
    if not picks:
        return
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)
    await ctx.draw_until(6)


# ----------------------------------------------------------------------
# Dark Gyarados (CEL25 5) -- Final Beam
# ----------------------------------------------------------------------

async def final_beam(ctx):
    """When Knocked Out by an attack: flip a coin; if heads, deal 20 damage
    per Water Energy that was attached to Dark Gyarados to the Pokemon that
    Knocked it Out.

    The engine discards the KO'd stack before ON_KNOCKED_OUT fires, so the
    attached Water Energies are counted in the owner's discard pile, where
    they just landed (an over-count only when Water Energies were discarded
    earlier in the same game).
    """
    if not ctx.ko_from_attack or ctx.ko_attacker is None:
        return
    if _acc_disabled(ctx.source):
        return
    results = await ctx.flip_coins(1, "Final Beam")
    if not results or not results[0]:
        return
    water = sum(1 for c in ctx.discard_pile(ctx.player_id) if _is_water_energy(c))
    if water > 0:
        await ctx.deal_damage(20 * water, target=ctx.ko_attacker)


# ----------------------------------------------------------------------
# Garchomp C LV.X (CEL25 18) -- Healing Breath + Dragon Rush
# ----------------------------------------------------------------------

async def healing_breath(ctx):
    """When Garchomp C LV.X is put onto your Active Garchomp C: remove all
    damage counters from each of your Pokemon. ("Pokemon SP" is not modeled;
    the owner's whole side is healed instead.)"""
    mine = ctx.my_pokemon_in_play()
    if not any(_is_damaged(ctx, p) for p in mine):
        return
    if not await ctx.ask_yes_no("Remove all damage counters from each of your Pokémon?"):
        return
    for pokemon in mine:
        await _full_heal(ctx, pokemon)


def _is_damaged(ctx, pokemon) -> bool:
    return (pokemon.get_attribute(AttrID.HP, 0) or 0) < ctx.max_hp(pokemon)


async def dragon_rush(ctx):
    """Discard 2 Energy attached to Garchomp C; choose 1 of the opponent's
    Pokemon: this attack does 80 to it (no W/R off the Active). The
    can't-use-next-turn clause is Attack(locks_next_turn=True)."""
    await ctx.discard_energy_from(
        ctx.attacker, 2,
        prompt="Choose 2 Energy attached to Garchomp C to discard",
    )
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(80, target=target, apply_modifiers=False)


# ----------------------------------------------------------------------
# Gardevoir ex (CEL25 14) -- Imprison + Flame Ball
# ----------------------------------------------------------------------

def imprison_condition(board, player_id, pokemon):
    if _any_special_condition(pokemon):
        return False
    return board.active_pokemon(player_id) is pokemon


async def imprison(ctx):
    """Once per turn, if Gardevoir ex is your Active Pokemon: the chosen
    opponent's Pokemon can't use any Poke-Powers or Poke-Bodies. The engine
    has no marker state, so the lock rides a permanent temp passive on the
    target (it clears when that Pokemon leaves play). Attacks are unaffected
    because ability_locked only gates activated abilities."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon to Imprison"
    )
    if target is None:
        return
    ctx.add_temporary_passive(target, ability_lock_passive(lambda p, c: p is c))


async def flame_ball(ctx):
    """80. You may move a Fire Energy attached to Gardevoir ex to 1 of your
    Benched Pokemon."""
    await ctx.deal_damage()
    energies = [e for e in ctx.attached_energies(ctx.attacker) if _is_fire_energy(e)]
    bench = ctx.my_bench()
    if not energies or not bench:
        return
    if not await ctx.ask_yes_no(
        "Move a Fire Energy attached to Gardevoir ex to 1 of your Benched Pokémon?"
    ):
        return
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Fire Energy card to move",
    )
    if not picked:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is not None:
        await ctx.move_energy(picked[0], target)


# ----------------------------------------------------------------------
# Luxray GL LV.X (CEL25 17) -- Bright Look
# ----------------------------------------------------------------------

async def bright_look(ctx):
    """When Luxray GL LV.X is put onto your Active Luxray GL: switch the
    Defending Pokemon with 1 of your opponent's Benched Pokemon."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    if not await ctx.ask_yes_no(
        "Switch the Defending Pokémon with 1 of your opponent's Benched Pokémon?"
    ):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


# ----------------------------------------------------------------------
# Mew ex (CEL25 13) -- Versatile + Power Move
# ----------------------------------------------------------------------

class VersatilePassive(Passive):
    """Mew ex can use the attacks of all Pokemon in play as its own (energy
    costs still apply). Its own attacks are not re-granted."""

    def granted_attacks(self, board, pokemon, carrier):
        if carrier is not pokemon:
            return []
        attacks = []
        for player_id in board.player_ids:
            for other in board.pokemon_in_play(player_id):
                if other is pokemon:
                    continue
                for ability in getattr(def_for(other.archetype_id),
                                       "abilities", None) or []:
                    if isinstance(ability, Attack):
                        attacks.append(ability)
        return attacks


async def power_move(ctx):
    """Search your deck for an Energy card and attach it to Mew ex. Shuffle
    your deck. Then, you may switch Mew ex with 1 of your Benched Pokemon."""
    picks = await ctx.search_deck(
        is_energy_card, count=1, minimum=0,
        prompt="Choose an Energy card to attach to Mew ex",
    )
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)
        if ctx.attacker.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(ctx.attacker.entity_id)
    await ctx.shuffle_deck()
    bench = ctx.my_bench()
    if not bench:
        return
    if await ctx.ask_yes_no("Switch Mew ex with 1 of your Benched Pokémon?"):
        target = await ctx.choose_pokemon(bench, "Choose the new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


# ----------------------------------------------------------------------
# Umbreon * (CEL25 15) -- Dark Ray
# ----------------------------------------------------------------------

async def dark_ray(ctx):
    """When you put Umbreon * from your hand onto your Bench: choose 1 card
    from your opponent's hand without looking and discard it."""
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    if not await ctx.ask_yes_no("Discard 1 card from your opponent's hand at random?"):
        return
    from spirit.game.card_effects.attacks_common import discard_random_from_hand
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)


# ----------------------------------------------------------------------
# Umbreon * (CEL25 15) -- Feint Attack
# ----------------------------------------------------------------------

async def feint_attack(ctx):
    """30 to 1 of the opponent's Pokemon, unaffected by Weakness, Resistance,
    or any other effects on that Pokemon."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(30, target=target, apply_modifiers=False,
                              ignore_target_effects=True)


# ----------------------------------------------------------------------
# Rocket's Zapdos (CEL25 7) -- Electroburn
# ----------------------------------------------------------------------

async def electroburn(ctx):
    """70. Rocket's Zapdos does damage to itself equal to 10 times the number
    of Lightning Energy cards attached to it."""
    await ctx.deal_damage()
    lightning = count_energy("self", PokemonTypes.LIGHTNING, cards=True)(ctx)
    if lightning > 0:
        await ctx.deal_damage(10 * lightning, target=ctx.attacker,
                              apply_modifiers=False)


# ----------------------------------------------------------------------
# Shining Magikarp (CEL25 10) -- Gold Scale + Dragon Bond
# ----------------------------------------------------------------------

_GYARADOS_FAMILY = ("Gyarados", "Dark Gyarados", "Shining Gyarados")


def _is_gyarados_family(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", None))
    return getattr(definition, "display_name", "") in _GYARADOS_FAMILY


async def gold_scale(ctx):
    """Your opponent may draw 2 cards. Either way, you may draw 2 cards."""
    if await ctx.ask_yes_no(
        "Your opponent may draw 2 cards. Does the opponent draw 2 cards?",
        player_id=ctx.opponent_id,
    ):
        await ctx.draw_cards(2, ctx.opponent_id)
    if await ctx.ask_yes_no("Draw 2 cards?"):
        await ctx.draw_cards(2)


def dragon_bond():
    """Search your deck for a card named Gyarados, Dark Gyarados, or Shining
    Gyarados, reveal it, put it into your hand, and shuffle your deck."""
    return search_to_hand(
        predicate=_is_gyarados_family, count=1, reveal=True,
        prompt="Choose a card named Gyarados, Dark Gyarados, or Shining Gyarados.",
    )


# ----------------------------------------------------------------------
# Tapu Lele-GX (CEL25 25) -- Wonder Tag / Energy Drive / Tapu Cure GX
# ----------------------------------------------------------------------

def wonder_tag():
    """When you play this Pokemon from your hand onto your Bench: search your
    deck for a Supporter card, reveal it, put it into your hand, and shuffle."""
    return search_to_hand(
        predicate=is_supporter_card, count=1, reveal=True,
        prompt="Choose a Supporter card to put into your hand.",
    )


async def energy_drive(ctx):
    """20x the Energy attached to both Active Pokemon, unaffected by Weakness
    or Resistance."""
    amount = 20 * (count_energy("my_active")(ctx)
                   + count_energy("opponent_active")(ctx))
    if amount > 0:
        await ctx.deal_damage(amount, apply_modifiers=False)


async def tapu_cure_gx(ctx):
    """Heal all damage from 2 of your Benched Pokemon. (The "only 1 GX attack
    per game" clause has no engine hook; this attack is otherwise scripted.)"""
    bench = ctx.my_bench()
    if not bench:
        return
    picks = await ctx.choose_cards(
        bench, 2, minimum=0,
        prompt="Choose up to 2 of your Benched Pokémon to heal",
    )
    for target in picks or []:
        await _full_heal(ctx, target)


# ----------------------------------------------------------------------
# Team Magma's Groudon (CEL25 11) -- Power Saver
# ----------------------------------------------------------------------

def _team_magma_in_play(board) -> int:
    count = 0
    for player_id in board.player_ids:
        for pokemon in board.pokemon_in_play(player_id):
            name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
            if "Team Magma" in name:
                count += 1
    return count


def power_saver_allows_attack(board, player_id, pokemon):
    """Power Saver gates the attacks directly: Groudon can't attack while 3 or
    fewer Pokemon with "Team Magma" in their name are in play."""
    return _team_magma_in_play(board) > 3


# ----------------------------------------------------------------------
# Trainers
# ----------------------------------------------------------------------

async def imposter_professor_oak(ctx):
    """Your opponent shuffles their hand into their deck, then draws 7."""
    await ctx.shuffle_into_deck(ctx.hand(ctx.opponent_id), ctx.opponent_id)
    await ctx.draw_cards(7, ctx.opponent_id)


async def rockets_admin(ctx):
    """Each player shuffles their hand into their deck. Then each player draws
    up to as many cards as they have Prize cards left (you draw first)."""
    for player_id in (ctx.player_id, ctx.opponent_id):
        await ctx.shuffle_into_deck(ctx.hand(player_id), player_id)
    you = count_prizes_remaining("mine")(ctx)
    them = count_prizes_remaining("opponent")(ctx)
    await ctx.draw_cards(you, ctx.player_id)
    await ctx.draw_cards(them, ctx.opponent_id)


async def here_comes_team_rocket(ctx):
    """Each player plays with their Prize cards face up for the rest of the
    game. The client has no persistent prize-face-up state, so both Prize
    piles are revealed once instead (an approximation of the lasting effect)."""
    for player_id in (ctx.player_id, ctx.opponent_id):
        area = ctx.board.find_player_area(player_id, "prizePile")
        if area:
            await ctx.reveal_cards(list(area.children))
