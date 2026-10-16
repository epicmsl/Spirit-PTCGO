from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import diving_swipe, mach_turn

card = PokemonCardDef(
    guid="ba26a7b8-88ce-5397-a04b-cee059b6bc43",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragapult.Name",
    display_name="Dragapult",
    searchable_by=["Dragapult", "Stage 2", "Dragapult"],
    subtypes=["Stage 2"],
    collector_number=132,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    family_id=885,
    abilities=[
        Attack(
            title="Mach Turn",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            effect=mach_turn(),
        ),
        Attack(
            title="Diving Swipe",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=diving_swipe(),
        ),
    ],
)
