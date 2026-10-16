from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import be_prepared

card = PokemonCardDef(
    guid="73316e85-8b8d-5bdc-9fb9-8fbdd96055bc",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=175,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Be Prepared",
            game_text="Attach a basic Energy card from your hand to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=be_prepared(),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
