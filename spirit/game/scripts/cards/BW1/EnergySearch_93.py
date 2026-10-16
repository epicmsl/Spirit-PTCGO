from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card
card = ItemCardDef(guid='b81ce9a4-bd24-5e56-9918-c6323995d488', key='BW1', name='com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name', display_name='Energy Search', searchable_by=['Energy Search', 'Item'], subtypes=['Item'], collector_number=93, set_code='BW1', rarity=Rarities.Common, effect=search_to_hand(is_basic_energy_card, count=1, minimum=0, reveal=True, prompt='Choose a basic Energy card to put into your hand.'))
