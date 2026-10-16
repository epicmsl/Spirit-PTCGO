from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.promo_swsh_effects import rampaging_kick

card = PokemonCardDef(
    guid="5d76fa18-b3ec-5bac-b278-1069882efe11",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianObstagoon.Name",
    display_name="Galarian Obstagoon",
    searchable_by=["Galarian Obstagoon", "Stage 2", "GalarianObstagoon"],
    subtypes=["Stage 2"],
    collector_number=193,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianLinoone.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Rampaging Kick",
            game_text="Discard 2 Darkness Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=rampaging_kick(2),
        ),
    ],
)
