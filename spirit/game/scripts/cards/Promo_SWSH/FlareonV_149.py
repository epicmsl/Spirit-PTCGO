from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import flaming_breath, scorching_column

card = PokemonCardDef(
    guid="65580701-beb4-59de-8a3f-51333dcaf42a",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonV.Name",
    display_name="Flareon V",
    searchable_by=["Flareon V", "Basic", "V", "FlareonV"],
    subtypes=["Basic", "V"],
    collector_number=149,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=136,
    abilities=[
        Attack(
            title="Flaming Breath",
            game_text="Search your deck for a Fire Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flaming_breath(),
        ),
        Attack(
            title="Scorching Column",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=scorching_column(),
        ),
    ],
)
