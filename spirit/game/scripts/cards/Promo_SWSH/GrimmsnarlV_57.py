from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import spiky_knuckle

card = PokemonCardDef(
    guid="59aa2f0b-050e-5780-9cd6-a1134fbc6828",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlV.Name",
    display_name="Grimmsnarl V",
    searchable_by=["Grimmsnarl V", "Basic", "V", "GrimmsnarlV"],
    subtypes=["Basic", "V"],
    collector_number=57,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=861,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
        ),
        Attack(
            title="Spiky Knuckle",
            game_text="Put 2 Darkness Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=200,
            effect=spiky_knuckle(2),
        ),
    ],
)
