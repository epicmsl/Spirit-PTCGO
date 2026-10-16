from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import shadow_cyclone, void_return

card = PokemonCardDef(
    guid="2ca7cad0-32dc-5e5b-b32b-426c51dae169",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroarkV.Name",
    display_name="Hisuian Zoroark V",
    searchable_by=["Hisuian Zoroark V", "Basic", "V", "HisuianZoroarkV"],
    subtypes=["Basic", "V"],
    collector_number=297,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=571,
    abilities=[
        Attack(
            title="Void Return",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={},
            damage=30,
            effect=void_return(),
        ),
        Attack(
            title="Shadow Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=shadow_cyclone(),
        ),
    ],
)
