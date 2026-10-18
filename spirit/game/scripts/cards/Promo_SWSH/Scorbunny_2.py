from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import super_singe

card = PokemonCardDef(
    guid="90c29d43-a827-5bb6-b82a-ba4d4fbe4d5e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    display_name="Scorbunny",
    searchable_by=["Scorbunny", "Basic", "Scorbunny"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=813,
    abilities=[
        Attack(
            title="Super Singe",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=super_singe(),
        ),
    ],
)
