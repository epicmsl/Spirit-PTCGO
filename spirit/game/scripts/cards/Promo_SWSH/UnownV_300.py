from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import shady_stamp, victory_symbol

card = PokemonCardDef(
    guid="d22346d9-40bf-51b6-ba6a-b03493741548",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownV.Name",
    display_name="Unown V",
    searchable_by=["Unown V", "Basic", "V", "UnownV"],
    subtypes=["Basic", "V"],
    collector_number=300,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=201,
    abilities=[
        Attack(
            title="Shady Stamp",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=shady_stamp(),
        ),
        Attack(
            title="Victory Symbol",
            game_text="If you use this attack when you have only 1 Prize card remaining, you win this game.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=victory_symbol(),
        ),
    ],
)
