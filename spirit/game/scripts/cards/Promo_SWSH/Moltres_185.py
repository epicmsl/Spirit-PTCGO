from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import inferno_wings

card = PokemonCardDef(
    guid="b5e75c02-329e-55a7-9565-ea3487ba19be",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=185,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Attack(
            title="Inferno Wings",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 70 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=inferno_wings(70),
        ),
    ],
)
