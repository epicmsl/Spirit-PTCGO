from spirit.game.data_utils import ItemCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.support_common import search_to_bench


async def poke_ball(ctx):
    """Flip a coin. If heads, search your deck for a Basic Pokemon onto your Bench."""
    results = await ctx.flip_coins(1, "Poké Ball")
    if not results or not results[0]:
        return
    await search_to_bench(predicate=is_basic_pokemon, count=1)(ctx)


card = ItemCardDef(
    guid="efdcdcf4-8b85-572b-8e5a-08b509da4022",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Poké Ball", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="Promo_SWSH",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWHOLO]),
    effect=poke_ball,
)
