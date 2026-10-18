from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import g_max_volt_tackle

card = PokemonCardDef(
    guid="3df4ff62-8f92-5e44-a1d8-3cf8a027ba1d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVMAX.Name",
    display_name="Pikachu VMAX",
    searchable_by=["Pikachu VMAX", "VMAX", "PikachuVMAX"],
    subtypes=["VMAX"],
    collector_number=62,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVMAX,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    family_id=25,
    abilities=[
        Attack(
            title="G-Max Volt Tackle",
            game_text="You may discard all Energy from this Pok\u00e9mon. If you do, this attack does 150 more damage.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=120,
            damage_operator="+",
            effect=g_max_volt_tackle(150),
        ),
    ],
)
