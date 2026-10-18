from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import fire_spin

card = PokemonCardDef(
    guid="d5a9f9db-e9da-5c16-bde8-88e389628576",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardVMAX.Name",
    display_name="Charizard VMAX",
    searchable_by=["Charizard VMAX", "VMAX", "CharizardVMAX"],
    subtypes=["VMAX"],
    collector_number=261,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=330,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardV.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
        Attack(
            title="G-Max Wildfire",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 2},
            damage=300,
            effect=fire_spin(2),
        ),
    ],
)
