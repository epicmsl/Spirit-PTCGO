from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import brave_buddies, collect

card = PokemonCardDef(
    guid="8719886b-0440-55f5-a18c-130f351b4ec1",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeV.Name",
    display_name="Eevee V",
    searchable_by=["Eevee V", "Basic", "V", "EeveeV"],
    subtypes=["Basic", "V"],
    collector_number=65,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloV,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SUNPILLAR]),
    hp=190,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=collect(3),
        ),
        Attack(
            title="Brave Buddies",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=brave_buddies(80),
        ),
    ],
)
