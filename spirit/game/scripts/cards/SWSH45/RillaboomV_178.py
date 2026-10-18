from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.support_common import search_to_bench

def _is_basic_grass_pokemon(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_pokemon(card) and PokemonTypes.GRASS.value in types
card = PokemonCardDef(guid='bf2de663-aa7d-5345-b566-3def3b29aabf', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomV.Name', display_name='Rillaboom V', searchable_by=['Rillaboom V', 'Basic', 'V', 'RillaboomV'], subtypes=['Basic', 'V'], collector_number=178, set_code='SWSH45', rarity=Rarities.RareHoloV, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=220, elements=[PokemonTypes.GRASS], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.FIRE, family_id=812, abilities=[Attack(title='Forest Feast', game_text='Search your deck for up to 2 Basic Grass Pokémon and put them onto your Bench. Then, shuffle your deck.', cost={PokemonTypes.GRASS: 1}, effect=search_to_bench(predicate=_is_basic_grass_pokemon, count=2)), Attack(title='Wood Hammer', game_text='This Pokémon also does 30 damage to itself.', cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1}, damage=220, effect=recoil_attack(30))])
