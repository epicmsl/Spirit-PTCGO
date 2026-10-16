from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import rapid_strike_search

card = PokemonCardDef(
    guid="fa3867f7-b85c-5910-a26f-c61430d06fa4",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1", "Octillery"],
    subtypes=["Stage 1"],
    collector_number=89,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Ability(
            title="Rapid Strike Search",
            game_text="Once during your turn, you may search your deck for a Rapid Strike card, reveal it, and put it into your hand. Then, shuffle your deck. You can't use more than 1 Rapid Strike Search Ability each turn.",
            effect=rapid_strike_search(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
