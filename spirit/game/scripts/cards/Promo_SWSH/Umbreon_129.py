from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import blindside, moon_mirage

card = PokemonCardDef(
    guid="f2332dfc-33b0-5f90-ba19-85aafa62b0b2",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Umbreon"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Blindside",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=blindside(60),
        ),
        Attack(
            title="Moon Mirage",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=moon_mirage(),
        ),
    ],
)
