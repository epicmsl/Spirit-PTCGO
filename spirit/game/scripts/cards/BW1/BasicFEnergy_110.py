from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="20432453-c1af-5374-987e-eb5afa86543d",
    key="BW1",
    name="Basic Fighting Energy",
    display_name="Basic Fighting Energy",
    searchable_by=["Basic Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="BW1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
)
