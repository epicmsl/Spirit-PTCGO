from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import basket_crash, shadow_slash

card = PokemonCardDef(
    guid="541a0e72-07e8-553a-8847-fb28b701d822",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSamurottV.Name",
    display_name="Hisuian Samurott V",
    searchable_by=["Hisuian Samurott V", "Basic", "V", "HisuianSamurottV"],
    subtypes=["Basic", "V"],
    collector_number=239,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=503,
    abilities=[
        Attack(
            title="Basket Crash",
            game_text="Discard up to 2 Pok\u00e9mon Tools from your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=basket_crash(2),
        ),
        Attack(
            title="Shadow Slash",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=180,
            effect=shadow_slash(),
        ),
    ],
)
