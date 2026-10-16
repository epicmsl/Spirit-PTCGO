from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import g_max_gold_rush

card = PokemonCardDef(
    guid="198ef107-b593-50e8-b346-cac114a0ba2d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MeowthVMAX.Name",
    display_name="Meowth VMAX",
    searchable_by=["Meowth VMAX", "VMAX", "MeowthVMAX"],
    subtypes=["VMAX"],
    collector_number=5,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVMAX,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MeowthV.Name",
    family_id=52,
    abilities=[
        Attack(
            title="G-Max Gold Rush",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=g_max_gold_rush(),
        ),
    ],
)
