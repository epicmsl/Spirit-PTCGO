from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import mad_party, shuffle_dance

card = PokemonCardDef(
    guid="50bf5b76-bd5e-5ecf-ae7a-3c05e2c9c9ba",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrRime.Name",
    display_name="Galarian Mr. Rime",
    searchable_by=["Galarian Mr. Rime", "Stage 1", "GalarianMrRime"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrMime.Name",
    family_id=122,
    abilities=[
        Ability(
            title="Shuffle Dance",
            game_text="Once during your turn, you may switch 1 of your opponent's face-down Prize cards with the top card of their deck. (The cards stay face down.)",
            effect=shuffle_dance(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Mad Party",
            game_text="This attack does 20 damage for each Pok\u00e9mon in your discard pile that has the Mad Party attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=mad_party(20),
        ),
    ],
)
