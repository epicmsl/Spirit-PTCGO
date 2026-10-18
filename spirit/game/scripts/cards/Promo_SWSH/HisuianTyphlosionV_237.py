from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import petrifying_flame, singe

card = PokemonCardDef(
    guid="223b5983-10bc-5e35-a78d-55829dc8ba19",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianTyphlosionV.Name",
    display_name="Hisuian Typhlosion V",
    searchable_by=["Hisuian Typhlosion V", "Basic", "V", "HisuianTyphlosionV"],
    subtypes=["Basic", "V"],
    collector_number=237,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=157,
    abilities=[
        Ability(
            title="Singe",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            effect=singe(),
        ),
        Attack(
            title="Petrifying Flame",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=petrifying_flame(),
        ),
    ],
)
