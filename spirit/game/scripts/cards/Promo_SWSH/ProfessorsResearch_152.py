from spirit.game.data_utils import SupporterCardDef, unimplemented, Foil
from spirit.game.card_effects.trainers import professors_research
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="38c4384d-cdb2-58b9-8db4-a59a90317ab3",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=152,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    effect=professors_research,

)
