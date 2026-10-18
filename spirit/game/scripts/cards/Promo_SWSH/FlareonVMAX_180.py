from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import max_detonate

card = PokemonCardDef(
    guid="fb49922e-fe01-536a-a30e-1a6532a14e45",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonVMAX.Name",
    display_name="Flareon VMAX",
    searchable_by=["Flareon VMAX", "VMAX", "Single Strike", "FlareonVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=180,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET]),
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.FlareonV.Name",
    family_id=136,
    abilities=[
        Attack(
            title="Max Detonate",
            game_text="Discard the top 5 cards of your deck. This attack does 100 damage for each Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="x",
            effect=max_detonate(100, 5),
        ),
    ],
)
