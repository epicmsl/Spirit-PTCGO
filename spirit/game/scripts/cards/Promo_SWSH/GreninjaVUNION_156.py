from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="941769b8-57e0-5d29-ab49-0d09cafe41a9",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaVUNION.Name",
    display_name="Greninja V-UNION",
    searchable_by=["Greninja V-UNION", "V-UNION", "GreninjaVUNION"],
    collector_number=156,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/GreninjaVUNION_Combined",
    piece=VUnionPiece.TOP_RIGHT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
