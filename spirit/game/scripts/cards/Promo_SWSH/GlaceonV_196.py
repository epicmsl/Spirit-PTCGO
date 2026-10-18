from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import frost_charge

card = PokemonCardDef(
    guid="8e478dfd-d95b-5be3-9006-352966b06543",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name",
    display_name="Glaceon V",
    searchable_by=["Glaceon V", "Basic", "V", "GlaceonV"],
    subtypes=["Basic", "V"],
    collector_number=196,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=471,
    abilities=[
        Attack(
            title="Frost Charge",
            game_text="Search your deck for a Water Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=frost_charge(),
        ),
        Attack(
            title="Freezing Wind",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
