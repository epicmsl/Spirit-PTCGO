from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import brave_blade, intrepid_sword

card = PokemonCardDef(
    guid="a81f4a1e-62fd-57ef-ae55-30a8a664c062",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianV.Name",
    display_name="Zacian V",
    searchable_by=["Zacian V", "Basic", "V", "ZacianV"],
    subtypes=["Basic", "V"],
    collector_number=292,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        Ability(
            title="Intrepid Sword",
            game_text="Once during your turn, you may look at the top 3 cards of your deck and attach any number of Metal Energy cards you find there to this Pok\u00e9mon. Put the other cards into your hand. If you use this Ability, your turn ends.",
            effect=intrepid_sword(3),
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
        ),
        Attack(
            title="Brave Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 3},
            damage=230,
            effect=brave_blade(),
            locks_next_turn=True,
        ),
    ],
)
