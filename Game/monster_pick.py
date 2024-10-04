import random, time


class Monster:
	def __init__(self, name, attack, defense, base_level, base_hp, evasion_rate, exp):
		self.name = name
		self.damage = attack
		self.defense = defense
		self.base_level = base_level
		self.base_hp = base_hp
		self.evasion_rate = evasion_rate
		self.exp = exp

	def spawn(self):
		# Hp and Level reset
		self.level = self.base_level
		self.hp = self.base_hp

		# Randomizer and Multipliers
		self.level = max(1, self.level + random.randint(-2, 5))
		self.hp = self.hp + (self.level * 2) 
		self.max_hp = self.hp 
		self.dmg = self.max_hp / 2 
		self.evade_chance = random.random()
		self.if_evaded = self.evade_chance <= self.evasion_rate
		self.exp = self.exp * self.level
		return

	def __str__(self):
		return self.name

class EvolvedMonster(Monster):

	def __init__(self, name, level, hp, evasion_rate, exp, amount):
		# Inherit the Monster class initialization
		super().__init__(name, level, hp, evasion_rate, amount)
		self.amount = amount
		self.max_hp = self.hp
		self.exp *= self.amount * self.level 

	def spawn(self):
		# Use parent spawn logic, then modify the hp based on amount
		super().spawn()
		self.hp *= self.amount
		self.max_hp = self.hp
		self.exp *= self.amount * self.level 

	def __str__(self):
		super().__str__()

#Spawn Monster
goblin = Monster("Goblin", 1, 2, 1, 10, 0.50, 300) # 1. Level, 2.Attack, 3.Defense, 4. Hp, 5. Evasion Rate, 6. Exp

# Grassland monsters
rabbit = Monster("Rabbit", 1, 3, 3, 20, 0.40, 100)
deer = Monster("Deer", 5, 5, 5, 40, 0.35, 200)

# Forest monsters
wolf = Monster("Wolf", 10, 7, 7, 60, 0.30, 300)
fox = Monster("Fox", 15, 7, 9, 80, 0.45, 400)

# Deep Forest monsters 
bear = Monster("Bear", 20, 20, 35, 100, 0.10, 500)
wraith = Monster("Wraith", 25, 15, 17, 120, 0.20, 500)

# Forest Heart monsters
wraith_2 = Monster("Wraith", 30, 20, 20, 140, 0.40, 600)
tree_treant = Monster("Tree Treant", 50, 23, 25, 200, 0, 700)

# Caves monsters
spider= EvolvedMonster("Spiders", 25, 40, 0.30, 800, 700,) # 1. Level; 2. Hp; 3. Evasion Rate; 4. Random Spawn amount

# Deep caves monsters
spider_2 = EvolvedMonster("Spider", 30, 40, 0.30, 900, 700, )
poison_spider = EvolvedMonster("Poisonous Spiders", 35, 60, 0.30, 1000, 700, )

# Cave heart monsters
queen_spider = Monster("Spider Queen", 50, 220, 0, 1500)

spawn = [goblin]
grassland = [rabbit, deer]
forest = [wolf, fox]
deep_forest = [bear, wraith]
forest_heart = [wraith_2, tree_treant]
caves = [spider]
caves_deep = [spider_2, poison_spider]
caves_heart = [queen_spider]

def randomize(list_location):
	if len(list_location) == 2:
		rng = random.randint(1,10)
		if rng > 7:
			current_monster = list_location[0]
		elif rng < 7:
			current_monster = list_location[1]
		else:
			current_monster = random.choice(list_location)
	else:
		current_monster = monster_list
	return current_monster
