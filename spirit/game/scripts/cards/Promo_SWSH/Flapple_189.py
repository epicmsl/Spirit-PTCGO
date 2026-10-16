from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import corrosive_acid, flight_up

card = PokemonCardDef(
    guid="0779482e-fa83-500c-9d76-ef178fc1a2a4",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flapple.Name",
    display_name="Flapple",
    searchable_by=["Flapple", "Stage 1", "Flapple"],
    subtypes=["Stage 1"],
    collector_number=189,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Flight Up",
            game_text="Attach up to 3 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            effect=flight_up(3),
        ),
        Attack(
            title="Corrosive Acid",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=70,
            effect=corrosive_acid(),
        ),
    ],
)
