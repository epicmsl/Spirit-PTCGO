from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a934a264-a8ad-5ab1-b6ec-aaa9e09b97a7",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    display_name="Scraggy",
    searchable_by=["Scraggy", "Basic", "Scraggy"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=559,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
