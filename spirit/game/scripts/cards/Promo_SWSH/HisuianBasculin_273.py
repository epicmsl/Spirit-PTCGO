from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import submerge_silently, submerge_silently_condition

card = PokemonCardDef(
    guid="d2a047b5-b794-5c91-a66b-f64b082569cd",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculin.Name",
    display_name="Hisuian Basculin",
    searchable_by=["Hisuian Basculin", "Basic", "HisuianBasculin"],
    subtypes=["Basic"],
    collector_number=273,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=550,
    abilities=[
        Attack(
            title="Submerge Silently",
            game_text="You can use this attack only if you go second, and only during your first turn. During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=submerge_silently(),
            condition=submerge_silently_condition,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
