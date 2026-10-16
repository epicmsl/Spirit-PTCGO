from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import pay_day

card = PokemonCardDef(
    guid="bf705b56-8972-530b-a961-9b2a9c76159f",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MeowthV.Name",
    display_name="Meowth V",
    searchable_by=["Meowth V", "Basic", "V", "MeowthV"],
    subtypes=["Basic", "V"],
    collector_number=4,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Pay Day",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=pay_day(),
        ),
        Attack(
            title="Slashing Claw",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
