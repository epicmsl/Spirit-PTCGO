from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw

card = PokemonCardDef(
    guid="1e816dac-1655-5b0e-8314-c26ebe145e69",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Basic", "Cleffa"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=173,
    abilities=[
        Attack(
            title="Eeeeeeek",
            game_text="Shuffle your hand into your deck, then draw 7 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=shuffle_hand_into_deck_draw(7),
        ),
    ],
)
