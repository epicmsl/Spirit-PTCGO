from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.content.definitions import Activations
from spirit.game.card_effects.cel25_effects import (
    energy_trans, energy_trans_condition,
)

card = PokemonCardDef(
    guid="7abec8cd-0633-51cf-bf24-ba1ad42d58df",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=27,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Energy Trans",
            game_text="As often as you like during your turn you may take 1 Grass Energy card attached to 1 of your Pok\u00e9mon and attach it to a different one. This power can't be used if Venusaur is Asleep, Confused, or Paralyzed.",
            effect=energy_trans,
            activation=Activations.UNLIMITED,
            condition=energy_trans_condition,
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 4},
            damage=60,
        ),
    ],
)
