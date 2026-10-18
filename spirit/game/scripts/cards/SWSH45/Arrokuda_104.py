from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="ec0ce3dc-f9cc-590c-82b5-ad32499f9296",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    display_name="Arrokuda",
    searchable_by=["Arrokuda", "Basic", "Arrokuda"],
    subtypes=["Basic"],
    collector_number=104,
    set_code="SWSH45",
    rarity=Rarities.Shining,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=846,
    abilities=[
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
