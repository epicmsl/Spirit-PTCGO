from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ace3a155-78c4-5904-9c91-eb0e212c9777",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    display_name="Timburr",
    searchable_by=["Timburr", "Basic", "Timburr"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=532,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
