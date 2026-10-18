from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import carry_off

card = PokemonCardDef(
    guid="ff134d03-3f73-5e77-adc9-ba18633325fb",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    display_name="Noctowl",
    searchable_by=["Noctowl", "Stage 1", "Noctowl"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    family_id=163,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Carry Off",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. They shuffle that Pok\u00e9mon and all attached cards into their deck. Then, shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=carry_off(),
        ),
    ],
)
