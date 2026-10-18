from spirit.game.card_effects.trainers import irida
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="a9526a63-bfc6-540b-b082-fddce9cbcb17",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Irida.Name",
    display_name="Irida",
    searchable_by=["Irida", "Supporter"],
    subtypes=["Supporter"],
    collector_number=204,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    effect=irida,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET])
)
