from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches

async def circle_throw(ctx):
    """Your opponent switches the Defending Pokemon with 1 of their Benched Pokemon."""
    await ctx.deal_damage()
    await opponent_switches(ctx)

async def storm_throw(ctx):
    """Damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)
card = PokemonCardDef(guid='7ee0141c-dbe2-52fe-8cf5-835e1da50a0d', key='BW1', name='com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name', display_name='Throh', searchable_by=['Throh', 'Basic', 'Throh'], subtypes=['Basic'], collector_number=61, set_code='BW1', rarity=Rarities.Rare, hp=100, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.BASIC, retreat_cost=3, weakness_type=PokemonTypes.PSYCHIC, family_id=538, abilities=[Attack(title='Circle Throw', game_text='Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.', cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=circle_throw), Attack(title='Storm Throw', game_text="This attack's damage isn't affected by Resistance.", cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=80, effect=storm_throw)])
