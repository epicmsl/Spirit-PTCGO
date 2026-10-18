from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import mad_party

card = PokemonCardDef(
    guid="ecb3b3dc-7df5-5f53-8da7-235c17960f4e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name",
    display_name="Bunnelby",
    searchable_by=["Bunnelby", "Basic", "Bunnelby"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=659,
    abilities=[
        Attack(
            title="Mad Party",
            game_text="This attack does 20 damage for each Pok\u00e9mon in your discard pile that has the Mad Party attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=mad_party(20),
        ),
    ],
)
