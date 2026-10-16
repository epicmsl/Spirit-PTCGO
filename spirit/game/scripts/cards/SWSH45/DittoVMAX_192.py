from spirit.game.data_utils import PokemonCardDef, Attack, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import max_transform

card = PokemonCardDef(
    guid="55c02562-ddd5-5649-873a-708e61bf3520",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DittoVMAX.Name",
    display_name="Ditto VMAX",
    searchable_by=["Ditto VMAX", "VMAX", "DittoVMAX"],
    subtypes=["VMAX"],
    collector_number=192,
    set_code="SWSH45",
    rarity=Rarities.RareHoloVMAX,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET]),
    hp=320,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DittoV.Name",
    family_id=132,
    abilities=[
        Attack(
            title="Max Transform",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=max_transform(),
        ),
    ],
)
