class Shop:
    def shop(self):
        print("\n" * 40)
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
        print("\n" * 40)
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
        print("\n" * 40)
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
        print("\n" * 40)
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
        print("\n" * 40)
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

shop_v = Shop()
weapon_v = Weapons()
armor_v = Armors()
potion_v = Potions()
blacksmith_v = Blacksmith()
ec_msg = random_ecounter()