from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.content.definitions import Triggers
from spirit.game.card_effects.cel25_effects import (
    healing_breath, dragon_rush,
)

card = PokemonCardDef(
    guid="2cb1f44b-dfae-5a55-9657-5728b7ab7477",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompC.Name",
    display_name="Garchomp C",
    searchable_by=["Garchomp C", "Restore", "GarchompC"],
    subtypes=["Restore"],
    collector_number=42,
    set_code="CEL25",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.RESTORED,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompC.Name",
    family_id=443,
    abilities=[
        Ability(
            title="Healing Breath",
            game_text="Once during your turn when you put Garchomp C LV.X from your hand onto your Active Garchomp C, you may remove all damage counters from each of your Pok\u00e9mon SP.",
            effect=healing_breath,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Dragon Rush",
            game_text="Discard 2 Energy attached to Garchomp C. Choose 1 of your opponent's Pok\u00e9mon. This attack does 80 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Garchomp C can't use Dragon Rush during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=dragon_rush,
            locks_next_turn=True,
        ),
    ],
)
