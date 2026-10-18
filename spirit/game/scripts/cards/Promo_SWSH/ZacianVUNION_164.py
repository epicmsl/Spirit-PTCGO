from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="0d512767-0752-542e-8a15-2394278f64d3",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianVUNION.Name",
    display_name="Zacian V-UNION",
    searchable_by=["Zacian V-UNION", "V-UNION", "ZacianVUNION"],
    collector_number=164,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/ZacianVUNION_Combined",
    piece=VUnionPiece.TOP_RIGHT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
