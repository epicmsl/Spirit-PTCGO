from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import flamethrower

card = PokemonCardDef(
    guid="4b0a0bbf-f27b-568d-b214-b374676598fe",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LancesCharizardV.Name",
    display_name="Lance's Charizard V",
    searchable_by=["Lance's Charizard V", "Basic", "V", "LancesCharizardV"],
    subtypes=["Basic", "V"],
    collector_number=133,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=flamethrower(),
        ),
    ],
)
