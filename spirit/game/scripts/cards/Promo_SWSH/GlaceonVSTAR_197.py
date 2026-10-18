from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import crystal_star, icicle_shot

card = PokemonCardDef(
    guid="2c87a5a0-cad0-595c-a5d2-6f4385b0c7f4",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonVSTAR.Name",
    display_name="Glaceon VSTAR",
    searchable_by=["Glaceon VSTAR", "VSTAR", "GlaceonVSTAR"],
    subtypes=["VSTAR"],
    collector_number=197,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVSTAR,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name",
    family_id=471,
    abilities=[
        Attack(
            title="Icicle Shot",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=icicle_shot(),
        ),
        Attack(
            title="[VSTAR Power] Crystal Star",
            game_text="During your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon. (You can't use more than 1 {VSTAR} Power in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=crystal_star(),
            vstar=True,
        ),
    ],
)
