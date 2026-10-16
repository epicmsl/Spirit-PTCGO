from spirit.game.data_utils import PokemonReprintCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = PokemonReprintCardDef(
    inherits="SWSH8/MewVMAX_114",
    guid="72b7e13f-0f90-50ba-992d-ac6ca731a25b",
    key="SWSH8",
    set_code="SWSH8",
    collector_number=268,
    rarity=Rarities.RareRainbow,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET])
)
