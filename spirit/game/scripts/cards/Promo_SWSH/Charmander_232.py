from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import tail_on_fire

card = PokemonCardDef(
    guid="6199ee02-3378-5c56-845d-f2256c81f478",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=232,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Attack(
            title="Tail on Fire",
            game_text="Search your deck for a Fire Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=tail_on_fire(),
        ),
    ],
)
