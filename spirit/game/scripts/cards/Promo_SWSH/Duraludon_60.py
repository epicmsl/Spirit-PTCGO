from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import metal_sharpener

card = PokemonCardDef(
    guid="ef61e124-6f60-5068-9d71-398376004340",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    display_name="Duraludon",
    searchable_by=["Duraludon", "Basic", "Duraludon"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=884,
    abilities=[
        Attack(
            title="Metal Sharpener",
            game_text="Attach a Metal Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=metal_sharpener(),
        ),
        Attack(
            title="Power Beam",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
