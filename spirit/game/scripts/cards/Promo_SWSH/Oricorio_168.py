from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import lesson_in_zeal
from spirit.game.card_effects.pokemon import glistening_droplets

card = PokemonCardDef(
    guid="0892a880-57e8-5047-b745-3c5c66e84cf1",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=168,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=741,
    abilities=[
        Ability(
            title="Lesson in Zeal",
            game_text="All of your Fusion Strike Pok\u00e9mon take 20 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance). You can't apply more than 1 Lesson in Zeal Ability at a time.",
            effect=lesson_in_zeal(20),
            passive=lesson_in_zeal(20),
        ),
        Attack(
            title="Glistening Droplets",
            game_text="Put 5 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=glistening_droplets,
        ),
    ],
)
