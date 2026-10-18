from spirit.game.data_utils import ItemCardDef, unimplemented, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.cel25_effects import imposter_professor_oak

card = ItemCardDef(
    guid="c3a7c851-e299-50a6-905d-245181e25a3b",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImposterProfessorOak.Name",
    display_name="Imposter Professor Oak",
    searchable_by=["Imposter Professor Oak", "Item"],
    subtypes=["Item"],
    collector_number=28,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    effect=imposter_professor_oak,
)
