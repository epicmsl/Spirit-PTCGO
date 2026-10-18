from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import twinkle_gathering

card = PokemonCardDef(
    guid="78e64ad6-e311-508d-89f2-23db669ab935",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantEevee.Name",
    display_name="Radiant Eevee",
    searchable_by=["Radiant Eevee", "Basic", "Radiant", "RadiantEevee"],
    subtypes=["Basic", "Radiant"],
    collector_number=230,
    set_code="Promo_SWSH",
    rarity=Rarities.RareRadiant,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.RADIANTHOLO]),
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Twinkle Gathering",
            game_text="Search your deck for a number of cards up to the number of different types of Pok\u00e9mon you have in play and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=twinkle_gathering(),
        ),
        Attack(
            title="Boost Dash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
