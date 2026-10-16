from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.pokemon import energy_provides_type, is_energy_card

async def spiral_jet(ctx):
    """Discard 2 Water Energy cards from hand. If you don't, this attack does nothing."""
    discarded = await ctx.discard_from_hand(2, minimum=0, predicate=_is_water_energy_card, prompt='Discard 2 Water Energy cards from your hand for Spiral Jet')
    if len(discarded) < 2:
        return
    await ctx.deal_damage()

def _is_water_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER)
card = PokemonCardDef(guid='41389f0d-d19a-54d5-a29f-f8b4fde24d69', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Barraskewda.Name', display_name='Barraskewda', searchable_by=['Barraskewda', 'Stage 1', 'Barraskewda'], subtypes=['Stage 1'], collector_number=105, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=120, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name', family_id=846, abilities=[Attack(title='Peck', cost={PokemonTypes.COLORLESS: 1}, damage=30), Attack(title='Spiral Jet', game_text="Discard 2 Water Energy cards from your hand. If you don't, this attack does nothing.", cost={PokemonTypes.WATER: 1}, damage=130, effect=spiral_jet)])
