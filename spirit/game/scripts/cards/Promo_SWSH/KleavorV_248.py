from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import axe_slash

card = PokemonCardDef(
    guid="056ce1b2-4282-5864-b91e-e34445b0df61",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KleavorV.Name",
    display_name="Kleavor V",
    searchable_by=["Kleavor V", "Basic", "V", "KleavorV"],
    subtypes=["Basic", "V"],
    collector_number=248,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=900,
    abilities=[
        Attack(
            title="Cut",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Axe Slash",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=axe_slash(),
        ),
    ],
)
