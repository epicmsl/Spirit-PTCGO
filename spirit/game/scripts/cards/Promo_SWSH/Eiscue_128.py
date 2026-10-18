from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import ice_bonus

card = PokemonCardDef(
    guid="bf0d2d56-de0f-5930-8b3d-262679bd4f67",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name",
    display_name="Eiscue",
    searchable_by=["Eiscue", "Basic", "Eiscue"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=875,
    abilities=[
        Attack(
            title="Ice Bonus",
            game_text="Discard a Water Energy card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=ice_bonus(3),
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
