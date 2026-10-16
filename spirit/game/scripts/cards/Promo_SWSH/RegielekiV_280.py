from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import lightning_wall, switching_bolt

card = PokemonCardDef(
    guid="adbf5ecf-bfba-5aee-bde0-cf4d8ece6e91",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegielekiV.Name",
    display_name="Regieleki V",
    searchable_by=["Regieleki V", "Basic", "V", "RegielekiV"],
    subtypes=["Basic", "V"],
    collector_number=280,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=894,
    abilities=[
        Attack(
            title="Switching Bolt",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=switching_bolt(),
        ),
        Attack(
            title="Lightning Wall",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 100 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=lightning_wall(100),
        ),
    ],
)
