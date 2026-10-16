from spirit.game.data_utils import Ability, Attack, Foil, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="bd2bd566-3e66-53ee-b4cd-462321f92781",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowkingVMAX.Name",
    display_name="Galarian Slowking VMAX",
    searchable_by=["Galarian Slowking VMAX", "VMAX", "Single Strike", "GalarianSlowkingVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=100,
    set_code="SWSH6",
    rarity=Rarities.RareHoloVMAX,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowkingV.Name",
    family_id=199,
    abilities=[
        Attack(
            title="Max Toxify",
            game_text="Your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 12 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, counters=12),
        ),
    ],
)
