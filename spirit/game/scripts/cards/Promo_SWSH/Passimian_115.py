from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import fling, throwing_coach

card = PokemonCardDef(
    guid="159a98a5-446c-5861-a3c6-25cf802c4a70",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name",
    display_name="Passimian",
    searchable_by=["Passimian", "Basic", "Passimian"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=766,
    abilities=[
        Ability(
            title="Throwing Coach",
            game_text="Your Rapid Strike Pok\u00e9mon's attacks do 30 more damage to your opponent's Benched Pok\u00e9mon and Benched Pok\u00e9mon GX Attack (before applying Weakness and Resistance). You can't apply more than 1 Throwing Coach Ability at a time.",
            effect=throwing_coach(30),
            passive=throwing_coach(30),
        ),
        Attack(
            title="Fling",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=fling(20),
        ),
    ],
)
