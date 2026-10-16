from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import fireball_shot, crisis_power_passive

card = PokemonCardDef(
    guid="b18b768a-f9d3-563b-9776-0e681f8a99a8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinderace.Name",
    display_name="Cinderace",
    searchable_by=["Cinderace", "Stage 2", "Cinderace"],
    subtypes=["Stage 2"],
    collector_number=278,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    family_id=813,
    abilities=[
        Ability(
            title="Crisis Power",
            game_text="This Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon for each Prize card your opponent has taken (before applying Weakness and Resistance).",
            effect=crisis_power_passive(30),
            passive=crisis_power_passive(30),
        ),
        Attack(
            title="Fireball Shot",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=fireball_shot(),
            locks_next_turn=True,
        ),
    ],
)
