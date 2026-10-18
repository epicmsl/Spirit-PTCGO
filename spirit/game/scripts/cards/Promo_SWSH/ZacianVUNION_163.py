from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="e0b9bee8-fa93-52f8-bdbb-6db52f2534c2",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianVUNION.Name",
    display_name="Zacian V-UNION",
    searchable_by=["Zacian V-UNION", "V-UNION", "ZacianVUNION"],
    collector_number=163,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/ZacianVUNION_Combined",
    piece=VUnionPiece.TOP_LEFT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
