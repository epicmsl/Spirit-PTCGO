from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="178071b3-5655-56d6-90e6-1ae09d80af25",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    display_name="Toxel",
    searchable_by=["Toxel", "Basic", "Toxel"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SWSH45",
    rarity=Rarities.Shining,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=848,
    abilities=[
        Attack(
            title="Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
