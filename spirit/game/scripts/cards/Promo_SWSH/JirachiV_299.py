from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.promo_swsh_effects import hypnostrike, wish_connector

card = PokemonCardDef(
    guid="1bf6d37c-c830-5066-978f-b75b5feb5fca",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JirachiV.Name",
    display_name="Jirachi V",
    searchable_by=["Jirachi V", "Basic", "V", "JirachiV"],
    subtypes=["Basic", "V"],
    collector_number=299,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=385,
    abilities=[
        Ability(
            title="Wish Connector",
            game_text="When 1 of your Basic Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, you may move a basic Energy card from that Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=wish_connector,
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
        ),
        Attack(
            title="Hypnostrike",
            game_text="Both Active Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=hypnostrike(),
        ),
    ],
)
