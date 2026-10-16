from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="6684196a-1ec6-5b75-910b-54fa77b8bae8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianVUNION.Name",
    display_name="Zacian V-UNION",
    searchable_by=["Zacian V-UNION", "V-UNION", "ZacianVUNION"],
    collector_number=165,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/ZacianVUNION_Combined",
    piece=VUnionPiece.BOTTOM_LEFT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
