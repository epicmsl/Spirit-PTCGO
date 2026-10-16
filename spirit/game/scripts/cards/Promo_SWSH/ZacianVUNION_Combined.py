from spirit.game.data_utils import VUnionPokemonDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, Rarities

from spirit.game.card_effects.promo_swsh_effects import dance_of_the_crowned_sword, master_blade, union_gain

card = VUnionPokemonDef(
    guid="e38fcd86-6dc9-5bd7-98e2-0889e6ee1f2f",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianVUNION.Name",
    display_name="Zacian V-UNION",
    searchable_by=["Zacian V-UNION", "V-UNION", "ZacianVUNION"],
    collector_number=163,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    hp=320,
    elements=[PokemonTypes.METAL],
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        Attack(
            title="Union Gain",
            game_text="Attach up to 2 Metal Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=union_gain(PokemonTypes.METAL, 2),
        ),
        Attack(
            title="Dance of the Crowned Sword",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 150 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=dance_of_the_crowned_sword(150),
        ),
        Attack(
            title="Steel Cut",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
        ),
        Attack(
            title="Master Blade",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=340,
            effect=master_blade(3),
        ),
    ],
)
