from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import bladed_armament, brave_blade

card = PokemonCardDef(
    guid="954274bd-90ef-5d08-9a64-a94f803293a9",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name",
    display_name="Zacian",
    searchable_by=["Zacian", "Restore", "Zacian"],
    subtypes=["Restore"],
    collector_number=135,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.RESTORED,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        Ability(
            title="Bladed Armament",
            game_text="Damage from this Pok\u00e9mon's attacks isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            effect=bladed_armament(),
            passive=bladed_armament(),
        ),
        Attack(
            title="Brave Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=brave_blade(),
            locks_next_turn=True,
        ),
    ],
)
