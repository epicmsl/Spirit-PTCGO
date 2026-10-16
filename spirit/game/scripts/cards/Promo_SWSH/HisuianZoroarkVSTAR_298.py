from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import phantom_star, ticking_curse

card = PokemonCardDef(
    guid="88e42623-35fd-5bb6-a60f-17d633de5748",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroarkVSTAR.Name",
    display_name="Hisuian Zoroark VSTAR",
    searchable_by=["Hisuian Zoroark VSTAR", "VSTAR", "HisuianZoroarkVSTAR"],
    subtypes=["VSTAR"],
    collector_number=298,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVSTAR,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroarkV.Name",
    family_id=571,
    abilities=[
        Attack(
            title="Ticking Curse",
            game_text="This attack does 50 damage for each of your Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=ticking_curse(50),
        ),
        Ability(
            title="[VSTAR Power] [Ability] Phantom Star",
            game_text="During your turn, you may discard your hand and draw 7 cards. (You can't use more than 1 {VSTAR} Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            effect=phantom_star(draw=7),
            vstar=True,
        ),
    ],
)
