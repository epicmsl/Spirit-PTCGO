from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import voltage_beat

card = PokemonCardDef(
    guid="b45d5767-29b0-5413-8493-46ae97bc58d7",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rillaboom.Name",
    display_name="Rillaboom",
    searchable_by=["Rillaboom", "Stage 2", "Rillaboom"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    family_id=810,
    abilities=[
        Ability(
            title="Voltage Beat",
            game_text="Once during your turn, you may search your deck for up to 2 Grass Energy cards and attach them to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            effect=voltage_beat(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
