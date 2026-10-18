from spirit.game.card_effects.trainers import piers
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="e7090528-8228-5af0-9b0d-c625e2b8126d",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Piers.Name",
    display_name="Piers",
    searchable_by=["Piers", "Supporter"],
    subtypes=["Supporter"],
    collector_number=187,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
    effect=piers,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
