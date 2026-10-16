from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import solar_shot, tantrum_blast

card = PokemonCardDef(
    guid="ad9497eb-8381-5aa5-94c6-adf1f910b071",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianElectrodeV.Name",
    display_name="Hisuian Electrode V",
    searchable_by=["Hisuian Electrode V", "Basic", "V", "HisuianElectrodeV"],
    subtypes=["Basic", "V"],
    collector_number=294,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=101,
    abilities=[
        Attack(
            title="Tantrum Blast",
            game_text="This attack does 100 damage for each Special Condition affecting this Pok\u00e9mon.",
            cost={},
            damage=100,
            damage_operator="x",
            effect=tantrum_blast(100),
        ),
        Attack(
            title="Solar Shot",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=solar_shot(),
        ),
    ],
)
