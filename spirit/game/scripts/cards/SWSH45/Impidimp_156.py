from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="ef982c88-e28b-512d-ba2f-a0abac1700a8",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name",
    display_name="Impidimp",
    searchable_by=["Impidimp", "Basic", "Impidimp"],
    subtypes=["Basic"],
    collector_number=156,
    set_code="SWSH45",
    rarity=Rarities.Shining,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=859,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Stampede",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
