from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.session.passives import Passive
from spirit.game.card_effects.passives_common import is_in_active_spot

class PrimalLawPassive(Passive):

    def blocks_evolution(self, player_id, target, carrier):
        return player_id != carrier.owning_player_id and is_in_active_spot(carrier)
card = PokemonCardDef(guid='ad551d5f-cf2c-5b31-8fb8-479fe9db8975', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Dracovish.Name', display_name='Dracovish', searchable_by=['Dracovish', 'Stage 1', 'Dracovish'], subtypes=['Stage 1'], collector_number=109, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=150, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=3, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.RareFossil.Name', family_id=883, abilities=[Ability(title='Primal Law', game_text="As long as this Pokémon is in the Active Spot, your opponent can't play any Pokémon from their hand to evolve their Pokémon.", passive=PrimalLawPassive()), Attack(title='Hammer In', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2}, damage=120)])
