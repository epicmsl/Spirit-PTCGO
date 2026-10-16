from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import forest_feast, wood_hammer

card = PokemonCardDef(
    guid="63bcafa0-3053-5c09-8c49-86371bae82e6",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomV.Name",
    display_name="Rillaboom V",
    searchable_by=["Rillaboom V", "Basic", "V", "RillaboomV"],
    subtypes=["Basic", "V"],
    collector_number=14,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=812,
    abilities=[
        Attack(
            title="Forest Feast",
            game_text="Search your deck for up to 2 Basic Grass Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=forest_feast(),
        ),
        Attack(
            title="Wood Hammer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=wood_hammer(30),
        ),
    ],
)
