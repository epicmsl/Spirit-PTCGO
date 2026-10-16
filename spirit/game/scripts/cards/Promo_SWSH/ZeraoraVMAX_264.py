from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import max_fist, reactive_pulse

card = PokemonCardDef(
    guid="43260a37-a5a2-5d61-bc7b-0ec79eabb7bc",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraVMAX.Name",
    display_name="Zeraora VMAX",
    searchable_by=["Zeraora VMAX", "VMAX", "ZeraoraVMAX"],
    subtypes=["VMAX"],
    collector_number=264,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVMAX,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=320,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraV.Name",
    family_id=807,
    abilities=[
        Attack(
            title="Reactive Pulse",
            game_text="This attack does 60 damage for each of your opponent's Pok\u00e9mon in play that has an Ability.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=60,
            damage_operator="x",
            effect=reactive_pulse(60),
        ),
        Attack(
            title="Max Fist",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=max_fist(2),
        ),
    ],
)
