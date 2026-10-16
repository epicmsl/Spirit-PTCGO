from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import single_strike_roar

card = PokemonCardDef(
    guid="8295881b-8cd3-56e8-abda-64ed5fa90d69",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Ability(
            title="Single Strike Roar",
            game_text="Once during your turn, you may search your deck for a Single Strike Energy card and attach it to 1 of your Single Strike Pok\u00e9mon. Then, shuffle your deck. If you attached Energy to a Pok\u00e9mon in this way, put 2 damage counters on that Pok\u00e9mon.",
            effect=single_strike_roar(),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
