from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import aura_sphere_volley, roaring_resolve

card = PokemonCardDef(
    guid="118ac5b1-d346-5838-9ae5-b8b1faad7554",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=186,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Ability(
            title="Roaring Resolve",
            game_text="Once during your turn, you may put 2 damage counters on this Pok\u00e9mon. If you do, search your deck for a Fighting Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            effect=roaring_resolve(2),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Aura Sphere Volley",
            game_text="Discard all Fighting Energy from this Pok\u00e9mon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=10,
            damage_operator="+",
            effect=aura_sphere_volley(60),
        ),
    ],
)
