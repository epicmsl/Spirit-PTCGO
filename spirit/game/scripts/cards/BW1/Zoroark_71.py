from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID
from spirit.game.card_effects.support_common import search_to_hand

async def foul_play(ctx):
    """Use 1 of the Defending Pokemon's attacks as this attack (damage copy)."""
    defender = ctx.defender
    if defender is None:
        return
    entries = [e for e in defender.get_attribute(AttrID.PIE_ABILITIES) or [] if isinstance(e, dict) and e.get('abilityType') == 'Attack' and e.get('abilityID')]
    if not entries:
        return
    titles = [e.get('title', {}).get('id', 'Attack') for e in entries]
    idx = await ctx.choose('Choose an attack to copy', titles)
    entry = entries[idx]
    dmg = entry.get('damage') or 0
    try:
        dmg = int(dmg)
    except (TypeError, ValueError):
        dmg = 0
    if dmg > 0:
        await ctx.deal_damage(dmg)
card = PokemonCardDef(guid='45e81b50-12a2-5c41-b6ee-f14d3807918c', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name', display_name='Zoroark', searchable_by=['Zoroark', 'Stage 1', 'Zoroark'], subtypes=['Stage 1'], collector_number=71, set_code='BW1', rarity=Rarities.RareHolo, foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.TINSEL]), hp=100, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, resistance_type=PokemonTypes.PSYCHIC, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name', family_id=570, abilities=[Attack(title='Nasty Plot', game_text='Search your deck for a card and put it into your hand. Shuffle your deck afterward.', cost={PokemonTypes.DARKNESS: 1}, effect=search_to_hand(count=1, minimum=1, reveal=False, prompt='Search your deck for a card.')), Attack(title='Foul Play', game_text="Choose 1 of the Defending Pokémon's attacks and use it as this attack.", cost={PokemonTypes.COLORLESS: 2}, effect=foul_play)])
