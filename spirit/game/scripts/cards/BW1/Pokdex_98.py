from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
card = ItemCardDef(guid='cb16cda2-d353-5dfd-9f96-8574c3dff955', key='BW1', name='com.direwolfdigital.cake.data.archetypes.trainer.Pokdex.Name', display_name='Pokédex', searchable_by=['Pokédex', 'Item'], subtypes=['Item'], collector_number=98, set_code='BW1', rarity=Rarities.Uncommon, effect=look_at_top(5, take=1, rest='shuffle', prompt='Choose a card to put into your hand.'))
