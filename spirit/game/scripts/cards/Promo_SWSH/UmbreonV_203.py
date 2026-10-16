from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import mean_look, moonlight_blade

card = PokemonCardDef(
    guid="791cfb6c-2181-5e9a-9a11-81f3e937b0b4",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonV.Name",
    display_name="Umbreon V",
    searchable_by=["Umbreon V", "Basic", "V", "UmbreonV"],
    subtypes=["Basic", "V"],
    collector_number=203,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=197,
    abilities=[
        Attack(
            title="Mean Look",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=mean_look(),
        ),
        Attack(
            title="Moonlight Blade",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=moonlight_blade(80),
        ),
    ],
)
