from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f86803d4-fb4a-5c03-9516-c89a4c9cbb4e",
    key="BW1",
    name="Basic Darkness Energy",
    display_name="Basic Darkness Energy",
    searchable_by=["Basic Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="BW1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
)
