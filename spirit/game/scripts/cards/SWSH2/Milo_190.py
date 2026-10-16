from spirit.game.card_effects.trainers import milo
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="4b84cead-436a-5955-b124-28ba7f216264",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Milo.Name",
    display_name="Milo",
    searchable_by=["Milo", "Supporter"],
    subtypes=["Supporter"],
    collector_number=190,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    effect=milo,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
