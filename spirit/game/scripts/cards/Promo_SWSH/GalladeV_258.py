from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import buster_swing, rising_sword

card = PokemonCardDef(
    guid="30abfb8d-20ca-52c4-a285-1c40f71a5c16",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalladeV.Name",
    display_name="Gallade V",
    searchable_by=["Gallade V", "Basic", "V", "GalladeV"],
    subtypes=["Basic", "V"],
    collector_number=258,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=475,
    abilities=[
        Attack(
            title="Rising Sword",
            game_text="This attack does 50 more damage for each Prize card you have taken.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=rising_sword(50),
        ),
        Attack(
            title="Buster Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=buster_swing(),
        ),
    ],
)
