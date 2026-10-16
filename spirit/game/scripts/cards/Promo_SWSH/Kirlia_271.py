from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import refinement

card = PokemonCardDef(
    guid="c6375d96-74eb-5773-b0e6-58732369ad88",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=["Kirlia", "Stage 1", "Kirlia"],
    subtypes=["Stage 1"],
    collector_number=271,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Refinement",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.",
            effect=refinement(2),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Slap",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
