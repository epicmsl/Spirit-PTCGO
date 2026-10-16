from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID

async def leaf_storm(ctx):
    """Heal 20 damage from each of your Grass Pokemon."""
    for pokemon in ctx.my_pokemon_in_play():
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.GRASS.value in types:
            await ctx.heal(20, pokemon)
card = PokemonCardDef(guid='6e5b0f1a-0031-55fb-b97b-1592787c8826', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name', display_name='Serperior', searchable_by=['Serperior', 'Stage 2', 'Serperior'], subtypes=['Stage 2'], collector_number=5, set_code='BW1', rarity=Rarities.RareHolo, foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.TINSEL]), hp=130, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=0, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name', family_id=495, abilities=[Attack(title='Vine Whip', cost={PokemonTypes.COLORLESS: 2}, damage=40), Attack(title='Leaf Storm', game_text='Heal 20 damage from each of your Grass Pokémon.', cost={PokemonTypes.GRASS: 2}, damage=60, effect=leaf_storm)])
