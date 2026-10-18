from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import revenge_blast, soft_wool

card = PokemonCardDef(
    guid="649cdc51-207d-5bef-8d5e-ca012bf1d2b7",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DubwoolV.Name",
    display_name="Dubwool V",
    searchable_by=["Dubwool V", "Basic", "V", "DubwoolV"],
    subtypes=["Basic", "V"],
    collector_number=49,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=832,
    abilities=[
        Ability(
            title="Soft Wool",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=soft_wool(30),
            passive=soft_wool(30),
        ),
        Attack(
            title="Revenge Blast",
            game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=revenge_blast(30),
        ),
    ],
)
