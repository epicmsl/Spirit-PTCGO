from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

async def leech_life(ctx):
    """Heal from this Pokemon the same amount of damage you did."""
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt)
card = PokemonCardDef(guid='4133e219-0410-59fd-b8cc-3f699ecd866c', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name', display_name='Joltik', searchable_by=['Joltik', 'Basic', 'Joltik'], subtypes=['Basic'], collector_number=45, set_code='BW1', rarity=Rarities.Common, hp=30, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=595, abilities=[Attack(title='Leech Life', game_text='Heal from this Pokémon the same amount of damage you did to the Defending Pokémon.', cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=leech_life)])
