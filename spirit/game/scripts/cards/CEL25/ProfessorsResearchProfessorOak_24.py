from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="39450361-45e4-5450-b8eb-e0d5b5b4789b",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorOak.Name",
    display_name="Professor's Research (Professor Oak)",
    searchable_by=["Professor's Research (Professor Oak)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=24,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    effect=professors_research,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
