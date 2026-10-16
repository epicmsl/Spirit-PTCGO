from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

card = PokemonCardDef(
    guid="2fe0d020-0699-5082-a596-5017ee3a4a2f",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name",
    display_name="Rookidee",
    searchable_by=["Rookidee", "Basic", "Rookidee"],
    subtypes=["Basic"],
    collector_number=174,
    set_code="SWSH45",
    rarity=Rarities.Shining,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=821,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
