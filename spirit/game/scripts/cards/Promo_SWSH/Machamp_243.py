from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import crisis_muscles, strong_arm_lariat

card = PokemonCardDef(
    guid="63c3187c-2b70-532b-998f-6341f2efc984",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=243,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Crisis Muscles",
            game_text="If your opponent has 3 or fewer Prize cards remaining, this Pok\u00e9mon gets +150 HP.",
            effect=crisis_muscles(150),
            passive=crisis_muscles(150),
        ),
        Attack(
            title="Strong-Arm Lariat",
            game_text="You may do 100 more damage. If you do, during your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=100,
            damage_operator="+",
            effect=strong_arm_lariat(100),
        ),
    ],
)
