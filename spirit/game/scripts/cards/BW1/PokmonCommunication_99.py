from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card

async def pokemon_communication(ctx):
    """Reveal a Pokemon in your hand, shuffle it into your deck, then search
    your deck for a Pokemon and put it into your hand."""
    pokemon = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not pokemon:
        return
    picks = await ctx.choose_cards(pokemon, 1, minimum=1, prompt='Reveal a Pokemon to shuffle into your deck')
    if not picks:
        return
    await ctx.reveal_hand(picks)
    await ctx.shuffle_into_deck(picks)
    found = await ctx.search_deck(is_pokemon_card, count=1, minimum=0, prompt='Choose a Pokemon to put into your hand')
    await ctx.put_in_hand(found, reveal=False)
    await ctx.shuffle_deck()
card = ItemCardDef(guid='a94c0fa8-bfd0-50f6-9ee3-57cf66b10bd9', key='BW1', name='com.direwolfdigital.cake.data.archetypes.trainer.PokmonCommunication.Name', display_name='Pokémon Communication', searchable_by=['Pokémon Communication', 'Item'], subtypes=['Item'], collector_number=99, set_code='BW1', rarity=Rarities.Uncommon, effect=pokemon_communication)
