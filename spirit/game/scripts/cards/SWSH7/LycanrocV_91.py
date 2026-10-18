from spirit.game.data_utils import Ability, Attack, Foil, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="f4d6b46b-8a33-5830-b017-880eb992275b",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocV.Name",
    display_name="Lycanroc V",
    searchable_by=["Lycanroc V", "Basic", "V", "LycanrocV"],
    subtypes=["Basic", "V"],
    collector_number=91,
    set_code="SWSH7",
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
            locks_next_turn=True,
        ),
    ],
)