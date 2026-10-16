from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import wind_pressure

card = PokemonCardDef(
    guid="3bca324f-81c4-5e87-8f3a-ee17586e7393",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Wind Pressure",
            game_text="If your opponent has 5 or fewer cards in their hand, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=250,
            effect=wind_pressure(),
        ),
    ],
)
