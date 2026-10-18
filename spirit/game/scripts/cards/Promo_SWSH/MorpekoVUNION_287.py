from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="5c20a166-a4e5-565f-9a25-8a37b5162752",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoVUNION.Name",
    display_name="Morpeko V-UNION",
    searchable_by=["Morpeko V-UNION", "V-UNION", "MorpekoVUNION"],
    collector_number=287,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/MorpekoVUNION_287_Combined",
    piece=VUnionPiece.TOP_LEFT,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
)
