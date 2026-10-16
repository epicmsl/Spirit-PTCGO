from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import dragon_pulse, spiral_burst

card = PokemonCardDef(
    guid="68a56f39-1b6d-56ae-816f-9ff2a275ca08",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaV.Name",
    display_name="Rayquaza V",
    searchable_by=["Rayquaza V", "Basic", "V", "RayquazaV"],
    subtypes=["Basic", "V"],
    collector_number=147,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=384,
    abilities=[
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
            effect=dragon_pulse(2),
        ),
        Attack(
            title="Spiral Burst",
            game_text="You may discard up to 2 basic Fire Energy or up to 2 basic Lightning Energy from this Pok\u00e9mon. This attack does 80 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=spiral_burst(80, 2),
        ),
    ],
)
