from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import mad_party, tea_break

card = PokemonCardDef(
    guid="29c43a05-1eb1-5e7a-ae4f-da6107e4b267",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Polteageist.Name",
    display_name="Polteageist",
    searchable_by=["Polteageist", "Stage 1", "Polteageist"],
    subtypes=["Stage 1"],
    collector_number=81,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name",
    family_id=854,
    abilities=[
        Ability(
            title="Tea Break",
            game_text="You must discard a Pok\u00e9mon that has the Mad Party attack from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.",
            effect=tea_break(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Mad Party",
            game_text="This attack does 20 damage for each Pok\u00e9mon in your discard pile that has the Mad Party attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=mad_party(20),
        ),
    ],
)
