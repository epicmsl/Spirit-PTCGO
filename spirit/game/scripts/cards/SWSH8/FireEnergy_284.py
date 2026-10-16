from spirit.game.data_utils import EnergyCardDef, Foil
from spirit.game.attributes import PokemonTypes, Rarities, FoilMasks, FoilEffects

card = EnergyCardDef(
    guid="8400e63d-1af3-51d4-861e-cebeaaaea92d",
    key="SWSH8",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=284,
    set_code="SWSH8",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET])
)
