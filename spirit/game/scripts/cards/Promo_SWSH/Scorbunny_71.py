from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import me_first

card = PokemonCardDef(
    guid="9003d6c7-a648-56a7-9247-7d81b5518119",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    display_name="Scorbunny",
    searchable_by=["Scorbunny", "Basic", "Scorbunny"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=813,
    abilities=[
        Attack(
            title="Me First",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=me_first(),
        ),
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
        ),
    ],
)
