from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import raid

card = PokemonCardDef(
    guid="feeeee04-4274-55d7-b307-5397dee20160",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Attack(
            title="Raid",
            game_text="If this Pok\u00e9mon evolved from Luxio during this turn, this attack does 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            damage_operator="+",
            effect=raid(100),
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
