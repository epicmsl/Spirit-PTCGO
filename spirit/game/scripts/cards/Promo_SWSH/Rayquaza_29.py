from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import jaw_lock, power_blast

card = PokemonCardDef(
    guid="b309602f-789c-5cee-9055-147994b7ca8e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Attack(
            title="Jaw Lock",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=jaw_lock(),
        ),
        Attack(
            title="Power Blast",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=power_blast(),
        ),
    ],
)
