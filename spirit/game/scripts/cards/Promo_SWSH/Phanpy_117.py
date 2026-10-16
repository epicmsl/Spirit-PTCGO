from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import strike_back

card = PokemonCardDef(
    guid="fe04d75e-fbfb-50d1-8ae6-8f489b8894b9",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    display_name="Phanpy",
    searchable_by=["Phanpy", "Basic", "Phanpy"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=231,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Strike Back",
            game_text="This attack does 30 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=strike_back(30),
        ),
    ],
)
