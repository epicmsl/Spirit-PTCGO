from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.promo_swsh_effects import float_up, happy_match

card = PokemonCardDef(
    guid="013fb532-1de5-5b22-aedc-1dd29e2d542d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EldegossV.Name",
    display_name="Eldegoss V",
    searchable_by=["Eldegoss V", "Basic", "V", "EldegossV"],
    subtypes=["Basic", "V"],
    collector_number=84,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=830,
    abilities=[
        Ability(
            title="Happy Match",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may put a Supporter card from your discard pile into your hand.",
            effect=happy_match(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Float Up",
            game_text="You may shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=float_up(),
        ),
    ],
)
