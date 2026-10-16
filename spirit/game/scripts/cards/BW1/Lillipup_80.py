from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

async def pickup(ctx):
    """Put an Item card from your discard pile into your hand."""
    items = [c for c in ctx.discard_pile() if _is_item_card(c)]
    if not items:
        return
    picks = await ctx.choose_cards(items, 1, minimum=1, prompt='Choose an Item card to put into your hand')
    if picks:
        await ctx.put_in_hand(picks, reveal=False)

def _is_item_card(card):
    from spirit.game.session.effects import is_trainer_card
    if not is_trainer_card(card):
        return False
    types = card.get_attribute(AttrID.TRAINER_TYPE) or None
    definition = def_for(getattr(card, 'archetype_id', None))
    if definition is not None and getattr(definition, 'subtypes', None):
        return 'Item' in definition.subtypes
    return types is None
card = PokemonCardDef(guid='3a4c953b-ac23-5398-a888-b9f3925998e3', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name', display_name='Lillipup', searchable_by=['Lillipup', 'Basic', 'Lillipup'], subtypes=['Basic'], collector_number=80, set_code='BW1', rarity=Rarities.Common, hp=50, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=506, abilities=[Attack(title='Pickup', game_text='Put an Item card from your discard pile into your hand.', cost={PokemonTypes.COLORLESS: 1}, effect=pickup), Attack(title='Bite', cost={PokemonTypes.COLORLESS: 1}, damage=10)])
