from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import draconic_star, giga_impact

card = PokemonCardDef(
    guid="4bca48d9-e40f-5ef0-b01e-539cc5504a24",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteVSTAR.Name",
    display_name="Dragonite VSTAR",
    searchable_by=["Dragonite VSTAR", "VSTAR", "DragoniteVSTAR"],
    subtypes=["VSTAR"],
    collector_number=236,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHoloVSTAR,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteV.Name",
    family_id=149,
    abilities=[
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=250,
            effect=giga_impact(),
            locks_next_turn=True,
        ),
        Attack(
            title="[VSTAR Power] Draconic Star",
            game_text="Look at the top 12 cards of your deck and attach any number of Water or Lightning Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck. (You can't use more than 1 {VSTAR} Power in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draconic_star(),
            vstar=True,
        ),
    ],
)
