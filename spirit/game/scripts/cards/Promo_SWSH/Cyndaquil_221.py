from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import charge_energy

card = PokemonCardDef(
    guid="38e43ceb-0072-5f05-bdb2-7e0d8e25e06d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name",
    display_name="Cyndaquil",
    searchable_by=["Cyndaquil", "Basic", "Cyndaquil"],
    subtypes=["Basic"],
    collector_number=221,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=155,
    abilities=[
        Attack(
            title="Charge Energy",
            game_text="Search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=charge_energy(),
        ),
        Attack(
            title="Live Coal",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
