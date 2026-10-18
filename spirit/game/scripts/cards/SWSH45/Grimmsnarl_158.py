from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.session.passives import Passive
from spirit.game.card_effects.passives_common import is_in_active_spot, opposing_active

class DarkOathPassive(Passive):

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if is_in_active_spot(carrier) and opposing_active(pokemon, carrier):
            cost['Colorless'] = cost.get('Colorless', 0) + 1
        return cost
card = PokemonCardDef(guid='0f07b300-9f13-5b27-b796-c7843bc8bdff', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Grimmsnarl.Name', display_name='Grimmsnarl', searchable_by=['Grimmsnarl', 'Stage 2', 'Grimmsnarl'], subtypes=['Stage 2'], collector_number=158, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=170, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE2, retreat_cost=3, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name', family_id=859, abilities=[Ability(title='Dark Oath', game_text="As long as this Pokémon is in the Active Spot, your opponent's Active Pokémon's attacks cost Colorless more.", passive=DarkOathPassive()), Attack(title='Energy Press', game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.", cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2}, damage=100, damage_operator='+')])
