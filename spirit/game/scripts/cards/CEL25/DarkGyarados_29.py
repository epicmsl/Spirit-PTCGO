from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, FoilMasks, FoilEffects
from spirit.game.content.definitions import Triggers
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.cel25_effects import final_beam

card = PokemonCardDef(
    guid="00822174-7fe9-5b9d-8d4f-62fee8a4320f",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGyarados.Name",
    display_name="Dark Gyarados",
    searchable_by=["Dark Gyarados", "Stage 1", "DarkGyarados"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Ability(
            title="Final Beam",
            game_text="When Dark Gyarados is Knocked Out by an attack, flip a coin. If heads, this power does 20 damage for each Water Energy attached to Dark Gyarados to the Pok\u00e9mon that Knocked Out Dark Gyarados. Apply Weakness and Resistance. This power doesn't work if Dark Gyarados is Asleep, Confused, or Paralyzed.",
            effect=final_beam,
            trigger=Triggers.ON_KNOCKED_OUT,
        ),
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 3},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
