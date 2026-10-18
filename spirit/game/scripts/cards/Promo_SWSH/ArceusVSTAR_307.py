from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import starbirth, trinity_charge

card = PokemonCardDef(
    guid="9a849222-c78f-540d-bc93-fa3d3b57f767",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusVSTAR.Name",
    display_name="Arceus VSTAR",
    searchable_by=["Arceus VSTAR", "VSTAR", "ArceusVSTAR"],
    subtypes=["VSTAR"],
    collector_number=307,
    set_code="Promo_SWSH",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR]),
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusV.Name",
    family_id=493,
    abilities=[
        Attack(
            title="Trinity Nova",
            game_text="Search your deck for up to 3 basic Energy cards and attach them to your Pok\u00e9mon V in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=trinity_charge(),
        ),
        Ability(
            title="[VSTAR Power][Ability] Starbirth",
            game_text="During your turn, you may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck. (You can't use more than 1 {VSTAR} Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            effect=starbirth(),
            vstar=True,
        ),
    ],
)
