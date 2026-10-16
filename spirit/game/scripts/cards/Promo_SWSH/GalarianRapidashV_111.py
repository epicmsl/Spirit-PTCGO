from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import libra_horn, psychic

card = PokemonCardDef(
    guid="be145439-675f-544b-9aaa-8705875ac0be",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianRapidashV.Name",
    display_name="Galarian Rapidash V",
    searchable_by=["Galarian Rapidash V", "Basic", "V", "GalarianRapidashV"],
    subtypes=["Basic", "V"],
    collector_number=111,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=78,
    abilities=[
        Attack(
            title="Libra Horn",
            game_text="Put damage counters on 1 of your opponent's Pok\u00e9mon until its remaining HP is 100.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=libra_horn(100),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=60,
            damage_operator="+",
            effect=psychic(30),
        ),
    ],
)
