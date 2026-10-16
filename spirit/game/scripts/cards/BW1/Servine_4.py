from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

async def wring_out(ctx):
    """Flip a coin. If heads, the Defending Pokemon is now Paralyzed and
    discard an Energy attached to it."""
    await ctx.deal_damage()
    target = ctx.defender
    if target is None or ctx.effects_blocked(target):
        return
    results = await ctx.flip_coins(1, 'Wring Out')
    if results and results[0]:
        await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)
        await ctx.discard_energy_from(target, 1, prompt='Choose Energy to discard from the Defending Pokemon')
card = PokemonCardDef(guid='cf249cf9-a663-56aa-8634-c8ee9bdd4178', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name', display_name='Servine', searchable_by=['Servine', 'Stage 1', 'Servine'], subtypes=['Stage 1'], collector_number=4, set_code='BW1', rarity=Rarities.Uncommon, hp=80, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name', family_id=495, abilities=[Attack(title='Wring Out', game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed and discard an Energy attached to the Defending Pokémon.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=wring_out)])
