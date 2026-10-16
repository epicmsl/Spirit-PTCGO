from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.promo_swsh_effects import mind_bend, teapot_of_surprises

card = PokemonCardDef(
    guid="ce3aa93a-5b7c-581c-9558-1aa1fdaa49d0",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PolteageistV.Name",
    display_name="Polteageist V",
    searchable_by=["Polteageist V", "Basic", "V", "PolteageistV"],
    subtypes=["Basic", "V"],
    collector_number=21,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=854,
    abilities=[
        Ability(
            title="Teapot of Surprises",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if it is Knocked Out), choose a random card from your opponent's hand. Your opponent reveals that card and puts it on the bottom of their deck.",
            effect=teapot_of_surprises,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title="Mind Bend",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=mind_bend(),
        ),
    ],
)
