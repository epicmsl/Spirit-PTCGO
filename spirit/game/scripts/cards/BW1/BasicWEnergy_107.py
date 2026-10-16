from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="464b9020-ae17-578e-aca0-936afefd805a",
    key="BW1",
    name="Basic Water Energy",
    display_name="Basic Water Energy",
    searchable_by=["Basic Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="BW1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False,
)
