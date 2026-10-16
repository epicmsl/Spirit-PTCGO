from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID, TrainerType
from spirit.game.card_effects.support_common import search_to_hand

def _is_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES
_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)
card = PokemonCardDef(guid='80ee621e-7bd1-5c36-8bf9-709e258f2668', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Greedent.Name', display_name='Greedent', searchable_by=['Greedent', 'Stage 1', 'Greedent'], subtypes=['Stage 1'], collector_number=173, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=120, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name', family_id=819, abilities=[Ability(title='Greedy Tail', game_text='Once during your turn, you may search your deck for a Pokémon Tool card, reveal it, and put it into your hand. Then, shuffle your deck.', effect=search_to_hand(_is_tool_card, count=1, minimum=0, reveal=True, prompt='Choose a Pokémon Tool card to reveal and put into your hand.'), activation=Activations.ONCE_PER_TURN), Attack(title='Tail Smack', cost={PokemonTypes.COLORLESS: 3}, damage=80)])
