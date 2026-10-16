from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

async def biting_whirlpool(ctx):
    """Whenever your opponent attaches an Energy card from their hand to 1 of
    their Pokémon, put 2 damage counters on that Pokémon."""
    if ctx.attaching_player_id == ctx.player_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None:
        return
    await ctx.deal_damage(20, target=receiver, apply_modifiers=False, as_counters=True)
card = PokemonCardDef(guid='bafa3e1b-bd1d-5ca5-8a3a-f34a878f10d9', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Arctozolt.Name', display_name='Arctozolt', searchable_by=['Arctozolt', 'Stage 1', 'Arctozolt'], subtypes=['Stage 1'], collector_number=119, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=130, elements=[PokemonTypes.LIGHTNING], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.RareFossil.Name', family_id=881, abilities=[Ability(title='Biting Whirlpool', game_text='Whenever your opponent attaches an Energy card from their hand to 1 of their Pokémon, put 2 damage counters on that Pokémon.', effect=biting_whirlpool, trigger=Triggers.ON_ENERGY_ATTACHED), Attack(title='Electro Ball', cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=70)])
