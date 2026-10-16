from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import damage_per, count_bench

card = PokemonCardDef(
    guid="09798e82-27b0-57df-8932-e08faa975de0",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MRayquazaEX.Name",
    display_name="M Rayquaza-EX",
    searchable_by=["M Rayquaza-EX", "MEGA", "EX", "MRayquazaEX"],
    subtypes=["MEGA", "EX"],
    collector_number=48,
    set_code="CEL25",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    family_id=384,
    abilities=[
        Attack(
            title="Emerald Break",
            game_text="This attack does 30 damage times the number of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_bench("mine"), per=30),
        ),
    ],
)
