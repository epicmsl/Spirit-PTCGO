from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import dyna_barrier, red_assist

card = PokemonCardDef(
    guid="476fdb57-0d5c-5847-ac2e-2aa8d7cbac7d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=171,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=380,
    abilities=[
        Ability(
            title="Red Assist",
            game_text="Once during your turn, you may attach a Psychic Energy card from your hand to 1 of your Latios.",
            effect=red_assist(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Dyna Barrier",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon .",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=dyna_barrier(),
        ),
    ],
)
