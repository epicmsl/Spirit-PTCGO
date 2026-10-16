from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="9171290f-dc3c-533b-b780-96ce545360da",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    display_name="Cufant",
    searchable_by=["Cufant", "Basic", "Cufant"],
    subtypes=["Basic"],
    collector_number=163,
    set_code="SWSH45",
    rarity=Rarities.Shining,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=878,
    abilities=[
        Attack(
            title="Strength",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
