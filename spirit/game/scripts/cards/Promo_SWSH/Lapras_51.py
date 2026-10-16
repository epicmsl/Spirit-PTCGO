from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import aqua_wash

card = PokemonCardDef(
    guid="a3ab5742-5663-598f-890f-f76b8c75e161",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Aqua Wash",
            game_text="You may put 2 Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.WATER: 4},
            damage=70,
            effect=aqua_wash(2),
        ),
    ],
)
