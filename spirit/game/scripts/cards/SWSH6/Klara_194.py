from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.trainers import klara

card = SupporterCardDef(
    guid="f37c5911-13a8-562f-90be-0b3633a6cbff",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Klara.Name",
    display_name="Klara",
    searchable_by=["Klara", "Supporter"],
    subtypes=["Supporter"],
    collector_number=194,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    effect=klara,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
