from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import incinerate

card = PokemonCardDef(
    guid="602c0863-946b-5b9a-a2ef-60575d9817a8",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardV.Name",
    display_name="Charizard V",
    searchable_by=["Charizard V", "Basic", "V", "CharizardV"],
    subtypes=["Basic", "V"],
    collector_number=260,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Incinerate",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=incinerate(),
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)
