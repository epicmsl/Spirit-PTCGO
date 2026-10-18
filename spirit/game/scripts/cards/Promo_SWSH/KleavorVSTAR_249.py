from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import axe_break, rampaging_star

card = PokemonCardDef(
    guid="beef33c4-d9dd-533d-8237-8fbb0bc69b50",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KleavorVSTAR.Name",
    display_name="Kleavor VSTAR",
    searchable_by=["Kleavor VSTAR", "VSTAR", "KleavorVSTAR"],
    subtypes=["VSTAR"],
    collector_number=249,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVSTAR,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KleavorV.Name",
    family_id=900,
    abilities=[
        Attack(
            title="Axe Break",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pok\u00e9mon V. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=axe_break(60),
        ),
        Attack(
            title="[VSTAR Power] Rampaging Star",
            game_text="This attack does 30 damage for each Pok\u00e9mon in your discard pile. (You can't use more than 1 {VSTAR} Power in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="x",
            effect=rampaging_star(per=30),
            vstar=True,
        ),
    ],
)
