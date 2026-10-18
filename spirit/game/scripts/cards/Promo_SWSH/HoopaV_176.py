from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import shadow_impact, two_faced

card = PokemonCardDef(
    guid="c4f17a47-daa4-5167-aebd-48aeb889ff2f",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoopaV.Name",
    display_name="Hoopa V",
    searchable_by=["Hoopa V", "Basic", "HoopaV"],
    subtypes=["Basic"],
    collector_number=176,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=720,
    abilities=[
        Ability(
            title="Two-Faced",
            game_text="As long as this Pok\u00e9mon is in play, it is Psychic and Darkness type.",
            effect=two_faced(),
            passive=two_faced(),
        ),
        Attack(
            title="Shadow Impact",
            game_text="Put 3 damage counters on 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=shadow_impact(3),
        ),
    ],
)
