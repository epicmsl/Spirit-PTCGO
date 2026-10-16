from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="79816372-a772-552f-be72-de59fd39bd82",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVUNION.Name",
    display_name="Pikachu V-UNION",
    searchable_by=["Pikachu V-UNION", "V-UNION", "PikachuVUNION"],
    collector_number=139,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/PikachuVUNION_Combined",
    piece=VUnionPiece.TOP_LEFT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
