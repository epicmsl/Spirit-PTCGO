from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import find_a_friend

card = PokemonCardDef(
    guid="f59774cb-b0f0-55bd-b593-065df4ce644d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatenna.Name",
    display_name="Hatenna",
    searchable_by=["Hatenna", "Basic", "Hatenna"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=856,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=find_a_friend(),
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
