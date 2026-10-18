from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.content.definitions import Activations
from spirit.game.card_effects.cel25_effects import (
    cosmic_power, cosmic_power_condition,
)

card = PokemonCardDef(
    guid="afcdf4a5-08ae-59af-bbda-f9569241140e",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Ability(
            title="Cosmic Power",
            game_text="Once during your turn you may choose up to 2 cards from your hand and put them on the bottom of your deck in any order. If you do, draw cards until you have 6 cards in your hand. This power can't be used if Claydol is affected by a Special Condition.",
            effect=cosmic_power,
            activation=Activations.ONCE_PER_TURN,
            condition=cosmic_power_condition,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
