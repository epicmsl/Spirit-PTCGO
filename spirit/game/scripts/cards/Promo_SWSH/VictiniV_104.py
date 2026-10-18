from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import energy_burst, spreading_flames

card = PokemonCardDef(
    guid="b70082f2-e1f4-51c6-8f0e-af5b11216590",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniV.Name",
    display_name="Victini V",
    searchable_by=["Victini V", "Basic", "V", "VictiniV"],
    subtypes=["Basic", "V"],
    collector_number=104,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="Spreading Flames",
            game_text="Attach up to 3 Fire Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=spreading_flames(3),
        ),
        Attack(
            title="Energy Burst",
            game_text="This attack does 30 damage for each Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="x",
            effect=energy_burst(30),
        ),
    ],
)
