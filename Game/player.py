import os, time

class Player:
	def __init__(self, name="Player", hp=20, mp=15, strength=1, intelligence=1, defense=1, level=1, stat_points=0, exp=0, exp_needed=300, gold=0):
		self.name = name
		self.hp = hp
		self.max_hp = self.hp
		self.mp = mp
		self.max_mp = self.mp
		self.strength = strength
		self.intelligence = intelligence
		self.defense = defense
		self.level = level
		self.stat_points = stat_points
		self.exp = exp
		self.exp_needed = exp_needed
		self.gold = gold

	def display_stats(self): #FOR WHILE IN INN/HOUSE
		os.system("cls" if os.name == "nt" else "clear")
		print(f"{'='*30}")
		print(f"Character: {self.name}")
		print(f"{'='*30}")
		print(f"{'Stat':<10} | {'Value':<5}")
		print(f"{'-'*30}")
		print(f"{'Health (HP)':<10}| {self.max_hp:<5}")
		print(f"{'Mana (MP)':<10} | {self.max_mp:<5}")
		print(f"{'Strength':<10} | {self.strength:<5}")
		print(f"{'Defense':<10} | {self.defense:<5}")
		print(f"{'Level':<10} | {self.level:<5}")
		print(f"{'Exp':<10} | {self.exp}/{self.exp_needed}")
		print(f"Stat Points Available: {self.stat_points}")
		print(f"{'='*30}")
		
		if self.stat_points:
			print("[1] Allocate Stats")
			if input() == "1":
				self.stats_up()

	def level_up(self):
		if self.exp >= self.exp_needed:
			print(f"Congratulations! You are now level {self.level + 1}")
			time.sleep(3)
			self.level += 1
			self.exp -= self.exp_needed
			self.exp_needed = intelligence(self.exp_needed * 1.2)
			self.exp = 0
			self.stat_points += 2

	def stats_up(self):
		choice_display = """
			Choose a stat to increase:
			[1] HP(+5)
			[2] MP(+5)
			[3] Strength(+1)
			[4] Intelligence(+1)
			[5] Defense(+1)
			"""
		for point in range(self.stat_points):
			print(choice_display)
			x = input()
			if x == "1":
				self.max_hp += 5
				print(f"You now have {self.max_hp} Max HP!")
			elif x == "2":
				self.max_mp += 5
				print(f"You now have {self.max_mp} Max MP!")
			elif x == "3":
				self.strength += 1
				print(f"You now have {self.strength} Strength!")
			elif x == "4":
				self.intelligence += 1
				print(f"You now have {self.intelligence} Intelligence!")
			elif x == "5":
				self.defense += 1
				print(f"You now have {self.defense} Defense!")

			self.stat_points -= 1
			print(f"You have {self.stat_points} stat points left.")

		input("You have no more points left.")
		self.display_stats()


	def get_exp(self, exp):
		self.exp += exp
		print(f"You have received {exp} exp!")
		if self.exp >= self.exp_needed:
			self.level_up()
			self.display_stats()


player = Player()

if __name__ == "__main__":
	player = Player()
	player.stat_points += 2
	player.display_stats()
