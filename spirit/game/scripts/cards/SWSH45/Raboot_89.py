from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import search_attach_energy

def _is_fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)
card = PokemonCardDef(guid='9521ba6a-7a73-5569-9bff-a8b5565f6029', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name', display_name='Raboot', searchable_by=['Raboot', 'Stage 1', 'Raboot'], subtypes=['Stage 1'], collector_number=89, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=90, elements=[PokemonTypes.FIRE], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.WATER, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name', family_id=813, abilities=[Attack(title='Flame Charge', game_text='Search your deck for a Fire Energy card and attach it to this Pokémon. Then, shuffle your deck.', cost={PokemonTypes.FIRE: 1}, damage=20, effect=search_attach_energy(predicate=_is_fire_energy, count=1, to_self=True)), Attack(title='Magnum Kick', cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1}, damage=70)])
