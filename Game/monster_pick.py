import random, time


class Monster:
	def __init__(self, name, base_level, attack, defense, base_hp, evasion_rate, exp, gold):
		self.name = name
		self.damage = attack
		self.defense = defense
		self.base_level = base_level
		self.base_hp = base_hp
		self.evasion_rate = evasion_rate
		self.exp = exp
		self.gold = gold

	def spawn(self):
		# Hp and Level reset
		self.level = self.base_level
		self.hp = self.base_hp

		# Randomizer and Multipliers
		random_multiplier = random.randint(-3, 3)
		modified_level = self.level + random_multiplier
		self.level = max(1, modified_level)
		self.hp = self.hp + self.level
		self.max_hp = self.hp 
		self.dmg = self.max_hp / 2
		self.exp = self.exp + self.level
		return

	def __str__(self):
		return self.name

#class EvolvedMonster(Monster):
#    def __init__(self, name, attack, defense, level, hp, evasion_rate, exp, amount):
        # Inherit the Monster class initialization with the correct arguments
#        super().__init__(name, attack, defense, level, hp, evasion_rate, exp, gold)
#        self.amount = amount
#        self.max_hp = self.base_hp
#        self.exp *= self.amount * self.base_level
#        self.gold = gold
        
#    def spawn(self):
        # Use parent spawn logic, then modify the hp based on amount
#        super().spawn()
#        self.hp *= self.amount
#        self.max_hp = self.hp
#        self.exp *= self.amount

#    def __str__(self):
#        return super().__str__()



"""# 1. Level, 2.Attack, 3.Defense, 4. Hp, 5. Evasion Rate, 6. Exp, 7. Gold"""
#Spawn Monster
goblin = Monster("Goblin", 1, 2, 1, 10, 0.50, 301, 5)

# Grassland monsters
rabbit = Monster("Rabbit", 1, 3, 3, 5, 0.40, 100, 2)
deer = Monster("Deer", 5, 5, 5, 10, 0.35, 200, 5)

# Forest monsters
wolf = Monster("Wolf", 10, 7, 7, 30, 0.30, 300, 7)
fox = Monster("Fox", 15, 7, 9, 40, 0.45, 400, 4)

# Deep Forest monsters 
bear = Monster("Bear", 20, 20, 35, 50, 0.10, 500, 9)
wraith = Monster("Wraith", 25, 15, 17, 60, 0.20, 500, 7)

# Forest Heart monsters
wraith_2 = Monster("Wraith", 30, 20, 20, 80, 0.40, 600, 10)
tree_treant = Monster("Tree Treant", 50, 23, 25, 150, 0, 700, 10)

# Caves monsters
#spider = EvolvedMonster("Spiders", 25, 40, 25, 40, 0.30, 800, random.randint(1, 3))  # 1. Level; 2. Hp; 3. Evasion Rate; 4. Random Spawn amount

# Deep caves monsters
#spider_2 = EvolvedMonster("Spiders", 25, 40, 25, 40, 0.30, 800, random.randint(1, 3)) 
#poison_spider = EvolvedMonster("Poisonous Spiders", 25, 40, 25, 40, 0.30, 800, random.randint(1, 3))

# Cave heart monsters
queen_spider = Monster("Spider Queen", 25, 40, 25, 40, 0.30, 800, 16)

# Monster Lists
spawn = [goblin]
grassland = [rabbit, deer]
forest = [wolf, fox]
deep_forest = [bear, wraith]
forest_heart = [wraith_2, tree_treant]
#caves_deep = [spider_2, poison_spider]


def randomize(group):
	weight = [3, 1]
	next_monster = random.choices(group, weights=weight, k=1)
	return next_monster[0]
