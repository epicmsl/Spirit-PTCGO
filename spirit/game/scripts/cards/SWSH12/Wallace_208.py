from spirit.game.card_effects.trainers import wallace
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="2c15487f-3b4a-5926-a3e6-1ea07f18e6fe",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wallace.Name",
    display_name="Wallace",
    searchable_by=["Wallace", "Supporter"],
    subtypes=["Supporter"],
    collector_number=208,
    set_code="SWSH12",
    rarity=Rarities.RareRainbow,
    effect=wallace,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET])
)
