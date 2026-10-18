from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import max_drain, protective_dna

card = PokemonCardDef(
    guid="5414dad3-2ea9-52cc-a2fa-b0b9ffa0c7ef",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysVMAX.Name",
    display_name="Deoxys VMAX",
    searchable_by=["Deoxys VMAX", "VMAX", "DeoxysVMAX"],
    subtypes=["VMAX"],
    collector_number=267,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVMAX,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=330,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name",
    family_id=386,
    abilities=[
        Ability(
            title="Protective DNA",
            game_text="All of your Pok\u00e9mon take 30 less damage from attacks from your opponent's Pok\u00e9mon {VSTAR} (after applying Weakness and Resistance).",
            effect=protective_dna(30),
            passive=protective_dna(30),
        ),
        Attack(
            title="Max Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=max_drain(30),
        ),
    ],
)
