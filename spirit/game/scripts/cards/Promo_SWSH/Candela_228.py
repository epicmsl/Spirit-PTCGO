from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects, PokemonTypes, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card


async def candela(ctx):
    """Draw 2. If you drew any cards, flip a coin; heads attaches a Fire
    Energy card from your discard pile to 1 of your Benched Pokemon."""
    drawn = await ctx.draw_cards(2)
    if drawn <= 0:
        return
    heads = (await ctx.flip_coins(1, "Candela"))[0]
    if not heads:
        return
    bench = ctx.my_bench()
    energies = [
        c for c in ctx.discard_pile()
        if is_basic_energy_card(c)
        and PokemonTypes.FIRE.value in (c.get_attribute(AttrID.POKEMON_TYPES) or [])
    ]
    if not bench or not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose a Fire Energy card from your discard pile.",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to attach Fire Energy to"
    )
    if target is not None:
        await ctx.attach_energy(picks[0], target)


card = SupporterCardDef(
    guid="2bcd0d99-0876-5a7d-94ef-e284ed44e307",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Candela.Name",
    display_name="Candela",
    searchable_by=["Candela", "Supporter"],
    subtypes=["Supporter"],
    collector_number=228,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    effect=candela,
)
