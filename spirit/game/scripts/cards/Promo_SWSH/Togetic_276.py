from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.promo_swsh_effects import voice_of_happiness

card = PokemonCardDef(
    guid="dfda90c3-1601-5b37-bf1e-5d7834726673",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    display_name="Togetic",
    searchable_by=["Togetic", "Stage 1", "Togetic"],
    subtypes=["Stage 1"],
    collector_number=276,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Voice of Happiness",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may heal 30 damage from your Active Pok\u00e9mon.",
            effect=voice_of_happiness(30),
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
