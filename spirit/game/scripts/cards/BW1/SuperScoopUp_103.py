from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

async def super_scoop_up(ctx):
    """Flip a coin. If heads, return your Active Pokemon to your hand."""
    results = await ctx.flip_coins(1, 'Super Scoop Up')
    if not results or not results[0]:
        return
    active = ctx.my_active()
    if active is None:
        return
    await ctx.discard_cards(list(ctx.attached_energies(active)))
    await ctx.put_in_hand([active], reveal=False)
    await ctx.session._promote_new_active(ctx.player_id)
card = ItemCardDef(guid='f7a4d1e1-d87b-5656-8db6-fcffeec8a4aa', key='BW1', name='com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name', display_name='Super Scoop Up', searchable_by=['Super Scoop Up', 'Item'], subtypes=['Item'], collector_number=103, set_code='BW1', rarity=Rarities.Uncommon, effect=super_scoop_up)
