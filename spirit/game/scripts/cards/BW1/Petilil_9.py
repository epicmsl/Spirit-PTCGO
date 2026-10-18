from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

async def _heal_self_10(ctx):
    await ctx.heal(10)
card = PokemonCardDef(guid='29b1b04c-0a55-54b4-ba0c-c35cf82da3a6', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name', display_name='Petilil', searchable_by=['Petilil', 'Basic', 'Petilil'], subtypes=['Basic'], collector_number=9, set_code='BW1', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, family_id=548, abilities=[Attack(title='Magical Leaf', game_text='Flip a coin. If heads, this attack does 10 more damage and heal 10 damage from this Pokémon.', cost={PokemonTypes.GRASS: 1}, damage=10, damage_operator='+', effect=flip_damage(bonus=10, also=_heal_self_10))])
