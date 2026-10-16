from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects, AttrID

async def ascension(ctx):
    """Search the deck for a card that evolves from this Pokémon and put it
    onto this Pokémon to evolve it. Then, shuffle the deck."""
    my_logic_name = ctx.source.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

    def matches(c):
        return c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == my_logic_name
    picks = await ctx.search_deck(matches, count=1, minimum=0, prompt='Choose a card that evolves from this Pokémon.')
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()
card = PokemonCardDef(guid='1be2bd3a-a0cd-5bf3-9d41-e13f5672eb4f', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name', display_name='Koffing', searchable_by=['Koffing', 'Basic', 'Koffing'], subtypes=['Basic'], collector_number=149, set_code='SWSH45', rarity=Rarities.Shining, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]), hp=60, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.FIGHTING, family_id=109, abilities=[Attack(title='Ascension', game_text='Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.', cost={PokemonTypes.DARKNESS: 1}, effect=ascension)])
