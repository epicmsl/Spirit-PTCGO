from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = VUnionPieceCardDef(
    guid="86c7a8b8-e64b-5be5-9128-cc8d6cc859ae",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVUNION.Name",
    display_name="Pikachu V-UNION",
    searchable_by=["Pikachu V-UNION", "V-UNION", "PikachuVUNION"],
    collector_number=142,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/PikachuVUNION_Combined",
    piece=VUnionPiece.BOTTOM_RIGHT,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
)
