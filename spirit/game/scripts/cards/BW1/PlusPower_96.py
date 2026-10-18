from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import TurnDamageModifier

async def plus_power(ctx):
    """This turn, your Pokemon's attacks do 10 more damage to the opponent's Active."""
    ctx.add_turn_damage_modifier(TurnDamageModifier(10, ctx.player_id))
card = ItemCardDef(guid='269e1959-78f0-5afe-922a-e7a0134af585', key='BW1', name='com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name', display_name='PlusPower', searchable_by=['PlusPower', 'Item'], subtypes=['Item'], collector_number=96, set_code='BW1', rarity=Rarities.Uncommon, effect=plus_power)
