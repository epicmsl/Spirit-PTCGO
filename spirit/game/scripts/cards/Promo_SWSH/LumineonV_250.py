from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.pokemon import aqua_return, luminous_sign

card = PokemonCardDef(
    guid="a9a49fa2-c6c5-579e-8a8f-d54f1f853281",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LumineonV.Name",
    display_name="Lumineon V",
    searchable_by=["Lumineon V", "Basic", "V", "LumineonV"],
    subtypes=["Basic", "V"],
    collector_number=250,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=457,
    abilities=[
        Ability(
            title="Luminous Sign",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=luminous_sign,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Aqua Return",
            game_text="Shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=aqua_return,
        ),
    ],
)
