from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="18398643-e625-5576-b6d6-c34a9701e1da",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawk.Name",
    display_name="Sawk",
    searchable_by=["Sawk", "Basic", "Sawk"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=539,
    abilities=[
        Attack(
            title="Low Sweep",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Beatdown",
            cost={PokemonTypes.FIGHTING: 2},
            damage=40,
        ),
    ],
)
