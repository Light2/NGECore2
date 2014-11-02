# Spawn Area file created with PSWG Planetary Spawn Tool
import sys
from java.util import Vector

def addSpawnArea(core):
	dynamicGroups = Vector()
	dynamicGroups.add('yavin4_black_sun')
	dynamicGroups.add('yavin4_choku')
	dynamicGroups.add('yavin4_skreeg')
	dynamicGroups.add('yavin4_klinik')
	core.spawnService.addDynamicSpawnArea(dynamicGroups, 5500, -4500, 3000, 'yavin4')
	return
