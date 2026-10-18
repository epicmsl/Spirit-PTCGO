from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import dark_mastery, wily_stance

card = PokemonCardDef(
    guid="2d01b897-4c0d-56d8-a3e6-37811c079fdd",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSamurott.Name",
    display_name="Hisuian Samurott",
    searchable_by=["Hisuian Samurott", "Stage 2", "HisuianSamurott"],
    subtypes=["Stage 2"],
    collector_number=207,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    family_id=501,
    abilities=[
        Ability(
            title="Wily Stance",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 3 cards.",
            effect=wily_stance(3),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Dark Mastery",
            game_text="This attack does 20 more damage for each Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=dark_mastery(20),
        ),
    ],
)
