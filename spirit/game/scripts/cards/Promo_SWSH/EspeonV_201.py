from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import zen_shot

card = PokemonCardDef(
    guid="f395e848-80c9-5cf1-b5fa-228c683ee31c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EspeonV.Name",
    display_name="Espeon V",
    searchable_by=["Espeon V", "Basic", "V", "EspeonV"],
    subtypes=["Basic", "V"],
    collector_number=201,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=196,
    abilities=[
        Attack(
            title="Zen Shot",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon . (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=zen_shot(60),
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
