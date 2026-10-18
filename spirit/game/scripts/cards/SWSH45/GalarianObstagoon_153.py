from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID
from spirit.game.card_effects.passives_common import prevent_damage_when

async def untamed_shout(ctx):
    if not await ctx.ask_yes_no("Put 3 damage counters on 1 of your opponent's Pokémon?"):
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(30, target=target, as_counters=True)

async def obstruct(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, prevent_damage_when(_attacker_is_basic))

def _attacker_is_basic(calc, carrier) -> bool:
    attacker = calc.attacker
    return attacker is not None and attacker.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
card = PokemonCardDef(guid='bad7a083-0000-5ca5-95fa-83ab10d353cc', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.GalarianObstagoon.Name', display_name='Galarian Obstagoon', searchable_by=['Galarian Obstagoon', 'Stage 2', 'GalarianObstagoon'], subtypes=['Stage 2'], collector_number=153, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=160, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name', family_id=263, abilities=[Ability(title='Untamed Shout', game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put 3 damage counters on 1 of your opponent's Pokémon.", effect=untamed_shout, trigger=Triggers.ON_EVOLVE), Attack(title='Obstruct', game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Basic Pokémon.", cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1}, damage=90, effect=obstruct)])
