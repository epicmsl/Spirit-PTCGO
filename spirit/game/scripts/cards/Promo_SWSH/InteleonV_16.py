from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import aqua_report, snipe_shot

card = PokemonCardDef(
    guid="7702d852-d3b5-5489-bbf2-94701b56076c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InteleonV.Name",
    display_name="Inteleon V",
    searchable_by=["Inteleon V", "Basic", "V", "InteleonV"],
    subtypes=["Basic", "V"],
    collector_number=16,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=818,
    abilities=[
        Attack(
            title="Snipe Shot",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=snipe_shot(40),
        ),
        Attack(
            title="Aqua Report",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=aqua_report(),
        ),
    ],
)
