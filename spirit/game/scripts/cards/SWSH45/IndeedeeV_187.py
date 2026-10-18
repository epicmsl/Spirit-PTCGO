from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

async def watch_over(ctx):
    """Once during your turn, you may heal 20 damage from your Active Pokémon."""
    if await ctx.ask_yes_no('Heal 20 damage from your Active Pokémon?'):
        await ctx.heal(20)
card = PokemonCardDef(guid='24081da7-1166-5654-8725-b2c3fd8a0280', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.IndeedeeV.Name', display_name='Indeedee V', searchable_by=['Indeedee V', 'Basic', 'V', 'IndeedeeV'], subtypes=['Basic', 'V'], collector_number=187, set_code='SWSH45', rarity=Rarities.RareHoloV, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=180, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.DARKNESS, resistance_type=PokemonTypes.FIGHTING, family_id=876, abilities=[Ability(title='Watch Over', game_text='Once during your turn, you may heal 20 damage from your Active Pokémon.', effect=watch_over, activation=Activations.ONCE_PER_TURN), Attack(title='Psychic', game_text="This attack does 60 more damage for each Energy attached to your opponent's Active Pokémon.", cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=10, damage_operator='+')])
