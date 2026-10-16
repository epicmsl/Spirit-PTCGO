from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import water_reserve

card = PokemonCardDef(
    guid="db2c9841-4be8-56de-b14d-0d4444b1a1e8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=226,
    abilities=[
        Attack(
            title="Water Reserve",
            game_text="Search your deck for up to 3 Water Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=water_reserve(),
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 2},
            damage=60,
        ),
    ],
)
