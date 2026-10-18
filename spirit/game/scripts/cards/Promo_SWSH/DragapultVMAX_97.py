from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import max_phantom
from spirit.game.card_effects.pokemon import shred

card = PokemonCardDef(
    guid="ebf136b1-273c-5b89-92c0-fa04e5ba5b2e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragapultVMAX.Name",
    display_name="Dragapult VMAX",
    searchable_by=["Dragapult VMAX", "VMAX", "DragapultVMAX"],
    subtypes=["VMAX"],
    collector_number=97,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET]),
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DragapultV.Name",
    family_id=887,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            effect=shred,
        ),
        Attack(
            title="Max Phantom",
            game_text="Put 5 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            effect=max_phantom(5),
        ),
    ],
)
