from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="32920cbd-b301-5c50-bcaa-63e2717a2619",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    display_name="Skwovet",
    searchable_by=["Skwovet", "Basic", "Skwovet"],
    subtypes=["Basic"],
    collector_number=172,
    set_code="SWSH45",
    rarity=Rarities.Shining,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=819,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
