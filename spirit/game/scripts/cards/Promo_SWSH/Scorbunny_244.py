from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import flaring_dash

card = PokemonCardDef(
    guid="9cf63fe3-a26b-552c-9337-ba3e5b8f8160",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    display_name="Scorbunny",
    searchable_by=["Scorbunny", "Basic", "Scorbunny"],
    subtypes=["Basic"],
    collector_number=244,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=813,
    abilities=[
        Attack(
            title="Flaring Dash",
            game_text="Flip a coin until you get tails. For each heads, draw a card.",
            cost={PokemonTypes.FIRE: 1},
            effect=flaring_dash(),
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
