from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import torrential_cannon

card = PokemonCardDef(
    guid="cd51c6d1-cc42-573c-afa1-dd162ca88385",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseV.Name",
    display_name="Blastoise V",
    searchable_by=["Blastoise V", "Basic", "V", "BlastoiseV"],
    subtypes=["Basic", "V"],
    collector_number=101,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=7,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Torrential Cannon",
            game_text="During your next turn, this Pok\u00e9mon can't use Torrential Cannon.",
            cost={PokemonTypes.WATER: 3},
            damage=200,
            effect=torrential_cannon(),
            locks_next_turn=True,
        ),
    ],
)
