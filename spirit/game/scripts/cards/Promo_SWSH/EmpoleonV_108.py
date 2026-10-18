from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import emperors_eyes, swirling_slice

card = PokemonCardDef(
    guid="716bf18e-fcbb-5291-8825-1332259097e0",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EmpoleonV.Name",
    display_name="Empoleon V",
    searchable_by=["Empoleon V", "Basic", "V", "EmpoleonV"],
    subtypes=["Basic", "V"],
    collector_number=108,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=395,
    abilities=[
        Ability(
            title="Emperor's Eyes",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Basic Pok\u00e9mon in play have no Abilities, except for Pok\u00e9mon with a Rule Box (Pok\u00e9mon , Pok\u00e9mon GX Attack, etc. have Rule Boxes).",
            effect=emperors_eyes(),
            passive=emperors_eyes(),
        ),
        Attack(
            title="Swirling Slice",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=swirling_slice(),
        ),
    ],
)
