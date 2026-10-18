from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import pin_missile, thunder_spear

card = PokemonCardDef(
    guid="9de2f23d-aac6-59d3-a51c-04473256073b",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonV.Name",
    display_name="Jolteon V",
    searchable_by=["Jolteon V", "Basic", "V", "JolteonV"],
    subtypes=["Basic", "V"],
    collector_number=183,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=135,
    abilities=[
        Attack(
            title="Thunder Spear",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=thunder_spear(20),
        ),
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=pin_missile(60, 4),
        ),
    ],
)
