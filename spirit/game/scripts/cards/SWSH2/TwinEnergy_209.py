from spirit.game.card_effects.energies import TWIN_ENERGY
from spirit.game.data_utils import EnergyCardDef, Foil
from spirit.game.attributes import PokemonTypes, Rarities, FoilMasks, FoilEffects

card = EnergyCardDef(
    guid="96dbb5dc-bb45-5d47-8d18-dc27698b75a3",
    key="SWSH2",
    name="Twin Energy",
    display_name="Twin Energy",
    searchable_by=["Twin Energy", "Special"],
    subtypes=["Special"],
    collector_number=209,
    set_code="SWSH2",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=TWIN_ENERGY,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET])
)
