from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects
from spirit.game.session.effects import EffectContext

async def worker(ctx: EffectContext):
    await ctx.draw_cards(3)
    await ctx.discard_stadium()

card = SupporterCardDef(
    guid="b7d2c717-b799-5909-b25c-f6a831bf8ef3",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Worker.Name",
    display_name="Worker",
    searchable_by=["Worker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=195,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    effect=worker,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
