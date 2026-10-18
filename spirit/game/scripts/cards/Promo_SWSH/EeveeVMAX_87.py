from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import g_max_cuddle

card = PokemonCardDef(
    guid="092f9866-7dd7-512f-9825-578fd15135ae",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeVMAX.Name",
    display_name="Eevee VMAX",
    searchable_by=["Eevee VMAX", "VMAX", "EeveeVMAX"],
    subtypes=["VMAX"],
    collector_number=87,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeV.Name",
    family_id=133,
    abilities=[
        Attack(
            title="G-Max Cuddle",
            game_text="During your opponent's next turn, if the Defending Pok\u00e9mon tries to attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=g_max_cuddle(),
        ),
    ],
)
