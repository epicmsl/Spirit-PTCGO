from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="1f721a13-093f-5732-9277-6e8e3a11c68c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    display_name="Squirtle",
    searchable_by=["Squirtle", "Basic", "Squirtle"],
    subtypes=["Basic"],
    collector_number=233,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=7,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
