from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import double_impact, limber_up

card = PokemonCardDef(
    guid="35dbb5d4-e787-5268-890e-2e40bb16ad31",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=247,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Attack(
            title="Limber Up",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=limber_up(),
        ),
        Attack(
            title="Double Impact",
            game_text="Flip 2 coins. This attack does 120 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="x",
            effect=double_impact(120, 2),
        ),
    ],
)
