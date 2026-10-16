from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import swelling_pulse

card = PokemonCardDef(
    guid="cb208be4-8bea-5fc3-97c8-c45c7e754dad",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirV.Name",
    display_name="Gardevoir V",
    searchable_by=["Gardevoir V", "Basic", "V", "GardevoirV"],
    subtypes=["Basic", "V"],
    collector_number=105,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=282,
    abilities=[
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Swelling Pulse",
            game_text="If this Pok\u00e9mon was healed during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=swelling_pulse(80),
        ),
    ],
)
