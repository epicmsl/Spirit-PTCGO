from spirit.game.data_utils import EnergyCardDef, Foil
from spirit.game.attributes import PokemonTypes, Rarities, FoilMasks, FoilEffects

card = EnergyCardDef(
    guid="878d7668-c23f-5c93-8926-82c09b586edf",
    key="SWSH8",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=283,
    set_code="SWSH8",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET])
)
