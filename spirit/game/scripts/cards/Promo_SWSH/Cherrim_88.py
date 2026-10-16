from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.data_utils import Activations
from spirit.game.card_effects.promo_swsh_effects import spring_bloom

card = PokemonCardDef(
    guid="6b9c93b3-3495-532e-8043-85e7a861cdb5",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name",
    display_name="Cherrim",
    searchable_by=["Cherrim", "Stage 1", "Cherrim"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    family_id=420,
    abilities=[
        Ability(
            title="Spring Bloom",
            game_text="As often as you like during your turn, you may attach a Grass Energy card from your hand to 1 of your Pok\u00e9mon that doesn't have a Rule Box (Pok\u00e9mon , Pok\u00e9mon GX Attack, etc. have Rule Boxes).",
            effect=spring_bloom(),
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
