from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="b9f5a701-3323-58da-bc20-f5e0fafd73ae",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    display_name="Tepig",
    searchable_by=["Tepig", "Basic", "Tepig"],
    subtypes=["Basic"],
    collector_number=172,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=498,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
