from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import defense_curl

card = PokemonCardDef(
    guid="3ed6618f-e4c2-5bc0-b5ec-04fbf0e7dd4a",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    display_name="Wooloo",
    searchable_by=["Wooloo", "Basic", "Wooloo"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=831,
    abilities=[
        Attack(
            title="Defense Curl",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=defense_curl(),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
