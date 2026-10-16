from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="ec0db785-405f-5b9f-a056-fb84b532f698",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaVUNION.Name",
    display_name="Greninja V-UNION",
    searchable_by=["Greninja V-UNION", "V-UNION", "GreninjaVUNION"],
    collector_number=155,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/GreninjaVUNION_Combined",
    piece=VUnionPiece.TOP_LEFT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
