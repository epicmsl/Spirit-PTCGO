from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import max_thunder_rumble

card = PokemonCardDef(
    guid="7b66260c-a17e-56a6-9d1f-4a7848d5572c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonVMAX.Name",
    display_name="Jolteon VMAX",
    searchable_by=["Jolteon VMAX", "VMAX", "JolteonVMAX"],
    subtypes=["VMAX"],
    collector_number=184,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET]),
    hp=300,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonV.Name",
    family_id=135,
    abilities=[
        Attack(
            title="Max Thunder Rumble",
            game_text="This attack also does 100 damage to 1 of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=max_thunder_rumble(100),
        ),
    ],
)
