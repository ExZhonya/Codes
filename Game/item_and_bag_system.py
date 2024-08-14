class WoodenSword:
	id_type= "weapon"
	id_rarity= "basic"
	id_name= "wooden sword"
	id_weap_type= "physical"
	id_weap_desc = "Just a basic sword, made of sticks.\n atk = 11"
	id_atk= 11


class WoodenStaff:
	id_type = "weapon"
	id_rarity = "basic"
	id_name = "wooden staff"
	id_weap_type = "magical"
	id_weap_desc = "A stick that's imbued with magical cystals.\n m.atk = 15"
	id_m_atk = 15
	id_spells= ["Tier I", "Lightning", "Stone Throw", "Light Beam"]


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


class Orange:
	id_type= "item"
	id_name= "orange"
	id_item_desc= "Just an average orange"
	id_heal = 5 


class BasicBag:
	id_type= "storage"
	id_name ="basic bag"
	bag_slots = ['','','','','','','','','','']
	id_weap_desc= "A bag made of ragged leather. Has 10 bag slots."


class BasicBagSystem:
	def __init__(self, slots, onhand, onhand_cache, incoming_item, eq):
		self.raw = 	   [slots[0], slots[1], slots[2],
						slots[3], slots[4], slots[5],
						slots[6], slots[7], slots[7],
						slots[9]]
		self.display = [slots[0].id_name, slots[1].id_name, slots[2].id_name,
						slots[3].id_name, slots[4].id_name, slots[5].id_name,
						slots[6].id_name, slots[7].id_name, slots[8].id_name,
						slots[9].id_name]
		self.item_type = [slots[0].id_type, slots[1].id_type, slots[2].id_type,
						  slots[3].id_type, slots[4].id_type, slots[5].id_type,
						  slots[6].id_type, slots[7].id_type, slots[8].id_type,
						  slots[9].id_type]
		self.onhand = onhand
		self.onhand_cache = onhand_cache
		self.incoming_item = incoming_item
		self.eq = eq
	def usebag(self):
		while True:
			print(f"Your bag has: {self.display}")
			print(f"[1]Take item [2]Check slots [3]Switch Equipment [4]Leave")
			bag_option = input("What will you do in this bag?  ")
			if bag_option == "1":
				self.takeitem()
				break
			elif bag_option == "2":
				self.howmanyslots()
				break
			elif bag_option == "3":
				self.switcheq()
				break
			elif bag_option == "4":
				break
			else:
				continue
	def howmanyslots(self):
		usablespace = 0
		for slot in self.display:
			if slot == '':
				usablespace += 1
		print(f"there are about: {usablespace} slots left in this bag.")

	def putitem(self):
		while True:
			put_item = input(f"Where would you like to store this {incoming_item.id_name}?")
			if put_item == "1":
				self.slots[0] = self.incoming_item
				self.display[0] = self.slots[0].id_name
				print(f"{self.display[0]} placed, removed from extra inventory.")
				self.display[0] = self.slots[0].id_name
				self.item_type[0] = self.slots[0].id_type
				return self.slots[0], self.display[0], self.item_type[0]
				break
	def takeitem(self):
		while True:
			take_item = input("What item to take? ")
			match take_item:
				case "1":
					self.onhand, self.onhand_cache, self.cache_name = self.raw[0], self.raw[0], self.display[0]
					print(f"{self.display[0]} taken, now in hand.")
					self.raw[0] = Empty()
					self.display[0] = self.raw[0].id_name
					self.item_type[0] = self.raw[0].id_type
					return self.raw[0], self.display[0], self.item_type[0]
					break
	def switcheq(self):
		while True:
			print(self.display)
			switchable = input('Which item will you equip? ')
			if switchable == '1':
				equipping = self.raw[0]
				print(f"{self.display[0]} is picked.")
				self.display[0] = self.raw[0].id_name
				self.item_type[0] = self.raw[0].id_type
				self.switch_eq_current(equipping)
				break
			elif switchable == '3':
				equipping = self.raw[2]
				print(f"{self.display[2]} is picked.")
				self.display[2] = self.raw[2].id_name
				self.item_type[2] = self.raw[2].id_type
				self.switch_eq_current(equipping)
				break
			elif switchable == '4':
				equipping = self.raw[3]
				print(f"{self.display[3]} is picked.")
				self.display[3] = self.raw[3].id_name
				self.item_type[3] = self.raw[3].id_type
				self.switch_eq_current(equipping)
				break 

	def switch_eq_current(self, equipping):
		while True:
			show_equips()
			print(f"[1]{self.eq[0].id_name} [2]{self.eq[1].id_name} [3]{self.eq[2].id_name} [4]{self.eq[3].id_name} [5]{self.eq[4].id_name} [6]Cancel")
			switch_to = input(f"Where will you switch {equipping.id_name} to? ")
			if switch_to == "1":
				if equipping.id_type == "weapon":
					self.eq[0] = equipping
					print(f"Successfully equipped {equipping.id_name}!")
					break 
				else:
					print("You cannot equip that in the weapons.")
					continue
			elif switch_to == "4":
				if equipping.id_type == "armor_head":
					self.eq[3] = equipping
					print(f"Successfully equipped {equipping.id_name}!")
					return self.eq[2]
					break
				else:
					print("You cannot equip that in the head.")
					continue
			elif switch_to == "6":
				break
			

