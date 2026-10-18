from spirit.game.data_utils import Foil, SupporterCardDef
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.trainers import professors_research

card = SupporterCardDef(
    guid="86d26aad-0a8b-5aa8-bec2-82c4ec9104a2",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorOak.Name",
    display_name="Professor's Research (Professor Oak)",
    searchable_by=["Professor's Research (Professor Oak)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=23,
    set_code="CEL25",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.FLATSILVER]),
    effect=professors_research
)
