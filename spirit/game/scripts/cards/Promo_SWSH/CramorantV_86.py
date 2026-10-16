from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import beak_catch, spit_shot

card = PokemonCardDef(
    guid="54f6b021-ab98-55f3-a1ce-80c4b620df41",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CramorantV.Name",
    display_name="Cramorant V",
    searchable_by=["Cramorant V", "Basic", "V", "CramorantV"],
    subtypes=["Basic", "V"],
    collector_number=86,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=845,
    abilities=[
        Attack(
            title="Beak Catch",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=beak_catch(2),
        ),
        Attack(
            title="Spit Shot",
            game_text="Discard all Energy from this Pok\u00e9mon. This attack does 160 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=spit_shot(160),
        ),
    ],
)
