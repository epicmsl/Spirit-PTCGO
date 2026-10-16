from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import hyper_beam

card = PokemonCardDef(
    guid="3bad168d-571b-5853-8575-9ce78a4cd12c",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteV.Name",
    display_name="Dragonite V",
    searchable_by=["Dragonite V", "Basic", "V", "DragoniteV"],
    subtypes=["Basic", "V"],
    collector_number=235,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=149,
    abilities=[
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=60,
            effect=hyper_beam(),
        ),
        Attack(
            title="Buster Tail",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)
