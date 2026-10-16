from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import stone_edge

card = PokemonCardDef(
    guid="b070dd4c-5498-59f4-a12d-5d5b1bb4a6f2",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    display_name="Cranidos",
    searchable_by=["Cranidos", "Stage 1", "Cranidos"],
    subtypes=["Stage 1"],
    collector_number=274,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name",
    family_id=409,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Stone Edge",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
            damage_operator="+",
            effect=stone_edge(40),
        ),
    ],
)
