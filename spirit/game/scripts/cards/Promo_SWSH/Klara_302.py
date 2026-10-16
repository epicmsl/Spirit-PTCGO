from spirit.game.data_utils import SupporterCardDef, unimplemented, Foil
from spirit.game.card_effects.trainers import klara, has_pokemon_or_basic_energy_in_discard
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="c6c8170b-d536-50e5-991f-4795a3eedfeb",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Klara.Name",
    display_name="Klara",
    searchable_by=["Klara", "Supporter"],
    subtypes=["Supporter"],
    collector_number=302,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    effect=klara,

)
