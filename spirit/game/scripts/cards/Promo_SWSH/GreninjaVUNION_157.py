from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="f426f919-cb14-5064-930d-20e869ba9c75",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaVUNION.Name",
    display_name="Greninja V-UNION",
    searchable_by=["Greninja V-UNION", "V-UNION", "GreninjaVUNION"],
    collector_number=157,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/GreninjaVUNION_Combined",
    piece=VUnionPiece.BOTTOM_LEFT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
