from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if

async def blindside(ctx):
    """50 damage to 1 of the opponent's Pokemon that has damage counters."""

    def counters(p):
        return max(0, (ctx.max_hp(p) - (p.get_attribute(AttrID.HP) or 0)) // 10)
    pool = [p for p in [ctx.opponent_active()] + ctx.opponent_bench() if p is not None and counters(p) > 0]
    if not pool:
        return
    pick = await ctx.choose_cards(pool, 1, minimum=1, prompt='Choose a Pokemon with damage counters to take 50 damage')
    if pick:
        await ctx.deal_damage(50, target=pick[0], apply_modifiers=None)

def _defender_is_stage2(ctx):
    defender = ctx.defender
    if defender is None:
        return False
    return defender.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value
card = PokemonCardDef(guid='dd9d904d-efc8-55ac-a426-1c6036e26646', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name', display_name='Mandibuzz', searchable_by=['Mandibuzz', 'Stage 1', 'Mandibuzz'], subtypes=['Stage 1'], collector_number=73, set_code='BW1', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name', family_id=629, abilities=[Attack(title='Blindside', game_text="Does 50 damage to 1 of your opponent's Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.DARKNESS: 1}, effect=blindside), Attack(title='Punishment', game_text='If the Defending Pokémon is a Stage 2 Pokémon, this attack does 60 more damage.', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=40, damage_operator='+', effect=bonus_if(_defender_is_stage2, 60))])
