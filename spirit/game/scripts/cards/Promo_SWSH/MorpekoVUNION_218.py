from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="1ec56d17-7f62-51e9-ab9d-1a7f81392ca4",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoVUNION.Name",
    display_name="Morpeko V-UNION",
    searchable_by=["Morpeko V-UNION", "V-UNION", "MorpekoVUNION"],
    collector_number=218,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/MorpekoVUNION_Combined",
    piece=VUnionPiece.BOTTOM_RIGHT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
