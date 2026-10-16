from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import acid_spray, apple_drop

card = PokemonCardDef(
    guid="1c0d0a38-0ce1-5524-be88-959fa2a0aef9",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flapple.Name",
    display_name="Flapple",
    searchable_by=["Flapple", "Stage 1", "Flapple"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Apple Drop",
            game_text="Once during your turn, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon. If you placed any damage counters in this way, shuffle this Pok\u00e9mon and all attached cards into your deck.",
            effect=apple_drop(2),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Acid Spray",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=acid_spray(),
        ),
    ],
)
