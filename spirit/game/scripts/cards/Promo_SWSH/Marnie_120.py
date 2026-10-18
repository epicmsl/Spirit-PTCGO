from spirit.game.data_utils import SupporterCardDef, unimplemented, Foil
from spirit.game.card_effects.trainers import marnie
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="21f1d892-71cc-57d3-9e1f-8cace779171f",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Marnie.Name",
    display_name="Marnie",
    searchable_by=["Marnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    effect=marnie,

)
