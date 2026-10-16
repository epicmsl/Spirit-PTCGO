from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="a6d56f5b-9f17-5430-9e38-d71a799c6204",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name",
    display_name="Chewtle",
    searchable_by=["Chewtle", "Basic", "Chewtle"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SWSH45",
    rarity=Rarities.Shining,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=833,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
