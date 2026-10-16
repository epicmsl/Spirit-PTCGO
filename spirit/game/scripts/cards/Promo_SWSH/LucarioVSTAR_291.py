from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import aura_star, fighting_knuckle

card = PokemonCardDef(
    guid="ab13a416-5d32-5101-81ed-f0a3cbfe45f2",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioVSTAR.Name",
    display_name="Lucario VSTAR",
    searchable_by=["Lucario VSTAR", "VSTAR", "LucarioVSTAR"],
    subtypes=["VSTAR"],
    collector_number=291,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioV.Name",
    family_id=448,
    abilities=[
        Attack(
            title="Fighting Knuckle",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon , this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=fighting_knuckle(120),
        ),
        Attack(
            title="[VSTAR Power] Aura Star",
            game_text="This attack does 70 damage for each Energy attached to all of your opponent's Pok\u00e9mon. (You can't use more than 1 {VSTAR} Power in a game.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=aura_star(per=70),
            vstar=True,
        ),
    ],
)
