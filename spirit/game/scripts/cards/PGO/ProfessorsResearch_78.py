from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="838f8f22-01c5-5132-a18e-92f11036a628",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="PGO",
    rarity=Rarities.RareUltra,
    effect=professors_research,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
