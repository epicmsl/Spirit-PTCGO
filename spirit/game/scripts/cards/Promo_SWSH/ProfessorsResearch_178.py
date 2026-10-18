from spirit.game.data_utils import SupporterCardDef, unimplemented, Foil
from spirit.game.card_effects.trainers import professors_research
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="e6a6f13f-2b3a-5368-8888-1ef6d2bc0942",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    effect=professors_research,

)
