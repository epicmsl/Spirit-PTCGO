from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import energy_provides_type

def _is_metal_energy_card(card):
    return energy_provides_type(card, PokemonTypes.METAL.value)

def shift_gear_condition(board, player_id, pokemon):
    pkmn = board.pokemon_in_play(player_id)
    if len(pkmn) < 2:
        return False
    return any((_is_metal_energy_card(e) for p in pkmn for e in board.attached_energies(p)))

async def shift_gear(ctx):
    """As often as you like: move a Metal Energy from 1 Pokemon to another."""
    pool = [(e, p) for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p) if _is_metal_energy_card(e)]
    if not pool:
        return
    picked = await ctx.choose_cards([e for e, _ in pool], 1, prompt='Choose a Metal Energy to move')
    if not picked:
        return
    energy = picked[0]
    holder = next((p for e, p in pool if e is energy))
    targets = [p for p in ctx.my_pokemon_in_play() if p is not holder]
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, 'Choose a Pokemon to move the Energy to')
    if target is not None:
        await ctx.move_energy(energy, target)
card = PokemonCardDef(guid='a85e9c89-d12e-589d-adc9-4506c318e0e0', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name', display_name='Klinklang', searchable_by=['Klinklang', 'Stage 2', 'Klinklang'], subtypes=['Stage 2'], collector_number=76, set_code='BW1', rarity=Rarities.RareHolo, foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.TINSEL]), hp=140, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name', family_id=599, abilities=[Ability(title='Shift Gear', game_text='As often as you like during your turn you may move a Metal Energy attached to 1 of your Pokémon to another of your Pokémon.', effect=shift_gear, activation=Activations.UNLIMITED, condition=shift_gear_condition), Attack(title='Gear Grind', game_text='Flip 2 coins. This attack does 80 damage times the number of heads.', cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2}, damage=80, damage_operator='x', effect=flip_damage(coins=2, per_heads=80))])
