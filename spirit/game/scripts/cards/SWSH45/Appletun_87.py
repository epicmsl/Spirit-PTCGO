from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.support_common import requires_in_play

async def delicious_aroma(ctx):
    """You may flip a coin; on heads switch an opposing Benched Basic in."""
    if not await ctx.ask_yes_no("Flip a coin to switch 1 of your opponent's Benched Basic Pokémon with their Active Pokémon?"):
        return
    heads = (await ctx.flip_coins(1, 'Delicious Aroma'))[0]
    if not heads:
        return
    candidates = [p for p in ctx.opponent_bench() if is_basic_pokemon(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)
card = PokemonCardDef(guid='16a8710d-c4e6-5ab0-abaa-bdbdc95c5ca8', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Appletun.Name', display_name='Appletun', searchable_by=['Appletun', 'Stage 1', 'Appletun'], subtypes=['Stage 1'], collector_number=87, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=90, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.FIRE, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name', family_id=840, abilities=[Ability(title='Delicious Aroma', game_text="Once during your turn, you may flip a coin. If heads, switch 1 of your opponent's Benched Basic Pokémon with their Active Pokémon.", effect=delicious_aroma, activation=Activations.ONCE_PER_TURN, condition=requires_in_play(is_basic_pokemon, side='opponent')), Attack(title='Solar Beam', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=70)])
