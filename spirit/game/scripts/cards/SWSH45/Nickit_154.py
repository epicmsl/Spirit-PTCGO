from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

async def instigate(ctx):
    moved = await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
    if moved > 0:
        await ctx.draw_cards(3, player_id=ctx.opponent_id)
card = PokemonCardDef(guid='340740a1-7041-50a8-a6a4-28f8d69e3584', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name', display_name='Nickit', searchable_by=['Nickit', 'Basic', 'Nickit'], subtypes=['Basic'], collector_number=154, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=70, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, family_id=827, abilities=[Attack(title='Instigate', game_text='Your opponent shuffles their hand and puts it on the bottom of their deck. If they put any cards on the bottom of their deck in this way, they draw 3 cards.', cost={PokemonTypes.DARKNESS: 1}, effect=instigate)])
