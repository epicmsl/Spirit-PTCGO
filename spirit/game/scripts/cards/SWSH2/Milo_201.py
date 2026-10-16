from spirit.game.card_effects.trainers import milo
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="e9da1e69-e321-59ee-9b32-d36030c0d9c2",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Milo.Name",
    display_name="Milo",
    searchable_by=["Milo", "Supporter"],
    subtypes=["Supporter"],
    collector_number=201,
    set_code="SWSH2",
    rarity=Rarities.RareRainbow,
    effect=milo,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET])
)
