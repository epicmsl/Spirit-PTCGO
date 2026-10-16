from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import raging_repeated_strike, wood_drain

card = PokemonCardDef(
    guid="d185d2e8-fd41-5113-8027-6131c593e1c7",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rillaboom.Name",
    display_name="Rillaboom",
    searchable_by=["Rillaboom", "Stage 2", "Rillaboom"],
    subtypes=["Stage 2"],
    collector_number=277,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    family_id=810,
    abilities=[
        Attack(
            title="Wood Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=wood_drain(30),
        ),
        Attack(
            title="Raging Repeated Strike",
            game_text="Discard any amount of Energy from your Pok\u00e9mon. This attack does 30 more damage for each card you discarded in this way.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=raging_repeated_strike(30),
        ),
    ],
)
