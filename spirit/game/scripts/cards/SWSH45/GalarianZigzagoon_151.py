from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import flip_or_nothing

async def headbutt_tantrum(ctx):
    """On play from hand to Bench: you may put 1 damage counter on 1 of
    your opponent's Pokémon."""
    if not await ctx.ask_yes_no("Put 1 damage counter on 1 of your opponent's Pokémon?"):
        return
    await ctx.place_damage_counters(1)
card = PokemonCardDef(guid='48ace423-43b4-58b1-81e1-f046b238ef07', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name', display_name='Galarian Zigzagoon', searchable_by=['Galarian Zigzagoon', 'Basic', 'GalarianZigzagoon'], subtypes=['Basic'], collector_number=151, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=70, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.GRASS, family_id=263, abilities=[Ability(title='Headbutt Tantrum', game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may put 1 damage counter on 1 of your opponent's Pokémon.", effect=headbutt_tantrum, trigger=Triggers.ON_PLAY), Attack(title='Surprise Attack', game_text='Flip a coin. If tails, this attack does nothing.', cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1}, damage=30, effect=flip_or_nothing())])
