import item_assets as item
import time

# Note: we wanna have NO while loops in the assets files, only in the engine, i'll remove the while loop here in the future, and move it in the main loop of the game
# Note for Lua: the "self" before any variable is a "locator" keyword, it means it'll access the variable (e.g. 'eq') in it's own class(self.variable = own class.variable/function etc.)
# This WILL error if you run it





class Database:
	i = [item.orange, item.empty, item.empty, item.empty, item.empty, item.empty, item.empty, item.empty, item.empty, item.empty] 
		# sets i(short for inventory) that is coded in a list, can be accessed by using import(import inventory_system).class(database).i(this thing)
	eq = [item.w_helmet, item.w_armor, item.w_legging, item.w_sword, item.w_shield] 
		# same with here, just do import.class.eq to access it
	h_item = item.orange
		# sets the held item to an orange :3
	state = "Available"

	def __str__(self):
		return "Basic Bag"

		# Difficulty: VERY EASY TO UNDERSTAND
	def show_inventory(self): # This function, as the name suggest calls the inventory(i) and displays it properly
		print(f"""
Current Inventory:
1.  {self.i[0]}
2.  {self.i[1]}
3.  {self.i[2]}
4.  {self.i[3]}
5.  {self.i[4]}
6.  {self.i[5]}
7.  {self.i[6]}
8.  {self.i[7]}
9.  {self.i[8]}
10. {self.i[9]}""")


		# Difficulty: VERY EASY TO UNDERSTAND
	def equipt_display(self): # Same with inventory, but just accesses the equipment list variabe(eq) 
		print(f"""
Current Equipment: 
 Head: {self.eq[0]}
 Body: {self.eq[1]}
 Leg:  {self.eq[2]}
 Left: {self.eq[3]}
 Main: {self.eq[4]}""")

		# Difficulty: VERY EASY TO UNDERSTAND
	def current_hold(self): # Shows the current held item(h_item in top of the class)
		print(f"""\nCurrently Holding: {self.h_item}\n""")


		# Difficulty: UNDERSTOOD IF YOU READ THE COMMENTS, NORMAL DIFFICULTY
	def access_inventory(self):
		# For this, since most of the functionality that this thing needs already exists, we'll just rename it as a held item first before sending it away

		self.show_inventory()
		a = input("Which item would you like to use [C]ancel: ")
		match a:
			case "1":
				self.h_item = self.i[0] # Turns the first spot to the held item, but we wont empty it our yet, that happens at the functions this will redirect to
			case "2":
				self.h_item = self.i[1] 
			case "3":
				self.h_item = self.i[2] 
			case "4":
				self.h_item = self.i[3] 
			case "5":
				self.h_item = self.i[4] 
			case "6":
				self.h_item = self.i[5] 
			case "7":
				self.h_item = self.i[6] 
			case "8":
				self.h_item = self.i[7] 
			case "9":
				self.h_item = self.i[8] 
			case "10":
				self.h_item = self.i[9] 

		if a not in ("C", "c", "cancel"): # If it's not canceled, we run the function, if it is canceled, nothing happens
			self.h_item_use() # Once we've set the slots as a held item, we'll run the function of held item use



		# Difficulty: HAVE TO READ THE COMMENTS AND ASK ME, VERY HARD TO UNDERSTAND
	def h_item_use(self):
		# This uses the held item, which can be used, thrown or stored in the inventory.
		print("==============================")
		self.current_hold()
		print("==============================")
		if self.h_item.id_type in ("item", "healthpot", "manapot"):  
			# Checks if the held item is an item, a health potion or a manapot 
			# (We grouped them, but if we wanna pin down the item type, we'll use a function, because i dont want a mega function that does everything, only the main looop does that)
			
			a = input("What would you like to do with this item?\n [Use]the item \n[Throw] away \n [Store]in the inventory")
			if a in ("use", "Use", "USE", "1"):
				using = self.h_item  # sets the item held as a 'using' state
				self.use_item(using)  # runs the use item function with the using variable, tho you can shorten it altogether by making it self.use_item(self.h_item), but that's too long kek
			if a in ("throw", "Throw", "THROW", "2"):
				throwing = self.h_item
				self.throw_item(throwing)
			if a in ("store", "Store", "STORE", "3"):
				storing = self.h_item
				self.store_item(storing)
			else:
				self.h_item_use()

		elif self.h_item.id_type in ("armor_body", "armor_leg", "armor_head", "shield", "weapon"):
			# If it's an equipable, then we just run the equipment function again
			self.change_equip(self.h_item)

		elif self.h_item.id_type in ("null"):
			print("Y'know that there's no items here, yet you used it, bitch ass.")
			time.sleep(3)

		self.h_item = item.empty # Once everything is done, it'll set the held item to empty. ask me for any complex question


		# Difficulty: YOU HAVE TO READ THE COMMENTS, VERY HARD TO UNDERSTAND
	def use_item(self, using):
		# Note: if we're using the item, we should identify which item it is first, which we do by acessing their id type

		if using.id_type == "healthpot": # checks if the item we're using is a health potion
			if using.id_rarity == 'basic': # checks the rarity
				# WILL ADD A THINGY THAT ADDS HP TO THE PLAYER IN THE FUTURE
				print(f'used a basic potion! healed for {using.id_heal}!')

		elif using.id_type == "item":
			# uhhh.... idk what you'll use an item for.... so uhh... maybe if it's a consumable, but not all is a consumable! maybe can be ingredient???
			pass
		elif using.id_type == "manapot":
			if using.id_rarity == 'basic':
				# WILL ADD A THINGY FOR MANA STATS FOR THE PLAYER IN THE FUTURE
				print(f"used a basic mana potion! regained {using.id_manaheal}!")


		# Difficulty: VERY EASY TO UNDERSTAND
	def throw_item(self, throwing):
		# We'll add a confirmation first if the player wants to throw it away.
		a = input("Sure to throw away {throwing}?")
		if a in ("y", "yes"):
			self.h_item = item.empty # sets the held item as empty
		else:
			self.h_item = throwing # reverts back the throwing variable to the h_item

		# Difficulty: VERY EASY TO UNDERSTAND
	def store_item(self, storing):
		self.show_inventory()
		print("===============================")
		a = input("Which slot will you store it in? ")
		match a:
			case "1":
				self.i[0] = storing # Sets that slot with the storing/stored item
			case "2":
				self.i[1] = storing
			case "3":
				self.i[1] = storing
			case "4":
				self.i[1] = storing
			case "5":
				self.i[1] = storing
			case "6":
				self.i[1] = storing
			case "7":
				self.i[1] = storing
			case "8":
				self.i[1] = storing
			case "9":
				self.i[1] = storing
			case "10":
				self.i[1] = storing

		# Difficulty: VERY EASY TO UNDERSTAND, IF YOU READ THE COMMENTS	
	def select_item(self):
		self.show_inventory()
		head_choice = input("Which item will you equip? ") # Asks which slot in the inventory will they switch into, we'll do this in all of the slots
		match head_choice: 
			case "1":
				self.change_equip(self.i[0]) # Explanation (self). runs the change equip function, with the value of whatever is in the first slot
				self.i[0] = item.empty # once the function is done, the first slot will be empty
			case "2":
				self.change_equip(self.i[1])
				self.i[1] = item.empty
			case "3":
				self.change_equip(self.i[2])
				self.i[2] = item.empty
			case "4":
				self.change_equip(self.i[3])
				self.i[3] = item.empty 
			case "5":
				self.change_equip(self.i[4])
				self.i[4] = item.empty
			case "6":
				self.change_equip(self.i[5])
				self.i[5] = item.empty
			case "7":
				self.change_equip(self.i[6])
				self.i[6] = item.empty
			case "8":
				self.change_equip(self.i[7])
				self.i[7] = item.empty 
			case "9":
				self.change_equip(self.i[8])
				self.i[8] = item.empty 
			case "10":
				self.change_equip(self.i[9])
				self.i[9] = item.empty  # The reason it stops at [9] and not 10, because lists are numbered 0-9, which counts 1-10.
			

		# Difficulty: READ THE COMMENTS TO UNDERSTAND
	def change_equip(self, selected_item):
		if selected_item.id_type not in ("weapon", "shield", "armor_head", "armor_body", "armor_leg"):
			print(f"You can't wear an {selected_item}, you fucking muppet.")
			self.select_item()
		print("""===========================""")
		self.equipt_display()
		print("""===========================""")
		print(f"Selected: {selected_item}")
		print("""===========================""")
		inpt = input("Which equipment will you switch to?")

		if inpt in ("head", "Head", "1"):
			if selected_item.id_type == "helmet": # the id_type came from the item_assets file, every class has one so we can distinguish them properly
				self.eq[0] = selected_item  # Once confirmed that it has the id type of a helmet, it'll successfully replace it(self.eq[0]) with the selected item(selected_item)
			else:
				print("You cannot equip this in your head.")
				self.select_item()
		
		elif inpt in ("body", "Body", "2"):
			if selected_item.id_type == "armor_body": 
				self.eq[1] = selected_item 
			else:
				print("You cannot equip this in your body.")
				self.select_item()

		elif inpt in ("leg", "Leg", "3"):
			if selected_item.id_type == "armor_leg": 
				self.eq[2] = selected_item 
			else:
				print("You cannot equip this in your legs.")
				self.select_item()

		elif inpt in ("left", "Left", "4"):
			if selected_item.id_type == "shield": 
				self.eq[3] = selected_item 
			else:
				print("You cannot equip this in your left hand.")
				self.select_item()

		elif inpt in ("main", "Main", "5"):
			if selected_item.id_type == "weapon": 
				self.eq[4] = selected_item 
			else:
				print("You cannot equip this in your main hand.")
				self.select_item()

		elif inpt in ("back", "Back", "6"):
			self.select_item() # Instead of running a loop here, we could avoid that by running the function above instead
		else:
			print("Error, retry again.")



database = Database()