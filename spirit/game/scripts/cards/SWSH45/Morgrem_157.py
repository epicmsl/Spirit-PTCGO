from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

async def false_surrender(ctx):
    """60. This attack's damage isn't affected by any effects on your
    opponent's Active Pokemon."""
    await ctx.deal_damage(ignore_target_effects=True)
card = PokemonCardDef(guid='f0adc117-5739-5be6-92c2-e7abca7f0fa6', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name', display_name='Morgrem', searchable_by=['Morgrem', 'Stage 1', 'Morgrem'], subtypes=['Stage 1'], collector_number=157, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=90, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name', family_id=859, abilities=[Attack(title='Bite', cost={PokemonTypes.DARKNESS: 1}, damage=30), Attack(title='False Surrender', game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.", cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=false_surrender)])
