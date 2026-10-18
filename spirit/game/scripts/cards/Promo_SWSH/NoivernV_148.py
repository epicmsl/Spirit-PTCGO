from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import boomburst, synchro_loud

card = PokemonCardDef(
    guid="1bdcba03-9331-5a74-bb96-566667b24214",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NoivernV.Name",
    display_name="Noivern V",
    searchable_by=["Noivern V", "Basic", "V", "NoivernV"],
    subtypes=["Basic", "V"],
    collector_number=148,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=715,
    abilities=[
        Attack(
            title="Boomburst",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=boomburst(20),
        ),
        Attack(
            title="Synchro Loud",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=60,
            damage_operator="+",
            effect=synchro_loud(120),
        ),
    ],
)
