from spirit.game.data_utils import SupporterCardDef, unimplemented, Foil
from spirit.game.card_effects.trainers import bosss_orders, opponent_has_bench, opponent_play_targets
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="50401e4d-c7da-5017-b630-5f1aeb562012",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BosssOrders.Name",
    display_name="Boss's Orders",
    searchable_by=["Boss's Orders", "Supporter"],
    subtypes=["Supporter"],
    collector_number=251,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    effect=bosss_orders,

)
