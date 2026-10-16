from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import lightning_blast

card = PokemonCardDef(
    guid="3bb93b88-88e8-5766-be63-3cf702e9f129",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    display_name="Pikachu V",
    searchable_by=["Pikachu V", "Basic", "V", "PikachuV"],
    subtypes=["Basic", "V"],
    collector_number=198,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Lightning Blast",
            game_text="You may discard all Lightning Energy from this Pok\u00e9mon. If you do, this attack does 120 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=lightning_blast(120),
        ),
    ],
)
