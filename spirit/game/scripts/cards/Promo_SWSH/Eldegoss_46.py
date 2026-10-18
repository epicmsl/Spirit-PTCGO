from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import blessing_of_fluff

card = PokemonCardDef(
    guid="7eca9f60-fe28-5729-b91d-62a9fd63c991",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eldegoss.Name",
    display_name="Eldegoss",
    searchable_by=["Eldegoss", "Stage 1", "Eldegoss"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="Promo_SWSH",
    rarity=Rarities.Rare,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.COSMOS]),
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name",
    family_id=829,
    abilities=[
        Attack(
            title="Blessing of Fluff",
            game_text="Search your deck for up to 3 Grass Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=blessing_of_fluff(),
        ),
        Attack(
            title="Leafage",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
