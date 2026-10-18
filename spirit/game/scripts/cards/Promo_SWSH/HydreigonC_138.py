from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import berserker_blade

card = PokemonCardDef(
    guid="ff52178e-beef-56bb-8c31-c509a1692f20",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HydreigonC.Name",
    display_name="Hydreigon C",
    searchable_by=["Hydreigon C", "Basic", "HydreigonC"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=633,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Berserker Blade",
            game_text="This attack also does 20 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=berserker_blade(20, 2),
        ),
    ],
)
