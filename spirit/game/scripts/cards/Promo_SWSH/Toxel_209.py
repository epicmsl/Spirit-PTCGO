from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import growl

card = PokemonCardDef(
    guid="2c201e06-eccc-5f43-8b58-e0f4b3565765",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    display_name="Toxel",
    searchable_by=["Toxel", "Basic", "Toxel"],
    subtypes=["Basic"],
    collector_number=209,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=848,
    abilities=[
        Attack(
            title="Growl",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=growl(30),
        ),
        Attack(
            title="Tiny Bolt",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
