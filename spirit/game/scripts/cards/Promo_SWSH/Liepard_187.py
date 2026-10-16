from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import trade

card = PokemonCardDef(
    guid="57e78ddb-d7bf-57c0-b2c3-60e45840f473",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1", "Liepard"],
    subtypes=["Stage 1"],
    collector_number=187,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Ability(
            title="Trade",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.",
            effect=trade(2),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
