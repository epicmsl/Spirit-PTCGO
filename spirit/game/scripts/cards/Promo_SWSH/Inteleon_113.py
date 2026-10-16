from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import quick_shooting

card = PokemonCardDef(
    guid="a86bcb2c-2b2a-5160-ad64-a818436e27d2",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inteleon.Name",
    display_name="Inteleon",
    searchable_by=["Inteleon", "Stage 2", "Inteleon"],
    subtypes=["Stage 2"],
    collector_number=113,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    family_id=816,
    abilities=[
        Ability(
            title="Quick Shooting",
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            effect=quick_shooting(2),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
