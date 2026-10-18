from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import everyone_laze_around

card = PokemonCardDef(
    guid="dddfa702-5ba0-5b22-818b-b8d531fc552b",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowpoke.Name",
    display_name="Galarian Slowpoke",
    searchable_by=["Galarian Slowpoke", "Basic", "GalarianSlowpoke"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=79,
    abilities=[
        Attack(
            title="Everyone Laze Around",
            game_text="Heal 10 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=everyone_laze_around(10),
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
