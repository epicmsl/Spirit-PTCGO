from spirit.game.card_effects.trainers import PathToThePeakPassive
from spirit.game.data_utils import StadiumCardDef, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects

card = StadiumCardDef(
    passive=PathToThePeakPassive(),
    guid="e55d0fe8-022a-5fc1-88bb-2f1c151e6615",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PathtothePeak.Name",
    display_name="Path to the Peak",
    searchable_by=["Path to the Peak", "Stadium"],
    subtypes=["Stadium"],
    collector_number=213,
    set_code="SWSH10",
    rarity=Rarities.RareSecret,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET])
)
