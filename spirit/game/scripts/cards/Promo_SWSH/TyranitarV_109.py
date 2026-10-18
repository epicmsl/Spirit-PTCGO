from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import cragalanche, single_strike_crush

card = PokemonCardDef(
    guid="95bbf553-fc12-5eec-a811-98057dcb4465",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TyranitarV.Name",
    display_name="Tyranitar V",
    searchable_by=["Tyranitar V", "Basic", "V", "TyranitarV"],
    subtypes=["Basic", "V"],
    collector_number=109,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=230,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=248,
    abilities=[
        Attack(
            title="Cragalanche",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=cragalanche(2),
        ),
        Attack(
            title="Single Strike Crush",
            game_text="Discard the top 4 cards of your deck.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=240,
            effect=single_strike_crush(4),
        ),
    ],
)
