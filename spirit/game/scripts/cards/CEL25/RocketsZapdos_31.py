from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.cel25_effects import electroburn

card = PokemonCardDef(
    guid="46aaa985-72f6-5801-ad9e-b44baa14962f",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsZapdos.Name",
    display_name="Rocket's Zapdos",
    searchable_by=["Rocket's Zapdos", "Basic", "RocketsZapdos"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Plasma",
            game_text="If there are any Lightning Energy cards in your discard pile, attach 1 of them to Rocket's Zapdos.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=attach_from_discard(
                predicate=is_lightning_energy, count=1, target="self",
                prompt="Choose a Lightning Energy card to attach to Rocket's Zapdos",
            ),
        ),
        Attack(
            title="Electroburn",
            game_text="Rocket's Zapdos does damage to itself equal to 10 times the number of Lightning Energy cards attached to it.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=electroburn,
        ),
    ],
)
