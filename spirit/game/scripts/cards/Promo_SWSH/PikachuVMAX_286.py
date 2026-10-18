from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import tail_charge

card = PokemonCardDef(
    guid="a2fca6a6-c046-527c-80d8-7a673e67e14d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVMAX.Name",
    display_name="Pikachu VMAX",
    searchable_by=["Pikachu VMAX", "VMAX", "PikachuVMAX"],
    subtypes=["VMAX"],
    collector_number=286,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVMAX,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Tail Charge",
            game_text="Attach up to 3 Lightning Energy cards from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=tail_charge(3),
        ),
        Attack(
            title="G-Max Thunder",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=250,
        ),
    ],
)
