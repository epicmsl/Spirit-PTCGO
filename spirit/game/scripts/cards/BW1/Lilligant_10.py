from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import flip_damage

async def _confuse_self(ctx):
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)

async def leaf_storm(ctx):
    """Heal 20 damage from each of your Grass Pokemon."""
    for pokemon in ctx.my_pokemon_in_play():
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        if PokemonTypes.GRASS.value in types:
            await ctx.heal(20, pokemon)
card = PokemonCardDef(guid='605b178e-1312-50fa-97ca-53c0304f9b20', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name', display_name='Lilligant', searchable_by=['Lilligant', 'Stage 1', 'Lilligant'], subtypes=['Stage 1'], collector_number=10, set_code='BW1', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name', family_id=548, abilities=[Attack(title='Petal Dance', game_text='Flip 3 coins. This attack does 30 damage times the number of heads. This Pokémon is now Confused.', cost={PokemonTypes.GRASS: 1}, damage=30, damage_operator='x', effect=flip_damage(coins=3, per_heads=30, also=_confuse_self)), Attack(title='Leaf Storm', game_text='Heal 20 damage from each of your Grass Pokémon.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=leaf_storm)])
