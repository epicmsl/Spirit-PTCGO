from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import g_max_bombard, grand_falls

card = PokemonCardDef(
    guid="a21c0cad-5975-58b9-9e06-b5da6c811936",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseVMAX.Name",
    display_name="Blastoise VMAX",
    searchable_by=["Blastoise VMAX", "VMAX", "BlastoiseVMAX"],
    subtypes=["VMAX"],
    collector_number=103,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVMAX,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseV.Name",
    family_id=7,
    abilities=[
        Attack(
            title="Grand Falls",
            game_text="Search your deck for up to 3 Water Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=grand_falls(),
        ),
        Attack(
            title="G-Max Bombard",
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 4},
            damage=220,
            effect=g_max_bombard(30, 2),
        ),
    ],
)
