from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import transfer_break

card = PokemonCardDef(
    guid="9593379b-b13b-5ad5-ae83-52d36ddc994e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoV.Name",
    display_name="Mewtwo V",
    searchable_by=["Mewtwo V", "Basic", "V", "MewtwoV"],
    subtypes=["Basic", "V"],
    collector_number=223,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Transfer Break",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=transfer_break(),
        ),
    ],
)
