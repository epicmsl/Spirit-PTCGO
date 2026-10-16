from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import electro_wheel, spark

card = PokemonCardDef(
    guid="9f4d6d46-9dca-57f8-9a07-61417341ccae",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoV.Name",
    display_name="Morpeko V",
    searchable_by=["Morpeko V", "Basic", "V", "MorpekoV"],
    subtypes=["Basic", "V"],
    collector_number=56,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=877,
    abilities=[
        Attack(
            title="Spark",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=spark(20),
        ),
        Attack(
            title="Electro Wheel",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, switch it with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=electro_wheel(),
        ),
    ],
)
