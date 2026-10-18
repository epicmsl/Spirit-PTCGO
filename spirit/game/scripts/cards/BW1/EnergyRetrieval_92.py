from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
card = ItemCardDef(guid='f4481ef7-97b4-5fda-aa1b-fadd2e09957e', key='BW1', name='com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name', display_name='Energy Retrieval', searchable_by=['Energy Retrieval', 'Item'], subtypes=['Item'], collector_number=92, set_code='BW1', rarity=Rarities.Uncommon, effect=recover_from_discard(is_basic_energy_card, count=2, minimum=1, to='hand'), condition=requires_discard(is_basic_energy_card))
