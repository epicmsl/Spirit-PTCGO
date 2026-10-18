from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.content.definitions import Triggers
from spirit.game.card_effects.cel25_effects import (
    wonder_tag, energy_drive, tapu_cure_gx,
)

card = PokemonCardDef(
    guid="cbbf2d22-b12d-5269-aff4-8d5a14e843ca",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuLeleGX.Name",
    display_name="Tapu Lele-GX",
    searchable_by=["Tapu Lele-GX", "Basic", "GX", "TapuLeleGX"],
    subtypes=["Basic", "GX"],
    collector_number=49,
    set_code="CEL25",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=785,
    abilities=[
        Ability(
            title="Wonder Tag",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=wonder_tag(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Energy Drive",
            game_text="This attack does 20 damage times the amount of Energy attached to both Active Pok\u00e9mon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=energy_drive,
        ),
        Attack(
            title="Tapu Cure GX",
            game_text="Heal all damage from 2 of your Benched Pok\u00e9mon. (You can't use more than 1  attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=tapu_cure_gx,
        ),
    ],
)
