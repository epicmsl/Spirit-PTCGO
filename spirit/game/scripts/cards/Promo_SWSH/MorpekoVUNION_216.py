from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="555e4208-8874-5f48-a1f9-693ce4fe2087",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoVUNION.Name",
    display_name="Morpeko V-UNION",
    searchable_by=["Morpeko V-UNION", "V-UNION", "MorpekoVUNION"],
    collector_number=216,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/MorpekoVUNION_Combined",
    piece=VUnionPiece.TOP_RIGHT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
