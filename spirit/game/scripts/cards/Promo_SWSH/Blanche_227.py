from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects, AttrID, PokemonTypes
from spirit.game.card_effects.trainers import is_energy_card


def _is_water_energy_card(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.WATER.value in types


async def blanche(ctx):
    """Draw 2. If you drew any, flip a coin; heads attaches a Water Energy from your discard to a Benched Pokemon."""
    drawn = await ctx.draw_cards(2)
    if not drawn:
        return
    flips = await ctx.flip_coins(1, "Blanche")
    if not flips[0]:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    energies = [c for c in ctx.discard_pile() if _is_water_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose a Water Energy card to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon") or bench[0]
    await ctx.attach_energy(picks[0], target)


card = SupporterCardDef(
    guid="6f1ca137-0ca6-5a90-8fa6-cecb3e9108f7",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blanche.Name",
    display_name="Blanche",
    searchable_by=["Blanche", "Supporter"],
    subtypes=["Supporter"],
    collector_number=227,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    effect=blanche,
)
