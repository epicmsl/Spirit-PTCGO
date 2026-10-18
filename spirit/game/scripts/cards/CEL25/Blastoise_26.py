from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.content.definitions import Activations
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.card_effects.cel25_effects import (
    rain_dance, rain_dance_condition, hydro_pump_count,
)

card = PokemonCardDef(
    guid="bbb9a256-c35f-545e-9eda-a6c707c9b29a",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Rain Dance",
            game_text="As often as you like during your turn you may attach 1 Water Energy card to 1 of your Water Pok\u00e9mon. (This doesn't use up your 1 Energy card attachment for the turn.) This power can't be used if Blastoise is Asleep, Confused, or Paralyzed.",
            effect=rain_dance,
            activation=Activations.UNLIMITED,
            condition=rain_dance_condition,
        ),
        Attack(
            title="Hydro Pump",
            game_text="Does 40 damage plus 10 more damage for each Water Energy attached to Blastoise but not used to pay for this attack's Energy cost. Extra Water Energy after the 2nd doesn't count.",
            cost={PokemonTypes.WATER: 3},
            damage=40,
            damage_operator="+",
            effect=damage_per(hydro_pump_count, per=10, base=40, cap=60),
        ),
    ],
)
