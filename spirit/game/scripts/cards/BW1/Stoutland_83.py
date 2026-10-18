from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks

async def odor_sleuth(ctx):
    """Flip 3 coins. For each heads, put a card from your discard pile into your hand."""
    results = await ctx.flip_coins(3, 'Odor Sleuth')
    heads = sum((1 for r in results if r))
    for _ in range(heads):
        pile = ctx.discard_pile()
        if not pile:
            return
        pick = await ctx.choose_cards(pile, 1, minimum=1, prompt='Choose a card to put into your hand')
        if not pick:
            return
        await ctx.put_in_hand(pick, reveal=False)

async def giga_impact(ctx):
    """Damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)
card = PokemonCardDef(guid='caf3fd8c-a125-537f-a0b0-ad1cf9e60255', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name', display_name='Stoutland', searchable_by=['Stoutland', 'Stage 2', 'Stoutland'], subtypes=['Stage 2'], collector_number=83, set_code='BW1', rarity=Rarities.Rare, hp=140, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name', family_id=506, abilities=[Attack(title='Odor Sleuth', game_text='Flip 3 coins. For each heads, put a card from your discard pile into your hand.', cost={PokemonTypes.COLORLESS: 2}, effect=odor_sleuth), Attack(title='Giga Impact', game_text="This Pokémon can't attack during your next turn.", cost={PokemonTypes.COLORLESS: 4}, damage=90, effect=giga_impact)])
