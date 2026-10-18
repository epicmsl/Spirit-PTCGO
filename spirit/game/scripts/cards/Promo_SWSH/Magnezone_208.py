from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import giga_magnet

card = PokemonCardDef(
    guid="28e15b5b-fc96-500d-9350-405ef6072df3",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2", "Magnezone"],
    subtypes=["Stage 2"],
    collector_number=208,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Giga Magnet",
            game_text="Once during your turn, you may look at the top 6 cards of your deck and attach any number of Metal Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck.",
            effect=giga_magnet(6),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Power Beam",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
