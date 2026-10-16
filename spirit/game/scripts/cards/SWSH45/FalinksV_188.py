from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.passives_common import takes_less_passive

def _protects_falinks(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    definition = def_for(target.archetype_id)
    return bool(definition and 'falinks' in (definition.display_name or '').lower())
card = PokemonCardDef(guid='9ca4e684-0848-5adf-95f0-ce618a010cbf', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.FalinksV.Name', display_name='Falinks V', searchable_by=['Falinks V', 'Basic', 'V', 'FalinksV'], subtypes=['Basic', 'V'], collector_number=188, set_code='SWSH45', rarity=Rarities.RareHoloV, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=160, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, family_id=870, abilities=[Ability(title='Iron Defense Formation', game_text='All of your Pokémon that have "Falinks" in their name take 20 less damage from your opponent\'s attacks (after applying Weakness and Resistance).', passive=takes_less_passive(20, protects=_protects_falinks)), Attack(title='Giga Impact', game_text="During your next turn, this Pokémon can't attack.", cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=210, locks_next_turn=True)])
