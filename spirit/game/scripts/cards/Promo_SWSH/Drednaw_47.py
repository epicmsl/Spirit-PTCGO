from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import jaw_lock, vise_bite

card = PokemonCardDef(
    guid="1775b452-aefc-5a8f-8aa7-4a470cf3c250",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drednaw.Name",
    display_name="Drednaw",
    searchable_by=["Drednaw", "Stage 1", "Drednaw"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name",
    family_id=833,
    abilities=[
        Attack(
            title="Vise Bite",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=vise_bite(30),
        ),
        Attack(
            title="Jaw Lock",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=jaw_lock(),
        ),
    ],
)
