from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import bubble_pod, max_torrent

card = PokemonCardDef(
    guid="aaa0131e-0cf7-5f1e-8ed1-4f36400a0f20",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonVMAX.Name",
    display_name="Vaporeon VMAX",
    searchable_by=["Vaporeon VMAX", "VMAX", "Rapid Strike", "VaporeonVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=182,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET]),
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonV.Name",
    family_id=134,
    abilities=[
        Attack(
            title="Bubble Pod",
            game_text="Put a Water Pok\u00e9mon from your discard pile onto your Bench. If you do, attach up to 3 Water Energy cards from your discard pile to that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bubble_pod(),
        ),
        Attack(
            title="Max Torrent",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=max_torrent(100),
        ),
    ],
)
