from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import dream_gift

card = PokemonCardDef(
    guid="c5af55f3-c227-5853-949c-8cc587fcbdcd",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonV.Name",
    display_name="Sylveon V",
    searchable_by=["Sylveon V", "Basic", "V", "SylveonV"],
    subtypes=["Basic", "V"],
    collector_number=202,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=700,
    abilities=[
        Ability(
            title="Dream Gift",
            game_text="Once during your turn, you may search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck. If you use this Ability, your turn ends.",
            effect=dream_gift(),
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
