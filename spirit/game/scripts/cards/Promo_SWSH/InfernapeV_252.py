from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import bright_flame, meteor_punch

card = PokemonCardDef(
    guid="41cf25ce-63da-54a7-b037-d949f37c5810",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.InfernapeV.Name",
    display_name="Infernape V",
    searchable_by=["Infernape V", "Basic", "V", "InfernapeV"],
    subtypes=["Basic", "V"],
    collector_number=252,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=390,
    abilities=[
        Attack(
            title="Meteor Punch",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=meteor_punch(30),
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=bright_flame(2),
        ),
    ],
)
