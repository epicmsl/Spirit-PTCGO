from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.support_common import heal_attack, distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card

async def decorate(ctx):
    """Attach any number of basic Energy cards from your hand to your Pokemon in any way you like."""
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(energies, len(energies), minimum=0, prompt='Choose basic Energy cards to attach.')
    candidates = ctx.my_pokemon_in_play()
    if picks and candidates:
        await distribute_energy(ctx, picks, candidates)
card = PokemonCardDef(guid='7f78378c-db3f-5443-a83f-63b51ccc0da4', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Alcremie.Name', display_name='Alcremie', searchable_by=['Alcremie', 'Stage 1', 'Alcremie'], subtypes=['Stage 1'], collector_number=131, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=110, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name', family_id=868, abilities=[Attack(title='Decorate', game_text='Attach any number of basic Energy cards from your hand to your Pokémon in any way you like.', cost={PokemonTypes.COLORLESS: 1}, effect=decorate), Attack(title='Draining Kiss', game_text='Heal 30 damage from this Pokémon.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1}, damage=50, effect=heal_attack(30))])
