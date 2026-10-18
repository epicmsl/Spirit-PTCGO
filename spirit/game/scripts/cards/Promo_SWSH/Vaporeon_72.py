from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import hydro_pump, watery_shroud

card = PokemonCardDef(
    guid="912e0293-0b4d-5e90-ba9c-3684b038e2e3",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1", "Vaporeon"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Watery Shroud",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage done to this Pok\u00e9mon by attacks (both yours and your opponent's).",
            effect=watery_shroud(),
            passive=watery_shroud(),
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 20 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=hydro_pump(20),
        ),
    ],
)
