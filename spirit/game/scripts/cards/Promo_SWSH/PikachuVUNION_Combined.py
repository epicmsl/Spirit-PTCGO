from spirit.game.data_utils import VUnionPokemonDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, Rarities

from spirit.game.card_effects.promo_swsh_effects import disconnect, shocking_shock, union_gain

card = VUnionPokemonDef(
    guid="c199b1ca-436e-5355-a3f6-0e15c14d0bb7",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVUNION.Name",
    display_name="Pikachu V-UNION",
    searchable_by=["Pikachu V-UNION", "V-UNION", "PikachuVUNION"],
    collector_number=139,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.LIGHTNING],
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Union Gain",
            game_text="Attach up to 2 Lightning Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=union_gain(PokemonTypes.LIGHTNING, 2),
        ),
        Attack(
            title="Shocking Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=shocking_shock(),
        ),
        Attack(
            title="Disconnect",
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=disconnect(),
        ),
        Attack(
            title="Electro Ball Together",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=250,
        ),
    ],
)
