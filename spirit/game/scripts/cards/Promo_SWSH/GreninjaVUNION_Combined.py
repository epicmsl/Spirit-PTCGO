from spirit.game.data_utils import VUnionPokemonDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, Rarities, SpecialConditions

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import jaw_lock, union_gain, feel_the_way
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.passives_common import condition_immunity_passive, trainer_effect_shield_passive

card = VUnionPokemonDef(
    guid="091c995e-cd5e-5786-8e09-8aadb210e04b",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaVUNION.Name",
    display_name="Greninja V-UNION",
    searchable_by=["Greninja V-UNION", "V-UNION", "GreninjaVUNION"],
    collector_number=155,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.WATER],
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=658,
    abilities=[
        Ability(
            title="Ninja Body",
            game_text="Whenever your opponent plays an Item card from their hand, prevent all effects of that card done to this Pok\u00e9mon.",
            effect=trainer_effect_shield_passive(supporters_only=False),
            passive=trainer_effect_shield_passive(supporters_only=False),
        ),
        Ability(
            title="Antidote Jutsu",
            game_text="This Pok\u00e9mon can't be Poisoned.",
            effect=condition_immunity_passive([SpecialConditions.POISONED]),
            passive=condition_immunity_passive([SpecialConditions.POISONED]),
        ),
        Ability(
            title="Feel the Way",
            game_text="Once during your turn, you may have your opponent reveal their hand.",
            effect=feel_the_way(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Union Gain",
            game_text="Attach up to 2 Water Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=union_gain(PokemonTypes.WATER, 2),
        ),
        Attack(
            title="Aqua Edge",
            cost={PokemonTypes.WATER: 1},
            damage=130,
        ),
        Attack(
            title="Twister Shuriken",
            game_text="This attack does 100 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=spread_damage(100, side="opponent"),
        ),
        Attack(
            title="Waterfall Bind",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=jaw_lock(),
        ),
    ],
)
