from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import bonus_if, count_energy

def _has_extra_energy(ctx) -> bool:
    total_cost = sum(ctx.ability.cost.values())
    return _ENERGY_ON_SELF(ctx) > total_cost
_ENERGY_ON_SELF = count_energy('self')
card = PokemonCardDef(guid='5b0a4291-a9f3-5751-a160-7ffa996468e1', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Stonjourner.Name', display_name='Stonjourner', searchable_by=['Stonjourner', 'Basic', 'Stonjourner'], subtypes=['Basic'], collector_number=148, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=140, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=4, weakness_type=PokemonTypes.GRASS, family_id=874, abilities=[Attack(title='Mega Kick', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=80), Attack(title='Power Press', game_text="If this Pokémon has at least 1 extra Energy attached (in addition to this attack's cost), this attack does 60 more damage.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3}, damage=120, effect=bonus_if(_has_extra_energy, 60), damage_operator='+')])
