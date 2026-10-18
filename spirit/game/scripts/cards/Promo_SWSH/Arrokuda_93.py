from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import flock

card = PokemonCardDef(
    guid="68d57d65-db24-5d62-8629-9b0a3be8657a",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    display_name="Arrokuda",
    searchable_by=["Arrokuda", "Basic", "Arrokuda"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=846,
    abilities=[
        Attack(
            title="Flock",
            game_text="Search your deck for up to 2 Arrokuda and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flock("Arrokuda", 2),
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
