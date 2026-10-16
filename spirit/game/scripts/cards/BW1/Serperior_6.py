from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID
from spirit.game.card_effects.pokemon import energy_provides_type

async def royal_heal(ctx):
    """Between turns: heal 10 damage from each of your Pokemon."""
    for pokemon in ctx.my_pokemon_in_play():
        if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon):
            await ctx.heal(10, pokemon)

async def leaf_tornado(ctx):
    """Move as many Grass Energy attached to your Pokemon to your other Pokemon."""
    mine = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(mine, mine, predicate=lambda e: energy_provides_type(e, PokemonTypes.GRASS.value))
card = PokemonCardDef(guid='aa93b5fc-6b56-5528-b06f-ce848596bf76', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name', display_name='Serperior', searchable_by=['Serperior', 'Stage 2', 'Serperior'], subtypes=['Stage 2'], collector_number=6, set_code='BW1', rarity=Rarities.RareHolo, foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.TINSEL]), hp=130, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name', family_id=495, abilities=[Ability(title='Royal Heal', game_text='At any time between turns, heal 10 damage from each of your Pokémon.', effect=royal_heal, trigger=Triggers.BETWEEN_TURNS), Attack(title='Leaf Tornado', game_text='Move as many Grass Energy attached to your Pokémon to your other Pokémon in any way you like.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=60, effect=leaf_tornado)])
