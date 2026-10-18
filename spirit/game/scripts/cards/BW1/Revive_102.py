from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon

async def revive(ctx):
    """Put a Basic Pokemon from your discard pile onto your Bench."""
    basics = [c for c in ctx.discard_pile() if is_basic_pokemon(c)]
    if not basics:
        return
    picks = await ctx.choose_cards(basics, 1, minimum=1, prompt='Choose a Basic Pokemon to put onto your Bench')
    if picks:
        await ctx.bench_pokemon(picks[0])
card = ItemCardDef(guid='cc687251-8e9c-5a64-85ad-7db76532acd4', key='BW1', name='com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name', display_name='Revive', searchable_by=['Revive', 'Item'], subtypes=['Item'], collector_number=102, set_code='BW1', rarity=Rarities.Uncommon, effect=revive)
