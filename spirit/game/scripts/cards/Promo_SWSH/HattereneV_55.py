from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import confounding_pulse, mental_crush

card = PokemonCardDef(
    guid="7c09df18-3b77-59b0-8dce-3623626f056d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HattereneV.Name",
    display_name="Hatterene V",
    searchable_by=["Hatterene V", "Basic", "V", "HattereneV"],
    subtypes=["Basic", "V"],
    collector_number=55,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=858,
    abilities=[
        Attack(
            title="Confounding Pulse",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. The new Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=confounding_pulse(),
        ),
        Attack(
            title="Mental Crush",
            game_text="If your opponent's Active Pok\u00e9mon is Confused, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=mental_crush(90),
        ),
    ],
)
