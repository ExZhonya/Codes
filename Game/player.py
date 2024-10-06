import os, time

class Player:
	def __init__(self, name="", hp=20, mp=15, strength=5, _int=1, defense=1, level=1, stat_points=0, exp=0, exp_needed=300):
		self.name = name
		self.hp = hp
		self.max_hp = self.hp
		self.mp = mp
		self.max_mp = self.mp
		self.strength = strength
		self.int = _int
		self.defense = defense
		self.level = level
		self.stat_points = stat_points
		self.exp = exp
		self.exp_needed = exp_needed

	def display_stats(self): #FOR WHILE IN INN/HOUSE
		os.system("cls" if os.name == "nt" else "clear")
		print(f"{'='*30}")
		print(f"Character: {self.name}")
		print(f"{'='*30}")
		print(f"{'Stat':<10} | {'Value':<5}")
		print(f"{'-'*30}")
		print(f"{'Health (HP)':<10}| {self.hp:<5}")
		print(f"{'Mana (MP)':<10} | {self.mp:<5}")
		print(f"{'Strength':<10} | {self.strength:<5}")
		print(f"{'Defense':<10} | {self.defense:<5}")
		print(f"{'Level':<10} | {self.level:<5}")
		print(f"{'Exp':<10} | {self.exp}/{self.exp_needed}")
		print(f"Stat Points Available: {self.stat_points}")
		print(f"{'='*30}")
		
		if self.stat_points > 0:
			print("[1] Allocate Stats")
			x = input()
			if x == "1":
				self.stats_up()

	def level_up(self):
		while self.exp >= self.exp_needed:
			print(f"Congratulations! You are now level {self.level + 1}")
			time.sleep(3)
			self.level += 1
			self.exp -= self.exp_needed
			self.exp_needed = int(self.exp_needed * 1.2)
			self.exp = 0
			self.stat_points += 2

	def stats_up(self):
		while self.stat_points > 0:
			print("""
			Choose a stat to increase:
			[1] HP(+5)
			[2] MP(+5)
			[3] Strength(+1)
			[4] Intelligence(+1)
			[5] Defense(+1)
			""")
			while self.stat_points > 0:
				x = input()
				if x == "1":
					self.hp += 5
					self.stat_points -= 1
					print(f"You have {self.stat_points} stat points left.")
				elif x == "2":
					self.mp += 5
					self.stat_points -= 1
					print(f"You have {self.stat_points} stat points left.")
				elif x == "3":
					self.strength += 1
					self.stat_points -= 1
					print(f"You have {self.stat_points} stat points left.")
				elif x == "4":
					self.int += 1
					self.stat_points -= 1
					print(f"You have {self.stat_points} stat points left.")
				elif x == "5":
					self.defense += 1
					self.stat_points -= 1
					print(f"You have {self.stat_points} stat points left.")
			if self.stat_points < 1:
				self.display_stats()

	def get_exp(self, exp):
		self.exp += exp
		print(f"You recieved {exp} exp!")
		if self.exp >= self.exp_needed:
			self.level_up()
			self.display_stats()

if __name__ == "__main__":
	player = Player()
	player.display_stats()
