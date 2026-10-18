from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import mist_slash

from spirit.game.data_utils import Triggers
from spirit.game.card_effects.promo_swsh_effects import shadow_knife

card = PokemonCardDef(
    guid="8c8cee0a-abed-5f6e-ac47-53132aaa999f",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name",
    display_name="Greninja \u2606",
    searchable_by=["Greninja \u2606", "Basic", "Greninja"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=658,
    abilities=[
        Ability(
            title="[Pok\u00e9-POWER] Shadow Knife",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may put 1 damage counter on 1 of your opponent's Pok\u00e9mon.",
            effect=shadow_knife(1),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Mist Slash",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=mist_slash(),
        ),
    ],
)
