from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="f46e6d11-e7ea-54ae-9e32-853a27814e04",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    effect=professors_research,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
