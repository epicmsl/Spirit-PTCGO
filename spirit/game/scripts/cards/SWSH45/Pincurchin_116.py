from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, SpecialConditions

async def shocking_needles(ctx):
    """Flip 4 coins. 30 damage per heads; 2+ heads also Paralyzes the Defending Pokemon."""
    results = await ctx.flip_coins(4, ctx.ability.title)
    heads = sum(results)
    if heads:
        await ctx.deal_damage(30 * heads)
    if heads >= 2 and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
card = PokemonCardDef(guid='2a640de5-bd9f-5379-b6ad-0d292735046e', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pincurchin.Name', display_name='Pincurchin', searchable_by=['Pincurchin', 'Basic', 'Pincurchin'], subtypes=['Basic'], collector_number=116, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=80, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, family_id=871, abilities=[Attack(title='Shocking Needles', game_text="Flip 4 coins. This attack does 30 damage for each heads. If at least 2 of them are heads, your opponent's Active Pokémon is now Paralyzed.", cost={PokemonTypes.LIGHTNING: 2}, damage=30, effect=shocking_needles, damage_operator='x')])
