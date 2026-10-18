from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import abyss_seeking
from spirit.game.card_effects.pokemon import shred

card = PokemonCardDef(
    guid="8909aa2e-4bea-5114-9e4d-87982fde229f",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaV.Name",
    display_name="Giratina V",
    searchable_by=["Giratina V", "Basic", "V", "GiratinaV"],
    subtypes=["Basic", "V"],
    collector_number=259,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=487,
    abilities=[
        Attack(
            title="Abyss Seeking",
            game_text="Look at the top 4 cards of your deck and put 2 of them into your hand. Put the other cards in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=abyss_seeking(2, 4),
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=shred,
        ),
    ],
)
