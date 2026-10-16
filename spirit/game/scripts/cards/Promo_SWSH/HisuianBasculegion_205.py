from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import grudge_dive

card = PokemonCardDef(
    guid="18d7d859-774e-5740-b4d8-1a246ac2cea8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculegion.Name",
    display_name="Hisuian Basculegion",
    searchable_by=["Hisuian Basculegion", "Stage 1", "HisuianBasculegion"],
    subtypes=["Stage 1"],
    collector_number=205,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculin.Name",
    family_id=550,
    abilities=[
        Attack(
            title="Grudge Dive",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an attack from your opponent's Pok\u00e9mon during their last turn, this attack does 90 more damage, and your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="+",
            effect=grudge_dive(90),
        ),
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
