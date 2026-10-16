from spirit.game.card_effects.trainers import brandon, brandon_playable
from spirit.game.data_utils import SupporterCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = SupporterCardDef(
    guid="f759f60f-584d-592b-b7f8-b5ee70c4239b",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brandon.Name",
    display_name="Brandon",
    searchable_by=["Brandon", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    effect=brandon,
    condition=brandon_playable,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SUNPILLAR])
)
