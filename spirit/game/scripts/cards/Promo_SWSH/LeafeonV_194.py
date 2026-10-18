from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import leaf_guard, slashing_strike

card = PokemonCardDef(
    guid="952f71cd-3c31-5e05-8c71-5df18bcb508f",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonV.Name",
    display_name="Leafeon V",
    searchable_by=["Leafeon V", "Basic", "V", "LeafeonV"],
    subtypes=["Basic", "V"],
    collector_number=194,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=470,
    abilities=[
        Attack(
            title="Leaf Guard",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=leaf_guard(30),
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Slashing Strike.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=slashing_strike(),
            locks_next_turn=True,
        ),
    ],
)
