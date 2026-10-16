from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import sturdy_shield

card = PokemonCardDef(
    guid="2d1808f3-8978-5166-8fba-a8b6600a2ed3",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zamazenta.Name",
    display_name="Zamazenta",
    searchable_by=["Zamazenta", "Basic", "Zamazenta"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=889,
    abilities=[
        Ability(
            title="Sturdy Shield",
            game_text="This Pok\u00e9mon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            effect=sturdy_shield(20),
            passive=sturdy_shield(20),
        ),
        Attack(
            title="Headbang",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
