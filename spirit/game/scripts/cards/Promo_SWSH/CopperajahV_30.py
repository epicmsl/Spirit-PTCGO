from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import adamantine_press

card = PokemonCardDef(
    guid="34b12004-2234-57c5-9b2b-63c6969fed0c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CopperajahV.Name",
    display_name="Copperajah V",
    searchable_by=["Copperajah V", "Basic", "V", "CopperajahV"],
    subtypes=["Basic", "V"],
    collector_number=30,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=879,
    abilities=[
        Attack(
            title="Adamantine Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=adamantine_press(30),
        ),
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)
