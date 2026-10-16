from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import explosive_fire, star_blaze

card = PokemonCardDef(
    guid="c0cea90e-bc8a-5b47-8e68-c8579dbde77e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardVSTAR.Name",
    display_name="Charizard VSTAR",
    searchable_by=["Charizard VSTAR", "VSTAR", "CharizardVSTAR"],
    subtypes=["VSTAR"],
    collector_number=262,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=280,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardV.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Explosive Fire",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=explosive_fire(100),
        ),
        Attack(
            title="[VSTAR Power] Star Blaze",
            game_text="Discard 2 Energy from this Pok\u00e9mon. (You can't use more than 1 {VSTAR} Power in a game.)",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=320,
            effect=star_blaze(),
            vstar=True,
        ),
    ],
)
