from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import iron_tail

card = PokemonCardDef(
    guid="bb5df577-c935-51de-a7f2-babdcf1891b8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.FLATSILVER]),
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=iron_tail(30),
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
