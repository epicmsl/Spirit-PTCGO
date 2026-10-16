from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

async def torment(ctx):
    """Damage then choose 1 of the Defending Pokemon's attacks; it can't be
    used during your opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    entries = [e for e in defender.get_attribute(AttrID.PIE_ABILITIES) or [] if isinstance(e, dict) and e.get('abilityType') == 'Attack' and e.get('abilityID')]
    if not entries:
        return
    titles = [e.get('title', {}).get('id', 'Attack') for e in entries]
    idx = await ctx.choose('Choose an attack to lock', titles)
    entry = entries[idx]
    ctx.session.turn_state.attack_locks[defender.entity_id, entry['abilityID']] = ctx.session.turn_state.turn_number + 1
card = PokemonCardDef(guid='687db912-1858-5a62-8024-c1225ad96e11', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name', display_name='Krokorok', searchable_by=['Krokorok', 'Stage 1', 'Krokorok'], subtypes=['Stage 1'], collector_number=64, set_code='BW1', rarity=Rarities.Uncommon, hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name', family_id=551, abilities=[Attack(title='Torment', game_text="Choose 1 of the Defending Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 1}, damage=10, effect=torment), Attack(title='Bite', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=50)])
