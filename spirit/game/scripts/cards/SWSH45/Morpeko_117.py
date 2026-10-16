from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID
from spirit.game.card_effects.attacks_common import snipe_attack

async def torment(ctx):
    """20. Choose 1 of your opponent's Active Pokemon's attacks. During your
    opponent's next turn, that Pokemon can't use that attack."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    entries = _attack_entries(defender)
    if not entries:
        return
    index = 0
    if len(entries) > 1:
        index = await ctx.choose("Choose an attack that can't be used during your opponent's next turn", [e['title']['id'] for e in entries])
    entry = entries[index]
    state = ctx.session.turn_state
    state.attack_locks[defender.entity_id, entry['abilityID']] = state.turn_number + 1

def _attack_entries(pokemon):
    return [e for e in pokemon.get_attribute(AttrID.PIE_ABILITIES) or [] if isinstance(e, dict) and e.get('abilityType') == 'Attack' and e.get('abilityID')]
card = PokemonCardDef(guid='70d5c4f5-750b-5229-a93f-0d6ad21a82a8', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name', display_name='Morpeko', searchable_by=['Morpeko', 'Basic', 'Morpeko'], subtypes=['Basic'], collector_number=117, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=80, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=877, abilities=[Attack(title='Torment', game_text="Choose 1 of your opponent's Active Pokémon's attacks. During your opponent's next turn, that Pokémon can't use that attack.", cost={PokemonTypes.COLORLESS: 1}, damage=20, effect=torment), Attack(title='Spark', game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=50, effect=snipe_attack(20, also_base=True))])
