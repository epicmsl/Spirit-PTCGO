from spirit.game.data_utils import Ability, Attack, Foil, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, FoilMasks, FoilEffects


async def max_shock(ctx):
    """Printed damage; if you have more Prizes remaining, paralyze the Active."""
    await ctx.deal_damage()
    if ctx.prizes_taken(ctx.player_id) < ctx.prizes_taken(ctx.opponent_id):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="a1fca07d-648c-588d-8ced-ad5b8527c5c6",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoVMAX.Name",
    display_name="Tapu Koko VMAX",
    searchable_by=["Tapu Koko VMAX", "VMAX", "TapuKokoVMAX"],
    subtypes=["VMAX"],
    collector_number=51,
    set_code="SWSH5",
    rarity=Rarities.RareHoloVMAX,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=320,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoV.Name",
    family_id=785,
    abilities=[
        Attack(
            title="Max Shock",
            game_text="If you have more Prize cards remaining than your opponent, their Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=max_shock,
        ),
    ],
)