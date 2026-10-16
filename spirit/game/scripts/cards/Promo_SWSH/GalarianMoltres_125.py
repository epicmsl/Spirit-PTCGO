from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.promo_swsh_effects import fiery_wrath, malevolent_charge

card = PokemonCardDef(
    guid="5a6aea63-0b1a-583d-a007-1088f8dd3afa",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMoltres.Name",
    display_name="Galarian Moltres",
    searchable_by=["Galarian Moltres", "Basic", "GalarianMoltres"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=146,
    abilities=[
        Ability(
            title="Malevolent Charge",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach up to 2 Darkness Energy cards from your hand to this Pok\u00e9mon.",
            effect=malevolent_charge(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Fiery Wrath",
            game_text="This attack does 50 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=fiery_wrath(50),
        ),
    ],
)
