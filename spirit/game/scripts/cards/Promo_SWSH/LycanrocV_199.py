from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import crashing_fangs

card = PokemonCardDef(
    guid="9f69010f-d11a-52bd-89e8-9f71a56230b9",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocV.Name",
    display_name="Lycanroc V",
    searchable_by=["Lycanroc V", "Basic", "V", "LycanrocV"],
    subtypes=["Basic", "V"],
    collector_number=199,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=745,
    abilities=[
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Crashing Fangs",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=crashing_fangs(),
            locks_next_turn=True,
        ),
    ],
)
