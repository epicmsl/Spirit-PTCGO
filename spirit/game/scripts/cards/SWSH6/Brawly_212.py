from spirit.game.data_utils import SupporterCardDef, subtypes_for, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.support_common import search_to_bench


def _is_basic_rapid_strike(card):
    return is_basic_pokemon(card) and "Rapid Strike" in subtypes_for(card.archetype_id)


card = SupporterCardDef(
    guid="f63f409b-895c-5959-b17e-95d32b3fbb04",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brawly.Name",
    display_name="Brawly",
    searchable_by=["Brawly", "Supporter", "Rapid Strike"],
    subtypes=["Supporter", "Rapid Strike"],
    collector_number=212,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    effect=search_to_bench(_is_basic_rapid_strike, count=3),
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET])
)
