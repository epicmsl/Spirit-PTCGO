from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import fire_spin

card = PokemonCardDef(
    guid="d48700a3-b628-5b82-bab3-b28bad641e2a",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardV.Name",
    display_name="Charizard V",
    searchable_by=["Charizard V", "Basic", "V", "CharizardV"],
    subtypes=["Basic", "V"],
    collector_number=50,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=fire_spin(2),
        ),
    ],
)
