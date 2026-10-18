from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.session.passives import Passive

class _SkyCircusPassive(Passive):

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        state = getattr(board, 'turn_state', None)
        if state and any((name == 'Bird Keeper' for _, name, _ in state.trainers_played)):
            return {}
        return cost

async def _feather_slice(ctx):
    bonus = False
    if ctx.hand_size() > 0 and await ctx.ask_yes_no('You may discard a card from your hand. If you do, this attack does 70 more damage.'):
        picks = await ctx.discard_from_hand(1, prompt='Discard a card for Feather Slice')
        bonus = bool(picks)
    await ctx.deal_damage(70 + (70 if bonus else 0))
card = PokemonCardDef(guid='0da1de43-7e64-51af-a98d-039f670ef6dc', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Swanna.Name', display_name='Swanna', searchable_by=['Swanna', 'Stage 1', 'Swanna'], subtypes=['Stage 1'], collector_number=169, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=110, elements=[PokemonTypes.COLORLESS], stage=PokemonStage.STAGE1, retreat_cost=0, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name', family_id=580, abilities=[Ability(title='Sky Circus', game_text="If you played Bird Keeper from your hand during this turn, ignore all Energy in this Pokémon's attack costs.", passive=_SkyCircusPassive()), Attack(title='Feather Slice', game_text='You may discard a card from your hand. If you do, this attack does 70 more damage.', cost={PokemonTypes.COLORLESS: 3}, damage=70, effect=_feather_slice, damage_operator='+')])
