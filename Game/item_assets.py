
# Note: we wanna have NO while loops in the assets files, only in the engine, i'll remove the while loop here in the future, and move it in the main loop of the game

class WoodenSword:
	id_type= "weapon"
	id_rarity= "basic"
	id_weap_type= "physical"
	id_weap_desc = "Just a basic sword, made of sticks.\natk = 11"
	id_atk= 11
	id_skill_tier = "Tier I"
	id_skills= ["Rage", "Charging Thrust", "Holy Imbued"]

	def __str__(self):
		return "[Wooden Sword]"


class WoodenStaff:
	id_type = "weapon"
	id_rarity = "basic"
	id_weap_type = "magical"
	id_weap_desc = "A stick that's imbued with magical cystals.\nm.atk = 15"
	id_m_atk = 15
	id_spell_tier = "Tier I"
	id_spells= ["Lightning", "Stone Throw", "Light Beam"]

	def __str__(self):
		return "[Wooden Staff]"


class WoodenShield:
	id_type= "shield"
	id_rarity= "basic"
	id_passive_def= 11
	id_allow_block = True

	def __str__(self):
		return "[Wooden Shield]"

class WoodenTorsoArmor:
	id_type= "armor_body"
	id_rarity= "basic"
	id_passive_def = 11

	def __str__(self):
		return "[Wooden Armor]"

class WoodenHeadArmor:
	id_type= "armor_head"
	id_rarity= "basic"
	id_name = "helmet"
	id_passive_def = 11

	def __str__(self):
		return "[Wooden Helmet]"


class WoodenLegArmor:
	id_type= "armor_leg"
	id_rarity= "basic"
	id_passive_def = 11

	def __str__(self):
		return "[Wooden Leggings]"


class SimplePotion:
	id_type= "healthpot"
	id_rarity= "basic"
	id_heal= 20

	def __str__(self):
		return "[Health Potion I]"


class SimpleManaPot:
	id_type= "manapot"
	id_rarity= "basic"
	id_name= "Simple mana potion"
	id_manaheal= 30

	def __str__(self):
		return "[Mana Potion I]"


class Empty:
	id_type= "null"
	id_name= ""

	def __str__(self):
		return "[]"


class Orange:
	id_type= "item"
	id_item_desc= "Just an average orange"
	id_heal = 5 

	def __str__(self):
		return "[Orange]"


class BasicBag:
	id_type= "storage"
	id_name ="basic bag"
	id_weap_desc= "A bag made of ragged leather. Has 10 bag slots."

	def __str__(self):
		return "[Bag (Basic)]"

#===============================================================================#

class StoneSword:
	id_type= "weapon"
	id_rarity= "common"
	id_weap_type= "physical"
	id_weap_desc = "You've reached the stone age! \natk = 22"
	id_atk= 22
	id_skill_tier = "Tier II"
	id_skills= ["Rage II", "Charging Thrust II", "Holy Imbued II", "Iminent Darkness"]

	def __str__(self):
		return "[Stone Sword]"


class StoneStaff:
	id_type = "weapon"
	id_rarity = "common"
	id_weap_type = "magical"
	id_weap_desc = "A stone rod that's imbued with magical cystals.\nm.atk = 35"
	id_m_atk = 35
	id_spell_tier = "Tier II"
	id_spells= ["Lightning II", "Stone Throw II", "Light Beam II", "Clinging Shadow"]

	def __str__(self):
		return "[Stone Staff]"


class StoneShield:
	id_type= "shield"
	id_rarity= "common"
	id_passive_def= 25
	id_allow_block = True

	def __str__(self):
		return "[Stone Shield]"

class StoneTorsoArmor:
	id_type= "armor_body"
	id_rarity= "common"
	id_passive_def = 25

	def __str__(self):
		return "[Stone Armor]"

class StoneHeadArmor:
	id_type= "armor_head"
	id_rarity= "common"
	id_name = "helmet"
	id_passive_def = 25

	def __str__(self):
		return "[Stone Helmet]"


class StoneLegArmor:
	id_type= "armor_leg"
	id_rarity= "common"
	id_passive_def = 25

	def __str__(self):
		return "[Stone Leggings]"


class DecentPotion:
	id_type= "healthpot"
	id_rarity= "common"
	id_heal= 50

	def __str__(self):
		return "[Health Potion II]"


class DecentManaPot:
	id_type= "manapot"
	id_rarity= "common"
	id_manaheal= 50

	def __str__(self):
		return "[Mana Potion II]"


























#Calling the class is important, if adding a new object, do this!!!!
w_sword = WoodenSword()
w_staff = WoodenStaff()
w_helmet = WoodenHeadArmor()
w_armor = WoodenTorsoArmor()
w_legging = WoodenLegArmor()
w_shield = WoodenShield()
s_potion = SimplePotion()
s_manapotion = SimpleManaPot()
empty = Empty()
orange = Orange()
bag_basic = BasicBag()