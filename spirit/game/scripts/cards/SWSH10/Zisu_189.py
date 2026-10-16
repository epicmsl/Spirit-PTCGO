from spirit.game.card_effects.trainers import zisu
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="cad0b9be-03d2-5932-8559-e1f42ff4b198",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Zisu.Name",
    display_name="Zisu",
    searchable_by=["Zisu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    effect=zisu,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
