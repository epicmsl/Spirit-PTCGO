from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import earthquake

card = PokemonCardDef(
    guid="7230892f-d7ce-539b-9a3d-dce37878b72d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1", "Donphan"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Attack(
            title="Earthquake",
            game_text="This attack also does 20 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=120,
            effect=earthquake(20),
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
