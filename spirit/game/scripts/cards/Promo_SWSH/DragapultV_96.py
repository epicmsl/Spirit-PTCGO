from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import jet_assault

card = PokemonCardDef(
    guid="bc839eb9-9c5a-5da2-aa0c-6d593541e2c2",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragapultV.Name",
    display_name="Dragapult V",
    searchable_by=["Dragapult V", "Basic", "V", "DragapultV"],
    subtypes=["Basic", "V"],
    collector_number=96,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=887,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Jet Assault",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=60,
            damage_operator="+",
            effect=jet_assault(80),
        ),
    ],
)
