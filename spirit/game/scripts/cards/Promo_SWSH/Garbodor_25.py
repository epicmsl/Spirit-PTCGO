from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import poisonous_puddle

card = PokemonCardDef(
    guid="d133f532-0354-5fba-9f44-09fac117ad59",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Garbodor"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Ability(
            title="Poisonous Puddle",
            game_text="Once during your turn, if a Stadium is in play, you may make your opponent's Active Pok\u00e9mon Poisoned.",
            effect=poisonous_puddle(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Sludge Bomb",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
