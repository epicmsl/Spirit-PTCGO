from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import volt_tackle

card = PokemonCardDef(
    guid="e4708db1-82a8-5948-8dd8-d5948dea7867",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    display_name="Pikachu V",
    searchable_by=["Pikachu V", "Basic", "V", "PikachuV"],
    subtypes=["Basic", "V"],
    collector_number=145,
    set_code="Promo_SWSH",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWHOLO]),
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Volt Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=volt_tackle(30),
        ),
    ],
)
