from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="c0a84655-e400-5793-8eeb-a9ba0b7985f2",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVUNION.Name",
    display_name="Pikachu V-UNION",
    searchable_by=["Pikachu V-UNION", "V-UNION", "PikachuVUNION"],
    collector_number=140,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/PikachuVUNION_Combined",
    piece=VUnionPiece.TOP_RIGHT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
