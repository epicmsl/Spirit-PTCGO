from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import g_max_bombard, smash_turn

card = PokemonCardDef(
    guid="c9987265-71d5-55c6-b84b-f37dea664af9",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BoltundV.Name",
    display_name="Boltund V",
    searchable_by=["Boltund V", "Basic", "V", "BoltundV"],
    subtypes=["Basic", "V"],
    collector_number=219,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=836,
    abilities=[
        Attack(
            title="Smash Turn",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=smash_turn(),
        ),
        Attack(
            title="Electrobullet",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=g_max_bombard(30, 1),
        ),
    ],
)
