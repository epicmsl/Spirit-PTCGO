from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import beatdown_smash, slow_ballad

card = PokemonCardDef(
    guid="56be8f2d-869e-572f-8d3e-35243edd7437",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightToxtricity.Name",
    display_name="Light Toxtricity",
    searchable_by=["Light Toxtricity", "Stage 1", "LightToxtricity"],
    subtypes=["Stage 1"],
    collector_number=137,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Slow Ballad",
            game_text="Heal 30 damage from both Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=slow_ballad(30),
        ),
        Attack(
            title="Beatdown Smash",
            game_text="During your next turn, this Pok\u00e9mon can't use Beatdown Smash.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=beatdown_smash(),
            locks_next_turn=True,
        ),
    ],
)
