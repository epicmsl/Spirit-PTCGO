from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import extreme_current, lost_hack

card = PokemonCardDef(
    guid="1b8cdd35-f029-5e42-acba-1abe8c0742f7",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RotomV.Name",
    display_name="Rotom V",
    searchable_by=["Rotom V", "Basic", "V", "RotomV"],
    subtypes=["Basic", "V"],
    collector_number=257,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Attack(
            title="Lost Hack",
            game_text="Put a Special Energy attached to 1 of your opponent's Pok\u00e9mon in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=lost_hack(),
        ),
        Attack(
            title="Extreme Current",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=extreme_current(),
        ),
    ],
)
