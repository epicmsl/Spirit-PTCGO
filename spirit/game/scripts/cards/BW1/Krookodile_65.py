from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID
from spirit.game.card_effects.attacks_common import bonus_if, has_damage

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
card = PokemonCardDef(guid='006c8674-631c-5e05-948e-156db19389d6', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name', display_name='Krookodile', searchable_by=['Krookodile', 'Stage 2', 'Krookodile'], subtypes=['Stage 2'], collector_number=65, set_code='BW1', rarity=Rarities.RareHolo, foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.TINSEL]), hp=140, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name', family_id=551, abilities=[Attack(title='Torment', game_text="Choose 1 of the Defending Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.", cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=torment), Attack(title='Krookoroll', game_text='If the Defending Pokémon already has any damage counters on it, this attack does 40 more damage.', cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2}, damage=60, damage_operator='+', effect=bonus_if(has_damage('defender'), 40))])
