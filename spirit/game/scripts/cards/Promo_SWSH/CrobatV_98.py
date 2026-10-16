from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.promo_swsh_effects import dark_asset, venomous_fang

card = PokemonCardDef(
    guid="a2b54d07-0ea0-5eb1-ae00-38a140407fe4",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatV.Name",
    display_name="Crobat V",
    searchable_by=["Crobat V", "Basic", "V", "CrobatV"],
    subtypes=["Basic", "V"],
    collector_number=98,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=169,
    abilities=[
        Ability(
            title="Dark Asset",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may draw cards until you have 6 cards in your hand. You can't use more than 1 Dark Asset Ability each turn.",
            effect=dark_asset(6),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Venomous Fang",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=venomous_fang(),
        ),
    ],
)
