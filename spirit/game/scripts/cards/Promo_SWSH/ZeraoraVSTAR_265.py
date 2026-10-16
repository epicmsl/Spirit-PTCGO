from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import crushing_beat, lightning_storm_star

card = PokemonCardDef(
    guid="59992062-228c-53bc-966e-63e95f462544",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraVSTAR.Name",
    display_name="Zeraora VSTAR",
    searchable_by=["Zeraora VSTAR", "VSTAR", "ZeraoraVSTAR"],
    subtypes=["VSTAR"],
    collector_number=265,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVSTAR,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=270,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VSTAR,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraV.Name",
    family_id=807,
    abilities=[
        Attack(
            title="Crushing Beat",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=crushing_beat(),
        ),
        Attack(
            title="[VSTAR Power] Lightning Storm Star",
            game_text="Choose 1 of your opponent's Pok\u00e9mon 4 times. (You can choose the same Pok\u00e9mon more than once.) For each time you chose a Pok\u00e9mon, do 60 damage to it. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 {VSTAR} Power in a game.)",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            effect=lightning_storm_star(60, 4),
            vstar=True,
        ),
    ],
)
