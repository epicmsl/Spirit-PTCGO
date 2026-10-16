from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import cure_conditions_effect
card = ItemCardDef(guid='b5f3111b-9afa-5a86-9058-097b4b298f4a', key='BW1', name='com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name', display_name='Full Heal', searchable_by=['Full Heal', 'Item'], subtypes=['Item'], collector_number=95, set_code='BW1', rarity=Rarities.Uncommon, effect=cure_conditions_effect('active'))
