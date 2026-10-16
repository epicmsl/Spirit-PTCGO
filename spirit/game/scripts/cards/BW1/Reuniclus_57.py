from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.session.passives import effective_max_hp

def damage_swap_condition(board, player_id, pokemon):
    mine = board.pokemon_in_play(player_id)
    if len(mine) < 2:
        return False
    return any((p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p) for p in mine))

async def damage_swap(ctx):
    """As often as you like: move 1 damage counter from 1 Pokemon to another."""
    mine = ctx.my_pokemon_in_play()
    damaged = [p for p in mine if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged:
        return
    source = await ctx.choose_pokemon(damaged, 'Choose 1 of your Pokemon to move a damage counter from')
    if source is None:
        return
    targets = [p for p in mine if p is not source]
    if not targets:
        return
    dest = await ctx.choose_pokemon(targets, 'Choose 1 of your Pokemon to move the damage counter to')
    if dest is None:
        return
    await ctx.move_damage_counters(source, dest, max_count=1)
card = PokemonCardDef(guid='8f8f9e1c-abcf-5f21-b840-e528dadb862f', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Reuniclus.Name', display_name='Reuniclus', searchable_by=['Reuniclus', 'Stage 2', 'Reuniclus'], subtypes=['Stage 2'], collector_number=57, set_code='BW1', rarity=Rarities.RareHolo, foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.TINSEL]), hp=90, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE2, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name', family_id=577, abilities=[Ability(title='Damage Swap', game_text='As often as you like during your turn you may move 1 damage counter from 1 of your Pokémon to another of your Pokémon.', effect=damage_swap, activation=Activations.UNLIMITED, condition=damage_swap_condition), Attack(title='Psywave', game_text='Does 10 more damage for each Energy attached to the Defending Pokémon.', cost={PokemonTypes.PSYCHIC: 3}, damage=30, damage_operator='+', effect=damage_per(count_energy('defender'), 10, base=30))])
