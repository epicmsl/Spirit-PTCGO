from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import mad_party

card = PokemonCardDef(
    guid="e8ca2ff8-5759-5449-84e6-5f3a4f080872",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=702,
    abilities=[
        Attack(
            title="Mad Party",
            game_text="This attack does 20 damage for each Pok\u00e9mon in your discard pile that has the Mad Party attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=mad_party(20),
        ),
    ],
)
