class WoodenSword:
	id_type= "weapon"
	id_rarity= "basic"
	id_name= "wooden sword"
	id_atk= 11

class WoodenShield:
	id_type= "shield"
	id_rarity= "basic"
	id_name = "wooden shield"
	id_passive_def= 11
	id_allow_block = True

class WoodenTorsoArmor:
	id_type= "armor_body"
	id_rarity= "basic"
	id_name = "wooden armor(torso)"
	id_passive_def = 11

class WoodenHeadArmor:
	id_type= "armor_head"
	id_rarity= "basic"
	id_name = "wooden armor(helmet)"
	id_passive_def = 11

class WoodenLegArmor:
	id_type= "armor_leg"
	id_rarity= "basic"
	id_name = "wooden armor(leggings)"
	id_passive_def = 11

class SimplePotion:
	id_type= "healthpot"
	id_rarity= "basic"
	id_name= "simple potion"
	id_heal= 20

class SimpleManaPot:
	id_type= "manapot"
	id_rarity= "basic"
	id_name= "simple mana potion"
	id_manaheal= 30

class Empty:
	id_type= "null"
	id_name= ""

class BasicBag:
	id_type= "storage"
	id_name ="basic bag"
	bag_slots = ['','','','','','','','','','']

class BagSystem:
	bag_slots_raw = [SimplePotion(), SimpleManaPot(), Empty(), Empty(), Empty(),
					 Empty(), Empty(), Empty(), Empty(), Empty()]
	bag_slots_dis = [bag_slots_raw[0].id_name, bag_slots_raw[1].id_name, bag_slots_raw[2].id_name, bag_slots_raw[3].id_name, bag_slots_raw[4].id_name,
					 bag_slots_raw[5].id_name, bag_slots_raw[6].id_name, bag_slots_raw[7].id_name, bag_slots_raw[8].id_name, bag_slots_raw[9].id_name]
	bag_slots_type = [bag_slots_raw[0].id_type, bag_slots_raw[1].id_type, bag_slots_raw[2].id_type, bag_slots_raw[3].id_type, bag_slots_raw[4].id_type, 
					  bag_slots_raw[5].id_type, bag_slots_raw[6].id_type, bag_slots_raw[7].id_type, bag_slots_raw[7].id_type, bag_slots_raw[9].id_type]
	def usebag(self):
		while True:
			print(f"Your bag has: {self.bag_slots_dis}")
			print(f"[1]Take item [2]Check slots [3]Leave")
			bag_option = input("What will you do in this bag?")
			if bag_option == "1":
				self.takeitem()
				break
			elif bag_option == "2":
				self.howmanyslots()
				break
			elif bag_option == "3":
				break
			else:
				continue
	def howmanyslots(self):
		usablespace = 0
		for slot in self.bag_slots_dis:
			if slot == '':
				usablespace += 1
		print(f"there are about: {usablespace} slots left in this bag.")

	def takeitem(self):
		global onhand
		global onhand_cache
		global cache_name
		while True:
			take_item = input("What item to take? ")
			match take_item:
				case "1":
					onhand = self.bag_slots_raw[0]
					onhand_cache, cache_name = self.bag_slots_raw[0], self.bag_slots_dis[0]
					print(f"{self.bag_slots_dis[0]} taken, now in hand.")
					self.bag_slots_raw[0] = Empty()
					self.bag_slots_dis[0] = self.bag_slots_raw[0].id_name
					self.bag_slots_type[0] = self.bag_slots_raw[0].id_type
					return self.bag_slots_raw[0], self.bag_slots_dis[0], self.bag_slots_type[0]
					break
#=================TIER=1============================#

eq = [WoodenSword(), WoodenShield(), WoodenTorsoArmor(), WoodenHeadArmor(), WoodenLegArmor(), BasicBag()]
onhand = "none"
onhand_cache = "none"
cache_name = "none"
bag = BagSystem()
def show_equips():
	print(f"Sword: {eq[0].id_name}")
	print(f"Shield: {eq[1].id_name}")
	print(f"Body Armor: {eq[2].id_name}")
	print(f"Helmet: {eq[3].id_name}")
	print(f"Leggings: {eq[4].id_name}")
	print(f"Bag: {eq[5].id_name}")

def use_current_potion():
	global onhand_cache
	global cache_name
	if onhand_cache.id_rarity == "basic":
		basicpot = SimplePotion.id_heal
		print(f"You used {cache_name} for {basicpot}!")
def use_current_manapot():
	return f"You've refilled {manapot.id_manaheal} of mana with {manapot.id_name}!"

def null():
	return "Nothing happened."

def use_onhand():
	global onhand
	if onhand.id_type == "healthpot":
		use_current_potion()
	if onhand.id_type == "manapot":
		use_current_manapot()
	else:
		null()

while True:
	item_options = input(f"What will you do? \n[1]Show eqipment\n[2]Open Bag\n[3]Use onhand item\n[4]Leave: ")

	if  item_options == "1":
		show_equips()
		continue
	elif item_options == "2":
		bag.usebag()
		continue
	elif item_options == "3":
		use_onhand()
		continue
	elif item_options == "4":
		break
	else:
		continue
