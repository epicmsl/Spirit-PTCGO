from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.card_effects.attacks_common import bonus_if

def _bench_damaged(ctx) -> bool:
    return any((p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p) for p in ctx.my_bench()))
card = PokemonCardDef(guid='b62d6b51-0a8d-5972-92e1-59008dd3bbb9', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Copperajah.Name', display_name='Copperajah', searchable_by=['Copperajah', 'Stage 1', 'Copperajah'], subtypes=['Stage 1'], collector_number=164, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=190, elements=[PokemonTypes.METAL], stage=PokemonStage.STAGE1, retreat_cost=4, weakness_type=PokemonTypes.FIRE, resistance_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name', family_id=878, abilities=[Ability(title='Antibacterial Skin', game_text="This Pokémon can't be affected by any Special Conditions.", passive=condition_immunity_passive()), Attack(title='Vengeful Stomp', game_text='If your Benched Pokémon have any damage counters on them, this attack does 120 more damage.', cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2}, damage=120, effect=bonus_if(_bench_damaged, 120), damage_operator='+')])
