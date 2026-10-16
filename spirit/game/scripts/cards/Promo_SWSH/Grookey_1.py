from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="29be4a57-9cf7-5a7c-aaa5-e2490e71ca63",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name",
    display_name="Grookey",
    searchable_by=["Grookey", "Basic", "Grookey"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=810,
    abilities=[
        Attack(
            title="Branch Poke",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
