from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="12191812-96da-5e0d-99da-8b0ec08f2a53",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianVUNION.Name",
    display_name="Zacian V-UNION",
    searchable_by=["Zacian V-UNION", "V-UNION", "ZacianVUNION"],
    collector_number=166,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/ZacianVUNION_Combined",
    piece=VUnionPiece.BOTTOM_RIGHT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
