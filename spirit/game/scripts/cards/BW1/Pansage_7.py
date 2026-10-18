from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e9196ddc-cd3b-505e-bf2b-934a086c3fd7",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    display_name="Pansage",
    searchable_by=["Pansage", "Basic", "Pansage"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=511,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
