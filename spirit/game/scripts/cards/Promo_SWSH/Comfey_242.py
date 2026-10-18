from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.card_effects.promo_swsh_effects import in_active_spot_condition
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.pokemon import flower_selecting

card = PokemonCardDef(
    guid="ab064671-98a6-5675-b16f-5fab189758ca",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Comfey.Name",
    display_name="Comfey",
    searchable_by=["Comfey", "Basic", "Comfey"],
    subtypes=["Basic"],
    collector_number=242,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=764,
    abilities=[
        Ability(
            title="Flower Selecting",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may look at the top 2 cards of your deck and put 1 of them into your hand. Put the other card in the Lost Zone.",
            effect=flower_selecting,
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot_condition,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
