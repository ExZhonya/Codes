import random


class Monster:
	def __init__(self, name, level, hp, evasion_rate):
		self.name = name
		self.level = random.randint(1,5) + level
		self.hp = hp + (self.level * 2)
		self.max_hp = self.hp
		self.dmg = int(self.max_hp/2)
		self.evasion_rate = evasion_rate
		self.evade_chance = random.random()
		self.if_evaded = self.evade_chance <= self.evasion_rate

	def attack(self):
		self.display_monster()
		print(f"{self.name} dealt {self.dmg} dmg!") # debugging display
		

	def display_monster(self):
		hp = self.hp  # Current HP as an integer (percentage)
		max_hp_bar_length = 10  # Total number of bars

		hp_perc = hp / self.max_hp

		filled_bars = int(hp_perc * max_hp_bar_length)  # Each bar represents 10%

		# Create the HP bar based on the filled bars
		hp_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))

		print(f"==============================")
		print(f"|{self.name}| Lv.{self.level}         |")
		print(f"==============================")
		print(f"| HP:{self.hp} {hp_bar}        |""")
		print(f"==============================")
		print(f"|[1]Attack, [2]Defend, [3]Run|")
		print(f"==============================")

class EvolvedMonster:
	def __init__(self, name, level, hp, amount, evasion_rate):
		self.name = name
		self.amount = amount
		self.level = random.randint(1,5) + level
		self.hp = (hp + (self.level * 2)) * amount
		self.max_hp = self.hp
		self.dmg = self.max_hp/2
		self.evasion_rate = evasion_rate 
		self.evade_chance = random.random()
		self.if_evaded = self.evade_chance <= self.evasion_rate

	def attack(self):
		self.display_monster()
		print(f"{self.name} dealt {self.dmg} dmg!")
		

	def display_monster(self):
		hp = self.hp  # Current HP as an integer (percentage)
		max_hp_bar_length = 10  # Total number of bars

		hp_perc = hp / self.max_hp

		filled_bars = int(hp_perc * max_hp_bar_length)  # Each bar represents 10%

		# Create the HP bar based on the filled bars
		hp_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))

		print(f"==============================")
		print(f"|{self.name} +{self.amount}| Lv.{self.level}|")
		print(f"==============================")
		print(f"| HP:{self.hp} {hp_bar}|""")
		print(f"==============================")
		print(f"|[1]Attack, [2]Defend, [3]Run|")
		print(f"==============================")


"""Monster List
Grassland : Rabbits, Deers
Forest : Wolfes, Foxes(tameable?)
Deep Forest : Bears, Wraith
Heart Forest : Wraith, Tree Treant

Caves : Spiders(few amounts)
Deep Caves : Spiders(severals), Poisonous Spider(few amounts)
Heart Caves : Spider Queen"""

goblin = Monster("Goblin", 1, 10, 0.50)
rabbit = Monster("Rabbit", 1, 20, 0.40) #1. level, 2. HP, 3.Evasion
deer = Monster("Deer", 5, 40, 0.35)
wolf = Monster("Wolf", 10, 60, 0.30)
fox = Monster("Fox", 15, 80, 0.45)
bear = Monster("Bear", 20, 100, 0.10)
wraith = Monster("Wraith", 25, 120, 0.20)
wraith_2 = Monster("Wraith", 30, 140, 0.40)
tree_treant = Monster("Tree Treant", 50, 200, 0)

spider= EvolvedMonster("Spiders(Few)", 25, 40, random.randint(1,3), 0.30)
spider_2 = EvolvedMonster("Spider(Several)", 30, 40, random.randint(4,7), 0.30)
poison_spider = EvolvedMonster("Poisonous Spiders(Few)", 35, 60, random.randint(1,3), 0.30)
queen_spider = Monster("Spider Queen", 50, 220, 0)


while True:
	queen_spider.attack()
	input()
