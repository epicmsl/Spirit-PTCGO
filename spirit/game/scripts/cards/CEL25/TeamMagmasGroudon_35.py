from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import snipe_attack, bonus_if
from spirit.game.card_effects.cel25_effects import (
    power_saver_allows_attack, defender_has_two_counters,
)

card = PokemonCardDef(
    guid="1552560a-88a5-501f-aa1b-1625862566f2",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasGroudon.Name",
    display_name="Team Magma's Groudon",
    searchable_by=["Team Magma's Groudon", "Basic", "TeamMagmasGroudon"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Ability(
            title="Power Saver",
            game_text="As long as the number of Pok\u00e9mon in play (both yours and your opponent's) that has Team Magma in its name is 3 or less, Team Magma's Groudon can't attack.",
            ability_type=AbilityTypes.POKE_BODY,
        ),
        Attack(
            title="Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(20, pool="any"),
            condition=power_saver_allows_attack,
        ),
        Attack(
            title="Pulverize",
            game_text="If the Defending Pok\u00e9mon already has at least 2 damage counters on it, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=bonus_if(defender_has_two_counters, 20),
            condition=power_saver_allows_attack,
        ),
    ],
)
