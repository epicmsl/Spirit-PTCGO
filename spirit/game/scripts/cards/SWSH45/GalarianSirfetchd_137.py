from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.session.legal_actions import LOCK_UNTIL_LEAVES_ACTIVE

async def meteor_assault(ctx):
    """180. Can't use Meteor Assault again until this Pokemon leaves Active."""
    await ctx.deal_damage()
    ctx.session.turn_state.attack_locks[ctx.attacker.entity_id, ctx.ability.ability_id] = LOCK_UNTIL_LEAVES_ACTIVE
card = PokemonCardDef(guid='67d3f621-dcc3-54b5-b559-08d5f36dde32', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSirfetchd.Name', display_name="Galarian Sirfetch'd", searchable_by=["Galarian Sirfetch'd", 'Stage 1', 'GalarianSirfetchd'], subtypes=['Stage 1'], collector_number=137, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=130, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GalarianFarfetchd.Name', family_id=83, abilities=[Attack(title='Pierce', cost={PokemonTypes.FIGHTING: 1}, damage=40), Attack(title='Meteor Assault', game_text="This Pokémon can't use Meteor Assault again until it leaves the Active Spot.", cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2}, damage=180, effect=meteor_assault)])
