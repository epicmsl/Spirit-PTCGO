from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.cel25_effects import VersatilePassive, power_move

card = PokemonCardDef(
    guid="a60794a5-b0ec-5b5d-b140-d6664ee27255",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name",
    display_name="Mew ex",
    searchable_by=["Mew ex", "Basic", "EX", "Mewex"],
    subtypes=["Basic", "EX"],
    collector_number=37,
    set_code="CEL25",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Versatile",
            game_text="Mew ex can use the attacks of all Pok\u00e9mon in play as its own. (You still need the necessary Energy to use each attack.)",
            passive=VersatilePassive(),
        ),
        Attack(
            title="Power Move",
            game_text="Search your deck for an Energy card and attach it to Mew ex. Shuffle your deck afterward. Then, you may switch Mew ex with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=power_move,
        ),
    ],
)
