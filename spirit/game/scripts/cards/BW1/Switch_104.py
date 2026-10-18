from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch, player_has_bench
card = ItemCardDef(guid='a98b9a16-dbe6-5f78-9bab-c28bb35e29df', key='BW1', name='com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name', display_name='Switch', searchable_by=['Switch', 'Item'], subtypes=['Item'], collector_number=104, set_code='BW1', rarity=Rarities.Common, effect=switch, condition=player_has_bench)
