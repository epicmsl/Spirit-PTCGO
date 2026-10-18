from spirit.game.data_utils import SupporterCardDef, unimplemented, Foil
from spirit.game.card_effects.trainers import marnie
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="33d69943-a459-5c25-8e7e-934801ee7f26",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Marnie.Name",
    display_name="Marnie",
    searchable_by=["Marnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=121,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    effect=marnie,

)
