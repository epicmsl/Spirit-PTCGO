from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_energy_card


async def professor_burnet(ctx):
    """Discard the top 3 cards of your deck, and attach all Energy cards you
    discarded in this way to 1 of your Pokemon."""
    top = list(ctx.deck_top(3))
    if not top:
        return
    await ctx.discard_cards(top)
    energies = [c for c in top if is_energy_card(c)]
    if not energies:
        return
    targets = ctx.my_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your Pokémon to attach the discarded Energy to")
    if target is None:
        return
    for card in energies:
        await ctx.attach_energy(card, target)


card = SupporterCardDef(
    guid="c96b7ffa-5156-5a62-a1f4-d554eabb27aa",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBurnet.Name",
    display_name="Professor Burnet",
    searchable_by=["Professor Burnet", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    effect=professor_burnet,
)
