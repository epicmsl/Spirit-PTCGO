from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import steel_beam

card = PokemonCardDef(
    guid="dc5f6508-205f-54b8-aff3-7824b00804cd",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    display_name="Duraludon",
    searchable_by=["Duraludon", "Basic", "Duraludon"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=884,
    abilities=[
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
        Attack(
            title="Steel Beam",
            game_text="This Pok\u00e9mon also does 40 damage to itself.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=steel_beam(40),
        ),
    ],
)
