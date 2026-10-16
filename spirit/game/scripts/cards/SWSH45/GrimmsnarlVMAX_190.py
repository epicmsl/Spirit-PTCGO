from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Foil
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, FoilMasks, FoilEffects
from spirit.game.card_effects.attacks_common import count_energy

async def g_max_drill(ctx):
    attached = count_energy('self', energy_type=PokemonTypes.DARKNESS)(ctx)
    extra = max(0, attached - 3)
    bonus = min(100, extra * 50)
    await ctx.deal_damage(170 + bonus)
card = PokemonCardDef(guid='b31fa043-7835-5c9a-ae36-155432c012c9', key='SWSH45', name='com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlVMAX.Name', display_name='Grimmsnarl VMAX', searchable_by=['Grimmsnarl VMAX', 'VMAX', 'GrimmsnarlVMAX'], subtypes=['VMAX'], collector_number=190, set_code='SWSH45', rarity=Rarities.RareHoloVMAX, foil=Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.SWSECRET]), hp=330, elements=[PokemonTypes.DARKNESS], stage=PokemonStage.VMAX, retreat_cost=3, weakness_type=PokemonTypes.GRASS, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GrimmsnarlV.Name', family_id=861, abilities=[Attack(title='G-Max Drill', game_text="This attack does 50 more damage for each extra Darkness Energy attached to this Pokémon (in addition to this attack's cost). You can't add more than 100 damage in this way.", cost={PokemonTypes.DARKNESS: 3}, damage=170, effect=g_max_drill, damage_operator='+')])
