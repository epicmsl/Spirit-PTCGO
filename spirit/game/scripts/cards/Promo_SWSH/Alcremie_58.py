from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import decorate, draining_kiss

card = PokemonCardDef(
    guid="dac74df6-39c8-52be-bb36-c5c96c958ea6",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremie.Name",
    display_name="Alcremie",
    searchable_by=["Alcremie", "Stage 1", "Alcremie"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=868,
    abilities=[
        Attack(
            title="Decorate",
            game_text="Attach as many basic Energy cards as you like from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=decorate(),
        ),
        Attack(
            title="Draining Kiss",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=draining_kiss(30),
        ),
    ],
)
