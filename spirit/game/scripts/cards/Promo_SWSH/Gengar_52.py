from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import hypnoblast, life_shaker

card = PokemonCardDef(
    guid="3550e902-e4f9-5ba1-83ca-b7d4845b74d3",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Life Shaker",
            game_text="As often as you like during your turn, you may move 1 damage counter from 1 of your Psychic Pok\u00e9mon to another of your Psychic Pok\u00e9mon.",
            effect=life_shaker(),
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=hypnoblast(),
        ),
    ],
)
