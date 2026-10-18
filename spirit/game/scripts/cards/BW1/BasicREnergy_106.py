from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="148bd56e-a7b5-5173-b66b-f2c66cb69407",
    key="BW1",
    name="Basic Fire Energy",
    display_name="Basic Fire Energy",
    searchable_by=["Basic Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="BW1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
)
