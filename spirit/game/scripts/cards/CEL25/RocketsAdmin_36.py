from spirit.game.data_utils import SupporterCardDef, unimplemented, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.cel25_effects import rockets_admin

card = SupporterCardDef(
    guid="6e24f934-9020-5b13-be85-18a010ca3a62",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsAdmin.Name",
    display_name="Rocket's Admin.",
    searchable_by=["Rocket's Admin.", "Supporter"],
    subtypes=["Supporter"],
    collector_number=36,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    effect=rockets_admin,
)
