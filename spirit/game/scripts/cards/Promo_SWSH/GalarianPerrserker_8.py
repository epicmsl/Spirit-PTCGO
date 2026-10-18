from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import steely_spirit

card = PokemonCardDef(
    guid="8efef358-5965-5987-b1d9-a7e67b817bd8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPerrserker.Name",
    display_name="Galarian Perrserker",
    searchable_by=["Galarian Perrserker", "Stage 1", "GalarianPerrserker"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMeowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Steely Spirit",
            game_text="Your Metal Pok\u00e9mon's attacks do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=steely_spirit(20),
            passive=steely_spirit(20),
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
