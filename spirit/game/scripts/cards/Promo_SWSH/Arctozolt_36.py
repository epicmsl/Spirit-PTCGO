from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.promo_swsh_effects import biting_whirlpool

card = PokemonCardDef(
    guid="89a05c93-3397-5cf8-9701-5082cd781333",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arctozolt.Name",
    display_name="Arctozolt",
    searchable_by=["Arctozolt", "Stage 1", "Arctozolt"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RareFossil.Name",
    family_id=881,
    abilities=[
        Ability(
            title="Biting Whirlpool",
            game_text="Whenever your opponent attaches an Energy card from their hand to 1 of their Pok\u00e9mon, put 2 damage counters on that Pok\u00e9mon.",
            effect=biting_whirlpool,
            trigger=Triggers.ON_ENERGY_ATTACHED,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
