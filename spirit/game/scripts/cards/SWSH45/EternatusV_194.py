from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID
from spirit.game.card_effects.attacks_common import bonus_if, defender_is_v, defender_is_vmax
from spirit.game.card_effects.trainers import is_energy_card

async def power_accelerator(ctx):
    """30 damage. You may attach a Darkness Energy from hand to 1 Benched Pokémon."""
    await ctx.deal_damage(30)
    energies = [c for c in ctx.hand() if _is_darkness_energy(c)]
    if not energies or not ctx.my_bench():
        return
    if not await ctx.ask_yes_no('Attach a Darkness Energy card from your hand to 1 of your Benched Pokémon?'):
        return
    picked = await ctx.choose_cards(energies, 1, minimum=1, prompt='Choose a Darkness Energy card to attach')
    if not picked:
        return
    target = await ctx.choose_pokemon(ctx.my_bench(), 'Choose the Benched Pokémon to attach it to')
    if target is not None:
        await ctx.attach_energy(picked[0], target)

def _is_darkness_energy(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.DARKNESS.value in types
card = PokemonCardDef(guid='98df5096-fcb5-5a37-be19-602f3dd7e008', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.EternatusV.Name', display_name='Eternatus V', searchable_by=['Eternatus V', 'Basic', 'V', 'EternatusV'], subtypes=['Basic', 'V'], collector_number=194, set_code='SWSH45', rarity=Rarities.RareSecret, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET]), hp=220, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=2, weakness_type=PokemonTypes.FIGHTING, family_id=890, abilities=[Attack(title='Power Accelerator', game_text='You may attach a Darkness Energy card from your hand to 1 of your Benched Pokémon.', cost={PokemonTypes.COLORLESS: 1}, damage=30, effect=power_accelerator), Attack(title='Dynamax Cannon', game_text="If your opponent's Active Pokémon is a Pokémon , this attack does 120 more damage.", cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3}, damage=120, damage_operator='+', effect=bonus_if(defender_is_v, 120))])
