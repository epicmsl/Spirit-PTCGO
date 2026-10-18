from spirit.game.data_utils import EnergyCardDef, Foil
from spirit.game.attributes import PokemonTypes, Rarities, FoilMasks, FoilEffects

card = EnergyCardDef(
    guid="01be5a40-384d-5e6c-b9ac-dc0a1d10a6fb",
    key="CZ",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=158,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
