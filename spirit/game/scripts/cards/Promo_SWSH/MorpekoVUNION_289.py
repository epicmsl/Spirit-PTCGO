from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="e3d8b931-79dc-5232-af1b-0facf1ddde48",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoVUNION.Name",
    display_name="Morpeko V-UNION",
    searchable_by=["Morpeko V-UNION", "V-UNION", "MorpekoVUNION"],
    collector_number=289,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/MorpekoVUNION_287_Combined",
    piece=VUnionPiece.BOTTOM_LEFT,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
)
