from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import psychic_javelin, star_force

card = PokemonCardDef(
    guid="7ea785da-6b3d-518d-a647-f0901c0a22d8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysVSTAR.Name",
    display_name="Deoxys VSTAR",
    searchable_by=["Deoxys VSTAR", "VSTAR", "DeoxysVSTAR"],
    subtypes=["VSTAR"],
    collector_number=268,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVSTAR,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name",
    family_id=386,
    abilities=[
        Attack(
            title="Psychic Javelin",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pok\u00e9mon . (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=psychic_javelin(60),
        ),
        Attack(
            title="[VSTAR Power] Star Force",
            game_text="This attack does 60 damage for each Energy attached to both Active Pok\u00e9mon. (You can't use more than 1 {VSTAR} Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator="x",
            effect=star_force(per=60),
            vstar=True,
        ),
    ],
)
