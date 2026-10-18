from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import cloak_in_shadows, hollow_binding

card = PokemonCardDef(
    guid="36b3893f-f395-5ad9-9e8c-af5f3f5e5f7c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShadowRiderCalyrexV.Name",
    display_name="Shadow Rider Calyrex V",
    searchable_by=["Shadow Rider Calyrex V", "Basic", "V", "ShadowRiderCalyrexV"],
    subtypes=["Basic", "V"],
    collector_number=131,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=898,
    abilities=[
        Attack(
            title="Cloak in Shadows",
            game_text="Attach a Psychic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=cloak_in_shadows(),
        ),
        Attack(
            title="Hollow Binding",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=hollow_binding(),
        ),
    ],
)
