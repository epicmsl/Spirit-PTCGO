from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import emerald_blade, verdant_wind

card = PokemonCardDef(
    guid="49ec0107-12b4-5813-a113-58aef8fe4d1a",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VirizionV.Name",
    display_name="Virizion V",
    searchable_by=["Virizion V", "Basic", "V", "VirizionV"],
    subtypes=["Basic", "V"],
    collector_number=295,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=640,
    abilities=[
        Ability(
            title="Verdant Wind",
            game_text="Each of your Pok\u00e9mon that has any Grass Energy attached recovers from all Special Conditions and can't be affected by any Special Conditions.",
            effect=verdant_wind(),
            passive=verdant_wind(),
        ),
        Attack(
            title="Emerald Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=emerald_blade(),
            locks_next_turn=True,
        ),
    ],
)
