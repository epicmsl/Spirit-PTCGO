from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID
from spirit.game.card_effects.attacks_common import condition_attack, damage_per

def _defender_retreat_cost(ctx):
    defender = ctx.defender
    return defender.get_attribute(AttrID.RETREAT_COST, 0) if defender else 0
card = PokemonCardDef(guid='e58c753e-a31b-52a1-87aa-718ef0112a28', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Drednaw.Name', display_name='Drednaw', searchable_by=['Drednaw', 'Stage 1', 'Drednaw'], subtypes=['Stage 1'], collector_number=102, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=130, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name', family_id=833, abilities=[Attack(title='Vise Bite', game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=damage_per(_defender_retreat_cost, 30, base=60), damage_operator='+'), Attack(title='Jaw Lock', game_text="During your opponent's next turn, the Defending Pokémon can't retreat.", cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3}, damage=130, effect=condition_attack(no_retreat=True))])
