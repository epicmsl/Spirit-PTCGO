from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4d99014d-2004-51d0-8fe9-6b38c5e614fa",
    key="BW1",
    name="Basic Grass Energy",
    display_name="Basic Grass Energy",
    searchable_by=["Basic Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="BW1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
)
