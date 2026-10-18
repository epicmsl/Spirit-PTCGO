from spirit.game.data_utils import VUnionPokemonDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, Rarities

from spirit.game.card_effects.promo_swsh_effects import all_you_can_eat, burst_wheel, union_gain

card = VUnionPokemonDef(
    guid="22a6ffd3-9e5d-5bac-abef-25d47e789e5b",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoVUNION.Name",
    display_name="Morpeko V-UNION",
    searchable_by=["Morpeko V-UNION", "V-UNION", "MorpekoVUNION"],
    collector_number=287,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=877,
    abilities=[
        Attack(
            title="Union Gain",
            game_text="Attach up to 2 Lightning Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=union_gain(PokemonTypes.LIGHTNING, 2),
        ),
        Attack(
            title="All You Can Eat",
            game_text="Draw cards until you have 10 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=all_you_can_eat(10),
        ),
        Attack(
            title="Burst Wheel",
            game_text="Discard all Energy from this Pok\u00e9mon. This attack does 100 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="x",
            effect=burst_wheel(100),
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)
