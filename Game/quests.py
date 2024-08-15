# Made by: Pilgrimir
# Co-owner/Intelectual Property: Exzhonya

import os

def prettify(): # Like the preset class, but turned to a function
	print("-" * 30)


class QuestStatus:
	grass_q_status = "Incomplete" # This is an attribute that only exists in this class 
	forest_q_status = "Incomplete"
	cave_q_status = "Incomplete"

	def start_grass_quest(self): 
		while self.grass_q_status == "Incomplete": # This is just a more complicated version of an if statement, but if you read it, it'll be True 
			os.system("cls") # Just clears the terminal screen 
			prettify() 
			print("Elder:\nAdventurer! please help us, there's bandits that keep attacking us! please kill them!") # Dialogue, feel free to add more
			prettify()
			print("[1]Accept Quest [2]Decline")
			prettify()
			player_choice = input()
			if player_choice == "1":
				self.grass_q_status = "Ongoing" # This sets the status for this quest as ongoing
				prettify()
				print("Elder:\nOh thank you Adventurer! You will be rewarded plenty for this!")
				prettify()
				break
			elif player_choice == "2": # if they decline, nothing happens, but you can add something here if you want @Lua
				break

	def check_quest_collision(self):
		if "Ongoing" in (self.grass_q_status, self.forest_q_status, self.cave_q_status): # Checks if there's any ongoing quests in the three, if there is, the code runs 
			os.system("cls") # Just clears the terminal screen 
			prettify() 
			print("You're already in a quest.") # Dialogue, feel free to add more
			prettify()
	

	def start_forest_quest(self): # Just copy the same shit in grass quest, and you can display rewards, just to entice the player to accept them
		pass

	def start_cave_quest(self):  # Just copy the same shit in grass quest, and you can display rewards, just to entice the player to accept them
		pass



quest_s = QuestStatus()