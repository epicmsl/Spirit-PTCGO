from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.content.definitions import Activations
from spirit.game.card_effects.cel25_effects import (
    imprison, imprison_condition, flame_ball,
)

card = PokemonCardDef(
    guid="b28a3bb7-e95f-57b9-b78b-6d5b8732a49a",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoirex.Name",
    display_name="Gardevoir ex",
    searchable_by=["Gardevoir ex", "Stage 2", "EX", "Gardevoirex"],
    subtypes=["Stage 2", "EX"],
    collector_number=38,
    set_code="CEL25",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Imprison",
            game_text="Once during your turn if Gardevoir ex is your Active Pok\u00e9mon, you may put an Imprison marker on 1 of your opponent's Pok\u00e9mon. Any Pok\u00e9mon that has any Imprison markers on it can't use any Poké-Powers or Poké-Bodies. This power can't be used if Gardevoir ex is affected by a Special Condition.",
            effect=imprison,
            activation=Activations.ONCE_PER_TURN,
            condition=imprison_condition,
        ),
        Attack(
            title="Flame Ball",
            game_text="You may move a  Energy card attached to Gardevoir ex to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=flame_ball,
        ),
    ],
)
