from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import clutch, sky_hurricane

card = PokemonCardDef(
    guid="5f15f464-56fe-5fbd-bb34-ecdfe9adf08b",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CorviknightV.Name",
    display_name="Corviknight V",
    searchable_by=["Corviknight V", "Basic", "V", "CorviknightV"],
    subtypes=["Basic", "V"],
    collector_number=200,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=823,
    abilities=[
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=clutch(),
        ),
        Attack(
            title="Sky Hurricane",
            game_text="During your next turn, this Pok\u00e9mon can't use Sky Hurricane.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=sky_hurricane(),
            locks_next_turn=True,
        ),
    ],
)
