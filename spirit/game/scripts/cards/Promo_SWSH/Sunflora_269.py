from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import bright_beam

card = PokemonCardDef(
    guid="e02f41ae-8d0d-5916-9a11-6404bf4cd6ad",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunflora.Name",
    display_name="Sunflora",
    searchable_by=["Sunflora", "Stage 1", "Sunflora"],
    subtypes=["Stage 1"],
    collector_number=269,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    family_id=191,
    abilities=[
        Attack(
            title="Bright Beam",
            game_text="You may discard up to 3 Energy cards from your hand. This attack does 70 more damage for each card you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=bright_beam(70, 3),
        ),
    ],
)
