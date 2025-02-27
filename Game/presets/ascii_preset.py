import os, random

#===============BUY MECHANISM==============
import inventory as inv
from player import player as p
from no_input import getch


def show_weapon_to_sell():
    items_to_sell = [inv.wooden_sword, inv.stone_sword, inv.iron_sword]
    weapon_v.weapon(p.gold, items_to_sell[0], items_to_sell[1], items_to_sell[2])
    choice = getch()

#===========================================



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
    def weapon(self, gold, item1, item2, item3):
        os.system("cls;clear")
        print("=" * 30)
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
        print("=" * 30)
        print(
            f"""
You have {gold} gold coins.""")

        print(f"[1]{item1["item"].name}({item1["item"].price})")
        print(f"[2]{item2["item"].name}({item2["item"].price})")
        print(f"[3]{item3["item"].name}({item3["item"].price})")
        print("[`]Back")
        print("-" * 30)
        
class Armors:
    def armor(self):
        os.system("cls;clear")
        print("=" * 30)
        print(
            r"""    _                              
   / \   _ __ _ __ ___   ___  _ __ 
  / _ \ | '__| '_ ` _ \ / _ \| '__|
 / ___ \| |  | | | | | | (_) | |   
/_/   \_\_|  |_| |_| |_|\___/|_|   
"""
        )
        from player import Player
        player = Player()
        gold = player.gold
        print("=" * 30)
        print(
            f"""
You have {gold} gold coins.

[-]Coming Soon
[-]Coming Soon
[-]Coming Soon
    """
        )
        print("[1]Back")
        print("-" * 30)

class Potions:
    def potion(self):
        os.system("cls;clear")
        print("=" * 30)
        print(
            r"""
 ____       _   _                 
|  _ \ ___ | |_(_) ___  _ __  ___ 
| |_) / _ \| __| |/ _ \| '_ \/ __|
|  __/ (_) | |_| | (_) | | | \__ \
|_|   \___/ \__|_|\___/|_| |_|___/
"""
        )
        from player import Player
        player = Player()
        gold = player.self.gold
        print("=" * 30)
        print(
            f"""
You have {gold} gold coins.
            
[-]Coming Soon
[-]Coming Soon
[-]Coming Soon
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

shop_v = Shop()
weapon_v = Weapons()
armor_v = Armors()
potion_v = Potions()
blacksmith_v = Blacksmith()
ec_msg = random_ecounter()