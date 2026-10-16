from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="da5a5e8c-f851-5081-ab4f-04c0977a3464",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVUNION.Name",
    display_name="Pikachu V-UNION",
    searchable_by=["Pikachu V-UNION", "V-UNION", "PikachuVUNION"],
    collector_number=141,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/PikachuVUNION_Combined",
    piece=VUnionPiece.BOTTOM_LEFT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
