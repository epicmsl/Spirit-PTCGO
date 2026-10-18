from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import splash_jump, triple_draw

card = PokemonCardDef(
    guid="0d5aa6d5-bef2-518f-8b57-e90bcc179f47",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonV.Name",
    display_name="Vaporeon V",
    searchable_by=["Vaporeon V", "Basic", "V", "VaporeonV"],
    subtypes=["Basic", "V"],
    collector_number=181,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=134,
    abilities=[
        Attack(
            title="Triple Draw",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=triple_draw(),
        ),
        Attack(
            title="Splash Jump",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=splash_jump(),
        ),
    ],
)
