from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ec76b1b4-3bcd-5ec2-a13d-88951cbf1c10",
    key="BW1",
    name="Basic Psychic Energy",
    display_name="Basic Psychic Energy",
    searchable_by=["Basic Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="BW1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
)
