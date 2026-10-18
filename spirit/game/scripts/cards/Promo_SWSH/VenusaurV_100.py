from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import double_edge, leaf_drain

card = PokemonCardDef(
    guid="760779d2-56c5-58ad-add2-919564b0de4d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurV.Name",
    display_name="Venusaur V",
    searchable_by=["Venusaur V", "Basic", "V", "VenusaurV"],
    subtypes=["Basic", "V"],
    collector_number=100,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Attack(
            title="Leaf Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=leaf_drain(30),
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=double_edge(30),
        ),
    ],
)
