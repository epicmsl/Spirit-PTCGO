from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import brawny_knuckle

card = PokemonCardDef(
    guid="018ef14c-3503-5caf-b85b-e8f65f51a317",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SingleStrikeUrshifuV.Name",
    display_name="Single Strike Urshifu V",
    searchable_by=["Single Strike Urshifu V", "Basic", "V", "SingleStrikeUrshifuV"],
    subtypes=["Basic", "V"],
    collector_number=106,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=892,
    abilities=[
        Attack(
            title="Low Kick",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Brawny Knuckle",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=180,
            effect=brawny_knuckle(),
        ),
    ],
)
