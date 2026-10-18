from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import disarming_voice, tricky_ribbon

card = PokemonCardDef(
    guid="9065e5ba-fbfb-5226-89bd-b3e322516900",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkSylveonV.Name",
    display_name="Dark Sylveon V",
    searchable_by=["Dark Sylveon V", "Basic", "V", "DarkSylveonV"],
    subtypes=["Basic", "V"],
    collector_number=134,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=700,
    abilities=[
        Attack(
            title="Disarming Voice",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=disarming_voice(),
        ),
        Attack(
            title="Tricky Ribbon",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=tricky_ribbon(),
        ),
    ],
)
