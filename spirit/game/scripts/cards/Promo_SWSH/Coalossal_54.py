from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import tar_generator

card = PokemonCardDef(
    guid="cc4f2855-5cb0-57f9-97dd-f36169e98cfe",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Coalossal.Name",
    display_name="Coalossal",
    searchable_by=["Coalossal", "Stage 2", "Coalossal"],
    subtypes=["Stage 2"],
    collector_number=54,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    family_id=837,
    abilities=[
        Ability(
            title="Tar Generator",
            game_text="Once during your turn, you may attach a Fire Energy card, a Fighting Energy card, or 1 of each from your discard pile to your Pok\u00e9mon in any way you like.",
            effect=tar_generator(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Flaming Avalanche",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
