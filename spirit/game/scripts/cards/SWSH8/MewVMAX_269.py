from spirit.game.data_utils import PokemonReprintCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = PokemonReprintCardDef(
    inherits="SWSH8/MewVMAX_114",
    guid="c7bbdd12-2615-5812-97c3-4560a7c991bc",
    key="SWSH8",
    set_code="SWSH8",
    collector_number=269,
    rarity=Rarities.RareRainbow,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET])
)
