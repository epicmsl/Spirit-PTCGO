from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import single_strike_tackle

card = PokemonCardDef(
    guid="ad544d88-ce27-51c9-ab59-2b0c305a3c00",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Attack(
            title="Slap Push",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Single Strike Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=single_strike_tackle(30),
        ),
    ],
)
