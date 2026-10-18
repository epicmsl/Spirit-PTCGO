from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import stealth_poison

card = PokemonCardDef(
    guid="58717f98-2822-542e-bda2-9fe542148085",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatVMAX.Name",
    display_name="Crobat VMAX",
    searchable_by=["Crobat VMAX", "VMAX", "CrobatVMAX"],
    subtypes=["VMAX"],
    collector_number=99,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET]),
    hp=300,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatV.Name",
    family_id=169,
    abilities=[
        Attack(
            title="Stealth Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=stealth_poison(),
        ),
        Attack(
            title="Max Cutter",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)
