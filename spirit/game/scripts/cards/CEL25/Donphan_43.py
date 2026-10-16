from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="b8dea235-261f-53b4-8919-563b1841bed4",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1", "Donphan"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="CEL25",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="Any damage done to Donphan by attacks is reduced by 20 (after applying Weakness and Resistance).",
            passive=takes_less_passive(20),
        ),
        Attack(
            title="Earthquake",
            game_text="Does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=spread_damage(10, side="mine", also_base=True),
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.FIGHTING: 3},
            damage=90,
        ),
    ],
)
