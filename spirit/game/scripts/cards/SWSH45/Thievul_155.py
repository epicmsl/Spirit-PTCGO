from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

async def thief(ctx):
    """20 damage. Reveal the opponent's hand and put a card found there on
    the bottom of their deck."""
    await ctx.deal_damage()
    opponent_hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    if not opponent_hand:
        return
    picks = await ctx.choose_cards(opponent_hand, 1, minimum=1, prompt="Choose a card to put on the bottom of your opponent's deck")
    for card_entity in picks:
        await ctx.put_on_bottom_of_deck(card_entity)
card = PokemonCardDef(guid='74b760fe-c0c9-5c80-856a-54116aceca18', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Thievul.Name', display_name='Thievul', searchable_by=['Thievul', 'Stage 1', 'Thievul'], subtypes=['Stage 1'], collector_number=155, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=100, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name', family_id=827, abilities=[Attack(title='Thief', game_text='Your opponent reveals their hand. Choose a card you find there and put it on the bottom of their deck.', cost={PokemonTypes.DARKNESS: 1}, damage=20, effect=thief), Attack(title='Darkness Fang', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=90)])
