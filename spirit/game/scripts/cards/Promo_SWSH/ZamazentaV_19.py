from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import assault_tackle, dauntless_shield

card = PokemonCardDef(
    guid="01ebe4d4-602c-578a-ae97-b13539ef166e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaV.Name",
    display_name="Zamazenta V",
    searchable_by=["Zamazenta V", "Basic", "V", "ZamazentaV"],
    subtypes=["Basic", "V"],
    collector_number=19,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=230,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=889,
    abilities=[
        Ability(
            title="Dauntless Shield",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon VMAX.",
            passive=dauntless_shield(),
        ),
        Attack(
            title="Assault Tackle",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=assault_tackle(),
        ),
    ],
)
