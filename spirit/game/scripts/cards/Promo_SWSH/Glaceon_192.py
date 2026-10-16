from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import frosty_typhoon, hail

card = PokemonCardDef(
    guid="7ac38c20-da82-5bb9-bb09-3be2e2b53aaa",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name",
    display_name="Glaceon",
    searchable_by=["Glaceon", "Stage 1", "Glaceon"],
    subtypes=["Stage 1"],
    collector_number=192,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Hail",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=hail(20),
        ),
        Attack(
            title="Frosty Typhoon",
            game_text="During your next turn, this Pok\u00e9mon can't use Frosty Typhoon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=frosty_typhoon(),
            locks_next_turn=True,
        ),
    ],
)
