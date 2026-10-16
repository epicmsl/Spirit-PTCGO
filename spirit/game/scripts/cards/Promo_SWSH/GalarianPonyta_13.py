from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import heal_pulse

card = PokemonCardDef(
    guid="a01fc430-539f-50ea-b730-fb48c193ac9c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPonyta.Name",
    display_name="Galarian Ponyta",
    searchable_by=["Galarian Ponyta", "Basic", "GalarianPonyta"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=77,
    abilities=[
        Attack(
            title="Heal Pulse",
            game_text="Heal 30 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_pulse(30),
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
