from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import arm_charge

card = PokemonCardDef(
    guid="42366c34-bb57-52fe-8b02-4604cd51b8c3",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MelmetalV.Name",
    display_name="Melmetal V",
    searchable_by=["Melmetal V", "Basic", "V", "MelmetalV"],
    subtypes=["Basic", "V"],
    collector_number=224,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=809,
    abilities=[
        Attack(
            title="Arm Charge",
            game_text="You may attach a Metal Energy card from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2},
            damage=50,
            effect=arm_charge(),
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.METAL: 3},
            damage=140,
        ),
    ],
)
