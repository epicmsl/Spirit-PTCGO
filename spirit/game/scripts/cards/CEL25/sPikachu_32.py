from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(
    guid="0565d19f-f26b-531c-b6c1-7d650be90d16",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.sPikachu.Name",
    display_name="_____'s Pikachu",
    searchable_by=["_____'s Pikachu", "Basic", "sPikachu"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Birthday Surprise",
            game_text="If it's not your birthday, this attack does 30 damage. If it is your birthday, flip a coin. If heads, this attack does 30 damage plus 50 more damage; if tails, this attack does 30 damage.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(50),
        ),
    ],
)
