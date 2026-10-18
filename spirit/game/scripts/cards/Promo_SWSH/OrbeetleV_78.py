from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import mysterious_wave, strafe

card = PokemonCardDef(
    guid="e48fab0b-8db8-52aa-861f-38163b5b927c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OrbeetleV.Name",
    display_name="Orbeetle V",
    searchable_by=["Orbeetle V", "Basic", "V", "OrbeetleV"],
    subtypes=["Basic", "V"],
    collector_number=78,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=826,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=strafe(),
        ),
        Attack(
            title="Mysterious Wave",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=mysterious_wave(30),
        ),
    ],
)
