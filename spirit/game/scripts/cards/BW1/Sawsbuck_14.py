from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.attacks_common import damage_per, count_energy

def _grass_energy_everywhere(ctx):
    total = count_energy('mine', energy_type=PokemonTypes.GRASS)(ctx)
    total += count_energy('opponent', energy_type=PokemonTypes.GRASS)(ctx)
    return total
card = PokemonCardDef(guid='37dd7df0-cded-5c65-9282-b9ed84d778cf', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Sawsbuck.Name', display_name='Sawsbuck', searchable_by=['Sawsbuck', 'Stage 1', 'Sawsbuck'], subtypes=['Stage 1'], collector_number=14, set_code='BW1', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.GRASS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.WATER, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name', family_id=585, abilities=[Attack(title='Nature Power', game_text="Does 10 more damage for each Grass Energy attached to both your and your opponent's Pokémon.", cost={PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='+', effect=damage_per(_grass_energy_everywhere, 10, base=20)), Attack(title='Horn Leech', game_text='Heal 20 damage from this Pokémon.', cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=heal_attack(20))])
