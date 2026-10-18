from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c8bfe3cd-c345-5e34-90e8-7d7e97b59990",
    key="BW1",
    name="Basic Metal Energy",
    display_name="Basic Metal Energy",
    searchable_by=["Basic Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="BW1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False,
)
