from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.content.definitions import Triggers
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.cel25_effects import bright_look

card = PokemonCardDef(
    guid="7e5e650c-06a1-5bf9-8b4a-86c4a6620ca2",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LuxrayGL.Name",
    display_name="Luxray GL",
    searchable_by=["Luxray GL", "Restore", "LuxrayGL"],
    subtypes=["Restore"],
    collector_number=41,
    set_code="CEL25",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.RESTORED,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LuxrayGL.Name",
    family_id=403,
    abilities=[
        Ability(
            title="Bright Look",
            game_text="Once during your turn when you put Luxray GL LV.X from your hand onto your Active Luxray GL, you may switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon.",
            effect=bright_look,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Flash Impact",
            game_text="Does 30 damage to 1 of your Pok\u00e9mon, and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=snipe_attack(30, pool="any", side="mine", also_base=True,
                                apply_modifiers=False),
        ),
    ],
)
