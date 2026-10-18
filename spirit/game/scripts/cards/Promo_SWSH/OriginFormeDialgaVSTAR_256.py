from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.pokemon import star_chronos
from spirit.game.card_effects.promo_swsh_effects import metal_blast

card = PokemonCardDef(
    guid="af93acdd-3ad1-5ddd-afa2-3553a398bc9a",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormeDialgaVSTAR.Name",
    display_name="Origin Forme Dialga VSTAR",
    searchable_by=["Origin Forme Dialga VSTAR", "VSTAR", "OriginFormeDialgaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=256,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVSTAR,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=280,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VSTAR,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormeDialgaV.Name",
    family_id=483,
    abilities=[
        Attack(
            title="Metal Blast",
            game_text="This attack does 40 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=metal_blast(40),
        ),
        Attack(
            title="[VSTAR Power] Star Chronos",
            game_text="Take another turn after this one. (Skip Pok\u00e9mon Checkup.) (You can't use more than 1 {VSTAR} Power in a game.)",
            cost={PokemonTypes.METAL: 4, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=star_chronos,
            vstar=True,
        ),
    ],
)
