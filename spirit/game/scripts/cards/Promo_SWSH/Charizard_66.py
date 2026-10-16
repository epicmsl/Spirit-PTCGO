from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import battle_sense, royal_blaze

card = PokemonCardDef(
    guid="0c043e4b-bbbb-5515-b34f-32d4b181c38e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=66,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Battle Sense",
            game_text="Once during your turn, you may look at the top 3 cards of your deck and put 1 of them into your hand. Discard the other cards.",
            effect=battle_sense(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Royal Blaze",
            game_text="This attack does 50 more damage for each Leon card in your discard pile.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            damage_operator="+",
            effect=royal_blaze(50),
        ),
    ],
)
