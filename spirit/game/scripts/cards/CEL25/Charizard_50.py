from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.content.definitions import Activations
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.cel25_effects import (
    energy_burn, energy_burn_condition,
)

card = PokemonCardDef(
    guid="82f75c89-d7a4-5266-ba2c-31b9f42bd37b",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=50,
    set_code="CEL25",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Energy Burn",
            game_text="As often as you like during your turn you may turn all Energy attached to Charizard into Fire Energy for the rest of the turn. This power can't be used if Charizard is Asleep, Confused, or Paralyzed.",
            effect=energy_burn,
            activation=Activations.UNLIMITED,
            condition=energy_burn_condition,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy cards attached to Charizard in order to use this attack.",
            cost={PokemonTypes.FIRE: 4},
            damage=100,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)
