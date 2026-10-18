from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.pokemon import energy_provides_type

def _is_fire_energy_card(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)

def inferno_fandango_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, 'hand')
    return bool(hand) and any((_is_fire_energy_card(c) for c in hand.children))

async def inferno_fandango(ctx):
    """As often as you like: attach a Fire Energy card from hand to 1 of your Pokemon."""
    energies = [c for c in ctx.hand() if _is_fire_energy_card(c)]
    if not energies:
        return
    picked = await ctx.choose_cards(energies, 1, minimum=1, prompt='Choose a Fire Energy card to attach')
    if not picked:
        return
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), 'Choose the Pokemon to attach it to')
    if target is not None:
        await ctx.attach_energy(picked[0], target)
card = PokemonCardDef(guid='ce517c8c-90c0-5c5a-8b2c-da59bfe9b3f3', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Emboar.Name', display_name='Emboar', searchable_by=['Emboar', 'Stage 2', 'Emboar'], subtypes=['Stage 2'], collector_number=20, set_code='BW1', rarity=Rarities.RareHolo, foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.TINSEL]), hp=150, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE2, retreat_cost=4, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name', family_id=498, abilities=[Ability(title='Inferno Fandango', game_text='As often as you like during your turn you may attach a Fire Energy card from your hand to 1 of your Pokémon.', effect=inferno_fandango, activation=Activations.UNLIMITED, condition=inferno_fandango_condition), Attack(title='Heat Crash', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2}, damage=80)])
