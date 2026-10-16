from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import close_quarters_shooting, mountain_hunt

card = PokemonCardDef(
    guid="035b2cf2-9705-58f4-83ee-04f3d00be93d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianDecidueyeV.Name",
    display_name="Hisuian Decidueye V",
    searchable_by=["Hisuian Decidueye V", "Basic", "V", "HisuianDecidueyeV"],
    subtypes=["Basic", "V"],
    collector_number=238,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=724,
    abilities=[
        Attack(
            title="Mountain Hunt",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=mountain_hunt(2),
        ),
        Attack(
            title="Close-Quarters Shooting",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=close_quarters_shooting(),
        ),
    ],
)
