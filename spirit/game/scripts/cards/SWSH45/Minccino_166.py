from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import flip_damage

async def glance(ctx):
    """Look at the top card of your opponent's deck."""
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if not top:
        return
    await ctx.present_card_choice(top[0], "Top card of your opponent's deck", ['OK'])
card = PokemonCardDef(guid='a5f188c3-ae3e-596b-b79f-098bbaff6f9d', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name', display_name='Minccino', searchable_by=['Minccino', 'Basic', 'Minccino'], subtypes=['Basic'], collector_number=166, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=70, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=572, abilities=[Attack(title='Glance', game_text="Look at the top card of your opponent's deck.", cost={PokemonTypes.COLORLESS: 1}, effect=glance), Attack(title='Tail Slap', game_text='Flip 2 coins. This attack does 20 damage for each heads.', cost={PokemonTypes.COLORLESS: 2}, damage=20, damage_operator='x', effect=flip_damage(coins=2, per_heads=20))])
