from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import primal_turbo

card = PokemonCardDef(
    guid="0e783f72-74bd-5817-aaf6-da7be205dcf8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archeops.Name",
    display_name="Archeops",
    searchable_by=["Archeops", "Stage 2", "Archeops"],
    subtypes=["Stage 2"],
    collector_number=272,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    family_id=566,
    abilities=[
        Ability(
            title="Primal Turbo",
            game_text="Once during your turn, you may search your deck for up to 2 Special Energy cards and attach them to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            effect=primal_turbo(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Speed Wing",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)
