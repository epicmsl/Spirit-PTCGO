from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import metal_transfer, has_energy_in_play

card = PokemonCardDef(
    guid="901e6645-0c0a-555b-a7e1-a68a6d90a1b3",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Ability(
            title="Metal Transfer",
            game_text="As often as you like during your turn, you may move a Metal Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=metal_transfer(),
            activation=Activations.UNLIMITED,
            condition=has_energy_in_play(PokemonTypes.METAL),
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
