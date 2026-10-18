from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import hydro_break, rule_the_region

card = PokemonCardDef(
    guid="e7040f08-7441-5d25-b482-04332ba9037b",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormePalkiaV.Name",
    display_name="Origin Forme Palkia V",
    searchable_by=["Origin Forme Palkia V", "Basic", "V", "OriginFormePalkiaV"],
    subtypes=["Basic", "V"],
    collector_number=253,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=484,
    abilities=[
        Attack(
            title="Rule the Region",
            game_text="Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=rule_the_region(),
        ),
        Attack(
            title="Hydro Break",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=hydro_break(),
            locks_next_turn=True,
        ),
    ],
)
