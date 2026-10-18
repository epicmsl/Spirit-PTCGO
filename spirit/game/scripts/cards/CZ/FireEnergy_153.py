from spirit.game.data_utils import EnergyCardDef, Foil
from spirit.game.attributes import PokemonTypes, Rarities, FoilMasks, FoilEffects

card = EnergyCardDef(
    guid="7dd9ffa9-c951-57de-a48b-e8b1a551ebb5",
    key="CZ",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=153,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
