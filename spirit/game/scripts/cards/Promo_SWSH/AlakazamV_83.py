from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import mind_ruler, zen_spoon

card = PokemonCardDef(
    guid="e8a5c33d-0e88-5f4b-b761-7fea07643d7e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamV.Name",
    display_name="Alakazam V",
    searchable_by=["Alakazam V", "Basic", "V", "AlakazamV"],
    subtypes=["Basic", "V"],
    collector_number=83,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=65,
    abilities=[
        Attack(
            title="Zen Spoon",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=zen_spoon,
        ),
        Attack(
            title="Mind Ruler",
            game_text="This attack does 30 damage for each card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="x",
            effect=mind_ruler(),
        ),
    ],
)
