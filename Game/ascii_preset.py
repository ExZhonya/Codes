import os
import time


class Shop:
    def shop(self):
        os.system("cls;clear")
        print("-" * 30)
        print(
            r"""
 ____  _                 
/ ___|| |__   ___  _ __  
\___ \| '_ \ / _ \| '_ \ 
 ___) | | | | (_) | |_) |
|____/|_| |_|\___/| .__/ 
                |_|    
                """
        )
        print("You're in the shop")
        print("[1]Weapons, [2]Armor, [3]Potions, [4]Back")
        print("-" * 30)


class Weapons:
    def weapon(self):
        os.system("cls;clear")
        print("-" * 30)
        print(
            r"""
__        __                               
\ \      / /__  __ _ _ __   ___  _ __  ___ 
 \ \ /\ / / _ \/ _` | '_ \ / _ \| '_ \/ __|
  \ V  V /  __/ (_| | |_) | (_) | | | \__ \
   \_/\_/ \___|\__,_| .__/ \___/|_| |_|___/
                    |_|                    
                    """
        )
        print(
            """
[1]Coming Soon
[2]Coming Soon
[3]Coming Soon
    """)
        print("[1]Back")
        print("-" * 30)
        
class Armors:
    def armor(self):
        os.system("cls;clear")
        print("-" * 30)
        print(
            r"""    _                              
   / \   _ __ _ __ ___   ___  _ __ 
  / _ \ | '__| '_ ` _ \ / _ \| '__|
 / ___ \| |  | | | | | | (_) | |   
/_/   \_\_|  |_| |_| |_|\___/|_|   
"""
        )
        print(
            """
[1]Coming Soon
[2]Coming Soon
[3]Coming Soon
    """
        )
        print("[1]Back")
        print("-" * 30)

class Potions:
    def potion(self):
        os.system("cls;clear")
        print("-" * 30)
        print(
            r"""
 ____       _   _                 
|  _ \ ___ | |_(_) ___  _ __  ___ 
| |_) / _ \| __| |/ _ \| '_ \/ __|
|  __/ (_) | |_| | (_) | | | \__ \
|_|   \___/ \__|_|\___/|_| |_|___/
"""
        )
        print(
            """
[1]Coming Soon
[2]Coming Soon
[3]Coming Soon
    """
        )
        print("[1]Back")
        print("-" * 30)

class Blacksmith:
    def blacksmith(self):
        os.system("cls;clear")
        print("-" * 30)
        print(r"""
 ____  _            _                  _ _   _     
| __ )| | __ _  ___| | _____ _ __ ___ (_) |_| |__  
|  _ \| |/ _` |/ __| |/ / __| '_ ` _ \| | __| '_ \ 
| |_) | | (_| | (__|   <\__ \ | | | | | | |_| | | |
|____/|_|\__,_|\___|_|\_\___/_| |_| |_|_|\__|_| |_|
              """)
        print("You are in Blacksmith")
        print("[1]Enhance, [2]Craft [3]Back")
        print("-" * 30)

class random_ecounter:
    def vil_msg():
        ecounter = ["You see people walking....", "You see children playing around..."]
        print(random.choice(ecounter))

class secret:
    def secret():
        while True:
            choice = input()
            if choice == "exzhonya and pilgrimir has made this game":
                print("wow! you have found our secret code. contact us in discord to claim reward")
                time.sleep(3)
                break
            else:
                break

class Player:
    def __init__(self, name, hp, mp, strength, defense, level):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.defense = defense
        self.level = level

    def display_stats(self):
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
        print(f"{'='*30}")

#stats and the variable, to activate it just put player.display_stats()
player = Player(name="Hero", hp=100, mp=50, strength=20, defense=15, level=5)

class mob_table():
    def preset():
        hp = 210  # Current HP as an integer (percentage)
        max_hp_bar_length = 21  # Total number of bars

        filled_bars = hp // 10  # Each bar represents 10%

        # Create the HP bar based on the filled bars
        maxHP_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))

        print(f"""
                ==============================
                | Goblin     |  Lv.1         |
                ==============================
                | HP: {maxHP_bar}|
                ==============================
                |[1]Attack, [2]Defend, [3]Run|
                ==============================
                """)

shop_v = Shop()
weapon_v = Weapons()
armor_v = Armors()
potion_v = Potions()
blacksmith_v = Blacksmith()
ec_msg = random_ecounter()





