from spirit.game.data_utils import ItemCardDef, unimplemented, Foil
from spirit.game.attributes import Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.cel25_effects import here_comes_team_rocket

card = ItemCardDef(
    guid="3a9b41af-815f-5ea6-b51a-0d8d2511b424",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!", "Item"],
    subtypes=["Item"],
    collector_number=30,
    set_code="CEL25",
    rarity=Rarities.RareUltra,
    foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.ANN25THCONFETTI]),
    effect=here_comes_team_rocket,
)
