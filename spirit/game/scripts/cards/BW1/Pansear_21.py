from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f696c651-655e-5fd8-9742-f0e52067db05",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    display_name="Pansear",
    searchable_by=["Pansear", "Basic", "Pansear"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=513,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
