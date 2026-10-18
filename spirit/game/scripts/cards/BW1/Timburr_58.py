from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8cae0ea7-1f8b-50a3-ab05-5be8a0e93a29",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    display_name="Timburr",
    searchable_by=["Timburr", "Basic", "Timburr"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=532,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
