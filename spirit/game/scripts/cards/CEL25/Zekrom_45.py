from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import (
    damage_per, damage_counters_on, recoil_attack,
)

card = PokemonCardDef(
    guid="0061a4bd-4093-53a9-b117-056171a2b3f4",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name",
    display_name="Zekrom",
    searchable_by=["Zekrom", "Basic", "Zekrom"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="CEL25",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Outrage",
            game_text="Does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), per=10, base=20),
        ),
        Attack(
            title="Bolt Strike",
            game_text="This Pok\u00e9mon does 40 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=recoil_attack(40),
        ),
    ],
)
