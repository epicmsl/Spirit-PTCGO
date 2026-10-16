from spirit.game.card_effects.trainers import irida
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="99351945-9d97-5a0e-a68f-3cead4b2ba95",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Irida.Name",
    display_name="Irida",
    searchable_by=["Irida", "Supporter"],
    subtypes=["Supporter"],
    collector_number=186,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    effect=irida,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
