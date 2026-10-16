from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import ivy_star, leaf_guard


def _ivy_star_condition(board, player_id, pokemon):
    opponent_id = next(p for p in board.player_ids if p != player_id)
    bench = board.find_player_area(opponent_id, "bench")
    return bool(board.active_pokemon(opponent_id)) and bool(bench and bench.children)

card = PokemonCardDef(
    guid="eeb71071-3c56-5e3b-93d2-259bbd801743",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonVSTAR.Name",
    display_name="Leafeon VSTAR",
    searchable_by=["Leafeon VSTAR", "VSTAR", "LeafeonVSTAR"],
    subtypes=["VSTAR"],
    collector_number=195,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVSTAR,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LeafeonV.Name",
    family_id=470,
    abilities=[
        Attack(
            title="Leaf Guard",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=leaf_guard(30),
        ),
        Ability(
            title="[VSTAR Power] [Ability] Ivy Star",
            game_text="During your turn, you may switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. (You can't use more than 1 {VSTAR} Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            condition=_ivy_star_condition,
            effect=ivy_star(),
            vstar=True,
        ),
    ],
)
