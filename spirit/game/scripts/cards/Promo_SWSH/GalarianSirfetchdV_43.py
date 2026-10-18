from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import meteor_smash, resolute_spear

card = PokemonCardDef(
    guid="cf72ff26-a6ef-5501-8b85-002dd6dedf0c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSirfetchdV.Name",
    display_name="Galarian Sirfetch'd V",
    searchable_by=["Galarian Sirfetch'd V", "Basic", "V", "GalarianSirfetchdV"],
    subtypes=["Basic", "V"],
    collector_number=43,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=865,
    abilities=[
        Ability(
            title="Resolute Spear",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may move any amount of Fighting Energy from your other Pok\u00e9mon to it.",
            effect=resolute_spear(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Meteor Smash",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=meteor_smash(),
            locks_next_turn=True,
        ),
    ],
)
