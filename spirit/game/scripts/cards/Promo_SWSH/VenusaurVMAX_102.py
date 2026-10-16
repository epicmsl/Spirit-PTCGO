from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import forest_storm, g_max_bloom

card = PokemonCardDef(
    guid="b534d1d4-38fe-531a-889e-ba2167e5ae41",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurVMAX.Name",
    display_name="Venusaur VMAX",
    searchable_by=["Venusaur VMAX", "VMAX", "VenusaurVMAX"],
    subtypes=["VMAX"],
    collector_number=102,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVMAX,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurV.Name",
    family_id=3,
    abilities=[
        Attack(
            title="Forest Storm",
            game_text="This attack does 30 damage for each Grass Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=forest_storm(30),
        ),
        Attack(
            title="G-Max Bloom",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=210,
            effect=g_max_bloom(30),
        ),
    ],
)
