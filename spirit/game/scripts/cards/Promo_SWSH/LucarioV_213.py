from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import crushing_punch

card = PokemonCardDef(
    guid="0d1f2a52-4f1a-5041-a8de-94a614079f9c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioV.Name",
    display_name="Lucario V",
    searchable_by=["Lucario V", "Basic", "V", "LucarioV"],
    subtypes=["Basic", "V"],
    collector_number=213,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=448,
    abilities=[
        Attack(
            title="Crushing Punch",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=crushing_punch(),
        ),
        Attack(
            title="Cyclone Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
