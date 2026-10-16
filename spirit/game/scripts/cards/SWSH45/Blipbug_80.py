from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="efb98611-e6c2-5f63-8d70-aca8a6109241",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blipbug.Name",
    display_name="Blipbug",
    searchable_by=["Blipbug", "Basic", "Blipbug"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SWSH45",
    rarity=Rarities.Shining,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=824,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
