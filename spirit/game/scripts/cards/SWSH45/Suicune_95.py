from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.pokemon import energy_provides_type

async def _aurora_loop(ctx):
    await ctx.deal_damage()
    water_energies = [e for e in ctx.attached_energies(ctx.attacker) if energy_provides_type(e, PokemonTypes.WATER.value)]
    picks = await ctx.choose_cards(water_energies, 2, prompt='Choose 2 Water Energy to put into your hand')
    await ctx.put_in_hand(picks, reveal=False)
card = PokemonCardDef(guid='ff92c4cb-4208-5886-b98b-5df0fc30ece3', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name', display_name='Suicune', searchable_by=['Suicune', 'Basic', 'Suicune'], subtypes=['Basic'], collector_number=95, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=120, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, family_id=245, abilities=[Attack(title='Wave Splash', cost={PokemonTypes.WATER: 1}, damage=20), Attack(title='Aurora Loop', game_text='Put 2 Water Energy attached to this Pokémon into your hand.', cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=130, effect=_aurora_loop)])
