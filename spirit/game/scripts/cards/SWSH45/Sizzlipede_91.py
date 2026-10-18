from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="62291d9b-f490-5f42-a93f-aa01b629c8e7",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    display_name="Sizzlipede",
    searchable_by=["Sizzlipede", "Basic", "Sizzlipede"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SWSH45",
    rarity=Rarities.Shining,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=850,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