class WeaponOutcomes:
	oncoming_dmg = 0
	turns = 0
	lightning_dmg_constant = 1.5
	stone_throw_dmg_constant = 2.5
	def determine(self):
		if eq[0].id_weap_type == "physical":
			print(f"You swung {eq[0].id_name} for {eq[0].id_atk} atk!")
		elif eq[0].id_weap_type == "magical":
			print(f"Tier of spell in {eq[0].id_name}: {eq[0].id_spells[0]}")
			self.magical_use()

	def magical_use(self):
		while True:
			magic_option = input(f"Available Spells on {eq[0].id_name}: [1]{eq[0].id_spells[1]} [2]{eq[0].id_spells[2]}")
			if magic_option == "1":
				self.use_spell(eq[0].id_spells[0], eq[0].id_spells[1], eq[0].id_m_atk)
				break
			if magic_option == "2":
				self.use_spell(eq[0].id_spells[0], eq[0].id_spells[2], eq[0].id_m_atk)
				continue

	def use_spell(self, tier_spell, used_spell, m_atk):
		if tier_spell == "Tier I":
			self.oncoming_dmg += 1
			if used_spell == "Lightning":
				lightning_dmg = m_atk * (self.oncoming_dmg + self.lightning_dmg_constant)
				print(f"Used Lightning to generate {lightning_dmg} lightning dmg!")
			if used_spell == "Stone Throw":
				self.turns += 1
				if self.turns == 1:
					print(f"Charging {used_spell}...")
				elif self.turns == 2:
					stone_dmg = m_atk * (self.oncoming_dmg + self.stone_throw_dmg_constant)
					print(f"Used Stone Throw to generate {stone_dmg} stone dmg!")

	

#=================TIER=1============================#

eq = [WoodenSword(), WoodenShield(), WoodenTorsoArmor(), WoodenHeadArmor(), WoodenLegArmor(), BasicBag()]
inventory = [SimplePotion(), SimpleManaPot(), WoodenStaff(), WoodenHeadArmor(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()]
onhand = "none"
onhand_cache = "none"
cache_name = "none"
incoming_item = SimplePotion()
bag = BasicBagSystem(inventory, onhand, onhand_cache, incoming_item, eq)

def show_equips():
	print(f"Weapon: {eq[0].id_name}")
	print(f"Shield: {eq[1].id_name}")
	print(f"Body Armor: {eq[2].id_name}")
	print(f"Helmet: {eq[3].id_name}")
	print(f"Leggings: {eq[4].id_name}")
	print(f"Bag: {eq[5].id_name}")

def use_current_potion(using):
	if using.id_rarity == "basic":
		basicpot = SimplePotion.id_heal
		print(f"You used {using.id_name} for {basicpot}!")


def use_current_manapot(using):
	if using.id_rarity == "basic":
		manapot = SimpleManaPot.id_manaheal
		print(f"You've refilled {manapot.id_manaheal} of mana with {manapot.id_name}!")

def null():
	return "Nothing happened."

def use_onhand(onhand):
	if onhand == "none":
		print("You have no onhand items.")
	else:
		if onhand.id_type == "healthpot":
			use_current_potion(onhand)
		if onhand.id_type == "manapot":
			use_current_manapot()
		else:
			null()
		onhand = "none"
	return onhand

def put_storage(incoming_item):
	if incoming_item.id_type in ("item", "healthpot", "manapot", "sword", "shield"):
		bag.putitem()
		incoming_item = "none"

def check_incoming(incoming_item):
	if incoming_item != "none":
		print(f"You have a {incoming_item.id_name} in the extra slot, want to store it? ")
		e_item_choice = input("y/n: ")
		if e_item_choice == "y":
			print("yes.")
			put_storage()
		else:
			check_incoming()
	else:
		print("You have no incoming items.")

def weapon_usage():
	while True:
		print(f"You're currently using {eq[0].id_name}.")
		print("[1]Use [2]Check description")
		weap_choices = input("How will you use it? ")
		if weap_choices == "1":
			weap_outcomes = WeaponOutcomes()
			weap_outcomes.determine()
			continue
		elif weap_choices == "2":
			print(f"{eq[0].id_weap_desc}")
			continue
		elif weap_choices == "3":
			break
		else:
			continue
while True:
	item_options = input(f"What will you do? \n[1]Show eqipment\n[2]Open Bag\n[3]Use onhand item\n[4]incoming item\n[5]Use weapon\n[6]Switch equip\n[9]Leave: ")

	if  item_options == "1":
		show_equips()
		continue
	elif item_options == "2":
		bag.usebag()
		continue
	elif item_options == "3":
		use_onhand(onhand)
		continue
	elif item_options == "4":
		check_incoming(incoming_item)
		continue
	elif item_options == "5":
		weapon_usage()
	elif item_options == "6":
		bag.switcheq()
	elif item_options == "9":
		break
	else:
		continue
