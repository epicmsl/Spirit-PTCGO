from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.support_common import search_to_bench

async def poke_ball(ctx):
    """Flip a coin. If heads, search your deck for a Basic Pokemon onto your Bench."""
    results = await ctx.flip_coins(1, 'Poké Ball')
    if not results or not results[0]:
        return
    await search_to_bench(predicate=is_basic_pokemon, count=1)(ctx)
card = ItemCardDef(guid='e5e2ab0f-ffa5-5aeb-9d70-67938bbdc3af', key='BW1', name='com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name', display_name='Poké Ball', searchable_by=['Poké Ball', 'Item'], subtypes=['Item'], collector_number=97, set_code='BW1', rarity=Rarities.Uncommon, effect=poke_ball)
