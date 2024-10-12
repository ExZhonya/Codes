class Weapon:
    def __init__(self, name):
        self.name = name

weap_1 = Weapon("Wooden Sword")
weap_2 = Weapon("Iron Sword")
weap_3 = Weapon("Steel Sword")
weap_4 = Weapon("Enchanted Sword")

weap_id = (weap_1, weap_2, weap_3, weap_4)

class Armor:
    def __init__(self, name):
        self.name = name

arm_1 = Armor("Leather Armor")
arm_2 = Armor("Iron Armor")
arm_3 = Armor("Steel Armor")
arm_4 = Armor("Enchanted Armor")

arm_id = (arm_1, arm_2, arm_3, arm_4)

class Potion:
    def __init__(self, name):
        self.name = name

id_1 = Potion("HP Potion")
id_2 = Potion("MP Potion")

pot_id = (id_1, id_2)


class chest:
    def show_chest():
        print("="*30)
        print(weap_1) 
        """
        weapons are stored in weap_n, n = id of the weapons, e.g wood sword = 1. weap_1 is wooden sword
        """
        print(arm_2) #same as weapons
        print(id_1) #HP potions are id_1
        print(id_2) #MP potions are id_2
        print("="*30)

