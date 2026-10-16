from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.content.definitions import Triggers
from spirit.game.card_effects.cel25_effects import dark_ray, feint_attack

card = PokemonCardDef(
    guid="3c49b363-bc8d-5f3a-afbd-6497739080a1",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon \u2606",
    searchable_by=["Umbreon \u2606", "Basic", "Umbreon"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="CEL25",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=197,
    abilities=[
        Ability(
            title="Dark Ray",
            game_text="Once during your turn, when you put Umbreon \u2606 from your hand onto your Bench, you may choose 1 card from your opponent's hand without looking and discard it.",
            effect=dark_ray,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Feint Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=feint_attack,
        ),
    ],
)
