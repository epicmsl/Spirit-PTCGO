from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import growl

card = PokemonCardDef(
    guid="d012e5f1-4945-5cd5-b1f5-87ee976d148a",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name",
    display_name="Sobble",
    searchable_by=["Sobble", "Basic", "Sobble"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=816,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=growl(20),
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
