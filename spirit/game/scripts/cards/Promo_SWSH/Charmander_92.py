from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import collect

card = PokemonCardDef(
    guid="5ad4da58-cd78-5910-9fcd-45545a2b5577",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.FIRE: 1},
            effect=collect(1),
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)
