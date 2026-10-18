from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import psychic

card = PokemonCardDef(
    guid="17033429-c2f2-57b3-a28f-3bfd639763ee",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name",
    display_name="Deoxys V",
    searchable_by=["Deoxys V", "Basic", "V", "DeoxysV"],
    subtypes=["Basic", "V"],
    collector_number=266,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=386,
    abilities=[
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=psychic(30),
        ),
        Attack(
            title="Power Edge",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
