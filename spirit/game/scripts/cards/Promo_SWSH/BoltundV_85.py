from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import bolt_storm, electrify

card = PokemonCardDef(
    guid="5fa20639-3f96-55a0-a214-022adfc17711",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BoltundV.Name",
    display_name="Boltund V",
    searchable_by=["Boltund V", "Basic", "V", "BoltundV"],
    subtypes=["Basic", "V"],
    collector_number=85,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=836,
    abilities=[
        Attack(
            title="Electrify",
            game_text="Search your deck for up to 2 Lightning Energy cards and attach them to your Benched Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=electrify(),
        ),
        Attack(
            title="Bolt Storm",
            game_text="This attack does 30 more damage for each Lightning Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=bolt_storm(30),
        ),
    ],
)
