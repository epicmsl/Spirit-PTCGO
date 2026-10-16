from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.passives_common import apply_protection

async def _fly_heads(ctx):
    await ctx.deal_damage()
    await apply_protection(ctx, prevent=True, through_own_next_turn=True)
card = PokemonCardDef(guid='4a60386b-3126-57b4-aef9-d50056a4d0ce', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name', display_name='Unfezant', searchable_by=['Unfezant', 'Stage 2', 'Unfezant'], subtypes=['Stage 2'], collector_number=86, set_code='BW1', rarity=Rarities.Rare, hp=120, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE2, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name', family_id=519, abilities=[Attack(title='Fly', game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 2}, damage=50, effect=flip_or_nothing(then=_fly_heads)), Attack(title='Cutting Wind', cost={PokemonTypes.COLORLESS: 3}, damage=70)])
