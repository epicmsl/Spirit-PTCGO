from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import extrasensory, hurried_gait

card = PokemonCardDef(
    guid="b46a6e99-772c-5aaf-9924-a67026d47b91",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wyrdeer.Name",
    display_name="Wyrdeer",
    searchable_by=["Wyrdeer", "Stage 1", "Wyrdeer"],
    subtypes=["Stage 1"],
    collector_number=206,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    family_id=234,
    abilities=[
        Ability(
            title="Hurried Gait",
            game_text="Once during your turn, you may draw a card.",
            effect=hurried_gait(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=extrasensory(80),
        ),
    ],
)
