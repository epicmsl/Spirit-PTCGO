from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import dynamax_cannon, power_accelerator

card = PokemonCardDef(
    guid="bbed2f8d-e761-5d2a-b1a9-a1b08481b304",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EternatusV.Name",
    display_name="Eternatus V",
    searchable_by=["Eternatus V", "Basic", "V", "EternatusV"],
    subtypes=["Basic", "V"],
    collector_number=44,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=890,
    abilities=[
        Attack(
            title="Power Accelerator",
            game_text="You may attach a Darkness Energy card from your hand to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=power_accelerator(),
        ),
        Attack(
            title="Dynamax Cannon",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon , this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=dynamax_cannon(120),
        ),
    ],
)
