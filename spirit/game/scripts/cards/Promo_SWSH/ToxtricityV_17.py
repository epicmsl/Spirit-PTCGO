from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import energize_lightning, venom_slap

card = PokemonCardDef(
    guid="460e1b9a-e259-560a-a404-250d94030e68",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ToxtricityV.Name",
    display_name="Toxtricity V",
    searchable_by=["Toxtricity V", "Basic", "V", "ToxtricityV"],
    subtypes=["Basic", "V"],
    collector_number=17,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=849,
    abilities=[
        Attack(
            title="Energize",
            game_text="Attach a Lightning Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=energize_lightning(),
        ),
        Attack(
            title="Venom Slap",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=venom_slap(),
        ),
    ],
)
