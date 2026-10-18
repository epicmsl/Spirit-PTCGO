from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.promo_swsh_effects import cruel_charge, psylaser

card = PokemonCardDef(
    guid="ce80a7aa-4375-5f6a-b5e3-fac86890b8d0",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianArticuno.Name",
    display_name="Galarian Articuno",
    searchable_by=["Galarian Articuno", "Basic", "GalarianArticuno"],
    subtypes=["Basic"],
    collector_number=282,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.RAINBOW]),
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Cruel Charge",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach up to 2 Psychic Energy cards from your hand to this Pok\u00e9mon.",
            effect=cruel_charge(PokemonTypes.PSYCHIC, 2),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Psylaser",
            game_text="Discard all Psychic Energy from this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=psylaser(120),
        ),
    ],
)
