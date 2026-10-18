from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import energize, thunder

card = PokemonCardDef(
    guid="329dac28-aa79-5d8f-bb7b-4ee20debcc05",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon",
    searchable_by=["Jolteon", "Stage 1", "Jolteon"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Energize",
            game_text="Attach a Lightning Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=energize(),
        ),
        Attack(
            title="Thunder",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=thunder(30),
        ),
    ],
)
