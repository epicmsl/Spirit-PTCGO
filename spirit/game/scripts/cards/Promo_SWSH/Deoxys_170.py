from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import photon_boost

card = PokemonCardDef(
    guid="f1d2e00f-290e-571d-bf50-f4fb878b70a2",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=170,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=386,
    abilities=[
        Attack(
            title="Photon Boost",
            game_text="If this Pok\u00e9mon has any Fusion Strike Energy attached, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=photon_boost(80),
        ),
    ],
)
