from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import oceanic_accompaniment

card = PokemonCardDef(
    guid="010b2ba2-9c2f-5e51-a8f3-1b6b5984cb4d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name",
    display_name="Finneon",
    searchable_by=["Finneon", "Basic", "Finneon"],
    subtypes=["Basic"],
    collector_number=240,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=456,
    abilities=[
        Ability(
            title="Oceanic Accompaniment",
            game_text="As often as you like during your turn, you may attach a Water Energy card from your hand to 1 of your Pok\u00e9mon that has the Swim Freely attack.",
            effect=oceanic_accompaniment(),
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
