from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8b421453-dd57-57eb-b078-b6636a6e3045",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name",
    display_name="Venipede",
    searchable_by=["Venipede", "Basic", "Venipede"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=543,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
