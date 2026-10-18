from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="85b9273e-8478-54b2-9572-6f6886794bff",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaVUNION.Name",
    display_name="Greninja V-UNION",
    searchable_by=["Greninja V-UNION", "V-UNION", "GreninjaVUNION"],
    collector_number=158,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/GreninjaVUNION_Combined",
    piece=VUnionPiece.BOTTOM_RIGHT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
