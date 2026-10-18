from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import filch, wet_claw

card = PokemonCardDef(
    guid="9cd6c2c6-7c73-5e5d-a4d0-d2bfc328362e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic", "Mimikyu"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=778,
    abilities=[
        Attack(
            title="Filch",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=filch(2),
        ),
        Attack(
            title="Wet Claw",
            game_text="Put an Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=wet_claw(1),
        ),
    ],
)
