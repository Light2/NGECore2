import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('falumpaset')
	mobileTemplate.setLevel(24)
	mobileTemplate.setMinLevel(20)
	mobileTemplate.setMaxLevel(30)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)

	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Herbivore Meat")
	mobileTemplate.setMeatAmount(12)
	mobileTemplate.setHideType("Leathery Hide")
	mobileTemplate.setHideAmount(8)
	mobileTemplate.setBoneType("Animal Bones")
	mobileTemplate.setBoneAmount(7)
	mobileTemplate.setSocialGroup("self")
	mobileTemplate.setAssistRange(2)
	mobileTemplate.setStalker(False)
	mobileTemplate.setOptionsBitmask(Options.ATTACKABLE)
	
	templates = Vector()
	templates.add('object/mobile/shared_falumpaset.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', WeaponType.UNARMED, 1.0, 6, 'kinetic')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	attacks.add('bm_bite_1')
	attacks.add('bm_kick_1')
	attacks.add('bm_provoke_1')
	attacks.add('bm_spit_1')
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('falumpaset', mobileTemplate)
	return