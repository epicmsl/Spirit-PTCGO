from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import mixed_call

card = PokemonCardDef(
    guid="40b8f1bf-6aee-5161-85c1-97a79bc4eab5",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=210,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=741,
    abilities=[
        Attack(
            title="Mixed Call",
            game_text="Search your deck for a Pok\u00e9mon and a Supporter card, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mixed_call(),
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
