from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects

from spirit.game.card_effects.promo_swsh_effects import crescent_glow, photon_laser

card = PokemonCardDef(
    guid="60046031-ea4f-5f73-822b-25f086421d26",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic", "Cresselia"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="Promo_SWSH",
    rarity=Rarities.RareHolo,
    foil=Foil(mask=FoilMasks.HOLO, effects=[FoilEffects.SWHOLO]),
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=488,
    abilities=[
        Attack(
            title="Crescent Glow",
            game_text="Search your deck for a Psychic Energy card and attach it to 1 of your Pok\u00e9mon. If you go second and it's your first turn, instead search for up to 3 Psychic Energy cards and attach them to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=crescent_glow(),
        ),
        Attack(
            title="Photon Laser",
            game_text="If you have at least 5 Energy in play, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="+",
            effect=photon_laser(90),
        ),
    ],
)
