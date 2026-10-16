from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import pitch_a_pyukumuku

card = PokemonCardDef(
    guid="117638ee-dcae-597e-b715-91c164f5f928",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyukumuku.Name",
    display_name="Pyukumuku",
    searchable_by=["Pyukumuku", "Basic", "Pyukumuku"],
    subtypes=["Basic"],
    collector_number=169,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=771,
    abilities=[
        Ability(
            title="Pitch a Pyukumuku",
            game_text="Once during your turn, if this Pok\u00e9mon is in your hand, you may reveal it and put it on the bottom of your deck. If you do, draw a card. You can't use more than 1 Pitch a Pyukumuku Ability each turn.",
            effect=pitch_a_pyukumuku(),
            activation=Activations.ONCE_PER_TURN,
            usable_from="hand",
        ),
        Attack(
            title="Knuckle Punch",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
