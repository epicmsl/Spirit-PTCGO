from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import heat_boost

card = PokemonCardDef(
    guid="9cf6bd0b-f092-5714-bb5d-d18e21c240ab",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name",
    display_name="Rapidash",
    searchable_by=["Rapidash", "Stage 1", "Rapidash"],
    subtypes=["Stage 1"],
    collector_number=270,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=77,
    abilities=[
        Ability(
            title="Heat Boost",
            game_text="Once during your turn, you may discard a Fire Energy card from your hand in order to use this Ability. During this turn, your Fire Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=heat_boost(30),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Fire Mane",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
