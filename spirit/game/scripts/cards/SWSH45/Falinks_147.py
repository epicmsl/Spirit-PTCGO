from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import count_bench, damage_per
from spirit.game.card_effects.support_common import is_basic, search_to_bench

def _falinks_named(p):
    d = def_for(p.archetype_id)
    return bool(d and d.display_name and ('Falinks' in d.display_name))
card = PokemonCardDef(guid='34d7b925-8a8a-5aa5-9f18-30469b2e6433', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name', display_name='Falinks', searchable_by=['Falinks', 'Basic', 'Falinks'], subtypes=['Basic'], collector_number=147, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=90, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, family_id=870, abilities=[Attack(title='Call for Family', game_text='Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.', cost={PokemonTypes.COLORLESS: 1}, effect=search_to_bench(is_basic, count=2)), Attack(title='Team Attack', game_text='This attack does 30 damage for each of your Benched Pokémon that has "Falinks" in its name.', cost={PokemonTypes.COLORLESS: 2}, damage=30, effect=damage_per(count_bench('mine', pred=_falinks_named), 30), damage_operator='x')])
