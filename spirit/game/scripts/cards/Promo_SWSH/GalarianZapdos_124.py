from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.promo_swsh_effects import strong_legs_charge, zapper_kick

card = PokemonCardDef(
    guid="e8475f6c-e73f-5dfe-b0d1-3a9dd6c841fa",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZapdos.Name",
    display_name="Galarian Zapdos",
    searchable_by=["Galarian Zapdos", "Basic", "GalarianZapdos"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=145,
    abilities=[
        Ability(
            title="Strong Legs Charge",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach up to 2 Fighting Energy cards from your hand to this Pok\u00e9mon.",
            effect=strong_legs_charge(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Zapper Kick",
            game_text="You may discard all Energy from this Pok\u00e9mon. If you do, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=zapper_kick(),
        ),
    ],
)
