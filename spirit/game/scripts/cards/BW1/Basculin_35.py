from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

async def crunch(ctx):
    """Flip a coin. If heads, discard an Energy attached to the Defending Pokemon."""
    await ctx.deal_damage()
    target = ctx.defender
    if target is None or ctx.effects_blocked(target):
        return
    results = await ctx.flip_coins(1, 'Crunch')
    if results and results[0]:
        await ctx.discard_energy_from(target, 1, prompt='Choose Energy to discard from the Defending Pokemon')
card = PokemonCardDef(guid='8fe1852a-d6b1-57d7-ae21-ef983fa625e7', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Basculin.Name', display_name='Basculin', searchable_by=['Basculin', 'Basic', 'Basculin'], subtypes=['Basic'], collector_number=35, set_code='BW1', rarity=Rarities.Uncommon, hp=70, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=550, abilities=[Attack(title='Crunch', game_text='Flip a coin. If heads, discard an Energy attached to the Defending Pokémon.', cost={PokemonTypes.WATER: 2}, damage=30, effect=crunch)])
