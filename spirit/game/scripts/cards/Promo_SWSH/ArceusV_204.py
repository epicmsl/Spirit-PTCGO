from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import trinity_charge

card = PokemonCardDef(
    guid="3b24d983-77bf-5bed-a0d5-ad5c6c084f4f",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusV.Name",
    display_name="Arceus V",
    searchable_by=["Arceus V", "Basic", "V", "ArceusV"],
    subtypes=["Basic", "V"],
    collector_number=204,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Attack(
            title="Trinity Charge",
            game_text="Search your deck for up to 3 basic Energy cards and attach them to your Pok\u00e9mon V in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=trinity_charge(),
        ),
        Attack(
            title="Power Edge",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
