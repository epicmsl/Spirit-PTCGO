from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import recoil_attack

async def risk_taker(ctx):
    """Flip a coin. If heads, discard the top 5 cards of your opponent's
    deck. If tails, discard the top 5 cards of your deck."""
    heads = await ctx.flip_coins(1, 'Risk Taker')
    pid = ctx.opponent_id if heads[0] else ctx.player_id
    await ctx.discard_cards(ctx.deck_top(5, player_id=pid))
card = PokemonCardDef(guid='35041fc6-a6a4-52c4-ba0e-3ed0b56f5e89', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name', display_name='Toxtricity', searchable_by=['Toxtricity', 'Stage 1', 'Toxtricity'], subtypes=['Stage 1'], collector_number=115, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=120, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name', family_id=848, abilities=[Attack(title='Risk Taker', game_text="Flip a coin. If heads, discard the top 5 cards of your opponent's deck. If tails, discard the top 5 cards of your deck.", cost={PokemonTypes.COLORLESS: 2}, effect=risk_taker), Attack(title='Thunder Jolt', game_text='This Pokémon also does 30 damage to itself.', cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=160, effect=recoil_attack(30))])
