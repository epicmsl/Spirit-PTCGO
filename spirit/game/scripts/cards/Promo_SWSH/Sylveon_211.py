from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import symphony_whip, time_out_kick

card = PokemonCardDef(
    guid="cf9e4f39-0da2-5472-82ab-36b35459a6c4",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name",
    display_name="Sylveon",
    searchable_by=["Sylveon", "Stage 1", "Sylveon"],
    subtypes=["Stage 1"],
    collector_number=211,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Time Out Kick",
            game_text="You may put an Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=time_out_kick(1),
        ),
        Attack(
            title="Symphony Whip",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 70 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=symphony_whip(70),
        ),
    ],
)
