from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import netherworld_gate, screaming_circle

card = PokemonCardDef(
    guid="7d57b2c9-c0b5-594f-a957-95109911056d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=241,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Netherworld Gate",
            game_text="Once during your turn, if this Pok\u00e9mon is in your discard pile, you may put it onto your Bench. If you do, put 3 damage counters on this Pok\u00e9mon.",
            effect=netherworld_gate(),
            usable_from="discard",
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Screaming Circle",
            game_text="Put 2 damage counters on your opponent's Active Pok\u00e9mon for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=screaming_circle(2),
        ),
    ],
)
