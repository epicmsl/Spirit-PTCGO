from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import circle_circuit

card = PokemonCardDef(
    guid="e0d7d96a-1875-55ea-98ad-7918113dd20a",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name",
    display_name="Pikachu V",
    searchable_by=["Pikachu V", "Basic", "V", "PikachuV"],
    subtypes=["Basic", "V"],
    collector_number=63,
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
            title="Pika Ball",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
        Attack(
            title="Circle Circuit",
            game_text="This attack does 30 damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            damage_operator="x",
            effect=circle_circuit(30),
        ),
    ],
)
