from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4f4b282c-7fe1-5ea3-8c9e-0029015c383e",
    key="BW1",
    name="Basic Lightning Energy",
    display_name="Basic Lightning Energy",
    searchable_by=["Basic Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="BW1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
)
