from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import metal_coating

card = PokemonCardDef(
    guid="15d3d2fa-19e0-53d7-82c7-8d394a8b68db",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormeDialgaV.Name",
    display_name="Origin Forme Dialga V",
    searchable_by=["Origin Forme Dialga V", "Basic", "V", "OriginFormeDialgaV"],
    subtypes=["Basic", "V"],
    collector_number=255,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=483,
    abilities=[
        Attack(
            title="Metal Coating",
            game_text="Attach up to 2 Metal Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=metal_coating(2),
        ),
        Attack(
            title="Temporal Rupture",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)
