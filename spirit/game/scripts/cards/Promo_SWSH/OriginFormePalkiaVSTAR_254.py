from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import star_portal, subspace_swell
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.session.effects import is_water_pokemon


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


def _star_portal_condition(board, player_id, pokemon=None):
    return requires_discard(_is_water_energy)(board, player_id, pokemon) \
        and any(is_water_pokemon(p) for p in board.pokemon_in_play(player_id))

card = PokemonCardDef(
    guid="297f105a-0726-5079-87fa-8bba217c4db8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormePalkiaVSTAR.Name",
    display_name="Origin Forme Palkia VSTAR",
    searchable_by=["Origin Forme Palkia VSTAR", "VSTAR", "OriginFormePalkiaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=254,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVSTAR,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=280,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormePalkiaV.Name",
    family_id=484,
    abilities=[
        Attack(
            title="Subspace Swell",
            game_text="This attack does 20 more damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            damage_operator="+",
            effect=subspace_swell(20),
        ),
        Ability(
            title="[VSTAR Power] [Ability] Star Portal",
            game_text="During your turn, you may attach up to 3 Water Energy cards from your discard pile to your Water Pok\u00e9mon in any way you like. (You can't use more than 1 {VSTAR} Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            condition=_star_portal_condition,
            effect=star_portal(count=3),
            vstar=True,
        ),
    ],
)
