from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.card_effects.promo_swsh_effects import field_runner_passive
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects


card = PokemonCardDef(
    guid="6d848b89-a948-5830-81e0-457429e7ebef",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CinderaceV.Name",
    display_name="Cinderace V",
    searchable_by=["Cinderace V", "Basic", "V", "CinderaceV"],
    subtypes=["Basic", "V"],
    collector_number=15,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=815,
    abilities=[
        Ability(
            title="Field Runner",
            game_text="If a Stadium is in play, this Pok\u00e9mon has no Retreat Cost.",
            effect=field_runner_passive(),
            passive=field_runner_passive(),
        ),
        Attack(
            title="Crimson Legs",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
