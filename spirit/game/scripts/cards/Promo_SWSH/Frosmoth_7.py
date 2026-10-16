from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import ice_dance

card = PokemonCardDef(
    guid="ac9190f0-146f-55f3-a591-43fa3fb546ba",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frosmoth.Name",
    display_name="Frosmoth",
    searchable_by=["Frosmoth", "Stage 1", "Frosmoth"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    family_id=872,
    abilities=[
        Ability(
            title="Ice Dance",
            game_text="As often as you like during your turn, you may attach a Water Energy card from your hand to 1 of your Benched Water Pok\u00e9mon.",
            effect=ice_dance(),
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
