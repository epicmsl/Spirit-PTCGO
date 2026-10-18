from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

async def constant_rattle(ctx):
    """Flip 3 coins: 10/30/60 damage for 1/2/3 heads."""
    results = await ctx.flip_coins(3, 'Constant Rattle')
    heads = sum((1 for r in results if r))
    if heads == 1:
        await ctx.deal_damage(10)
    elif heads == 2:
        await ctx.deal_damage(30)
    elif heads == 3:
        await ctx.deal_damage(60)

async def giga_drain(ctx):
    """Heal from this Pokemon the same amount of damage you did."""
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt)
card = PokemonCardDef(guid='1ab09884-3b5b-5690-a61c-389219191e9f', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name', display_name='Maractus', searchable_by=['Maractus', 'Basic', 'Maractus'], subtypes=['Basic'], collector_number=12, set_code='BW1', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, family_id=556, abilities=[Attack(title='Constant Rattle', game_text='Flip 3 coins. If 1 of them is heads, this attack does 10 damage. If 2 of them are heads, this attack does 30 damage. If all of them are heads, this attack does 60 damage.', cost={PokemonTypes.GRASS: 1}, effect=constant_rattle), Attack(title='Giga Drain', game_text='Heal from this Pokémon the same amount of damage you did to the Defending Pokémon.', cost={PokemonTypes.GRASS: 3}, damage=50, effect=giga_drain)])
