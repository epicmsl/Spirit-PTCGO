from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import dark_squall

card = PokemonCardDef(
    guid="4d16adab-390b-5bd0-872d-ee445162753a",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Dark Squall",
            game_text="As often as you like during your turn, you may attach a Darkness Energy card from your hand to 1 of your Pok\u00e9mon.",
            effect=dark_squall(),
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title="Pitch-Black Fangs",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
