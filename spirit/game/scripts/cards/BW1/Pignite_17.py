from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.pokemon import energy_provides_type

def _is_fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)
card = PokemonCardDef(guid='31700d93-8e88-5b47-94a3-0f4b0cf820eb', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name', display_name='Pignite', searchable_by=['Pignite', 'Stage 1', 'Pignite'], subtypes=['Stage 1'], collector_number=17, set_code='BW1', rarity=Rarities.Uncommon, hp=100, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name', family_id=498, abilities=[Attack(title='Flame Charge', game_text='Search your deck for a Fire Energy card and attach it to this Pokémon. Shuffle your deck afterward.', cost={PokemonTypes.COLORLESS: 1}, effect=search_attach_energy(predicate=_is_fire_energy, count=1, to_self=True)), Attack(title='Heat Crash', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=50)])
