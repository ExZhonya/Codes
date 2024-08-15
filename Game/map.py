# Creator: @ExZhonya
import time
#import quest


class preset:
    def area(name, option):
        print("\n" * 40)
        print("-" * 30)
        print(name)
        print(option)
        print("-" * 30)

class map1:
    def village():
        while True:
            preset.area(
                "You're in the Village",
                "[0]Elder, [1]Home, [2]Shop, [3]Blacksmith, [4]Grassland, [5]City",
            )
            choice = input()
            if choice == "0":
                map1.vil_quest()
            elif choice == "1":
                map1.home()
            elif choice == "2":
                map1.vil_shop()
            elif choice == "3":
                map1.blacksmith()
            elif choice == "4":
                map1.grassland()
            elif choice == "5":
                map2.city()

    def vil_quest():
        while True:
            print("\n\n\n\n\n\n\n\n")
            print("-" * 30)
            print(
                "Adventurer! Please help us eradicate monsters destroying our fields.. we will reward you!"
            )
            print("[1]Grassland Quest, [2]Forest Quest, [3]Cave Quest, [4]Go Back")
            print("-" * 30)
            choice = input(" ")
            if choice == "1":
                pass
            elif choice == "2":
                print("\n\n\n\n\n\n\n")
                print("-" * 30)
                print("Coming Soon")
                print("-" * 30)
                back = input("[1]Go Back")
                print("-" * 30)
                if back == 1:
                    map1.vil_quest()
                else:
                    map1.vil_quest()
            elif choice == "3":
                print("\n\n\n\n\n\n\n")
                print("-" * 30)
                print("Coming Soon")
                print("-" * 30)
                back = input("[1]Go Back")
                print("-" * 30)
            elif choice == "4":
                map1.village()

    def home():
        while True:
            print("\n" *40)
            print("-" * 30)
            print("You're in your house")
            print("[1]Rest, [2]Chest, [3]Back")
            print("-" * 30)
            choice = input()
            if choice == "1":
                print("\n"*40*40)
                print("-"*30)
                print("Eating... \n")
                time.sleep(3)
                print("Drinking... \n")
                time.sleep(2)
                print("Sleeping... \n")
                time.sleep(5)
                continue
            elif choice == "2":
                pass
            elif choice == "3":
                map1.village()

    def vil_shop():
        while True:
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
            print("[1]Buy, [2]Exit")
            print("-" * 30)
            choice = input()
            if choice == "1":
                map1.village_shop()
            elif choice == "2":
                map1.village()

    def village_shop():
        while True:
            print("\n" * 40)
            print("-" * 30)
            print("You're in the village shop")
            print("\n")
            print("Welcome! Do you need anything?")
            print("[1]Weapons, [2]Armor, [3]Potions, [4]Back")
            print("-" * 30)
            choice = input()
            if choice == "1":
                map1.vil_weap()
            elif choice == "2":
                map1.vil_arm()
            elif choice == "3":
                map1.vil_pot()
            elif choice == "4":
                map1.vil_shop()

    def vil_weap():
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
    """
        )
        print("[1]Back")
        print("-" * 30)
        choice = input()
        if choice == "1":
            map1.village_shop()

    def vil_arm():
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
        choice = input()
        if choice == "1":
            map1.village_shop()

    def vil_pot():
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
        choice = input()
        if choice == "1":
            map1.village_shop()

    def blacksmith():
        while True:
            print("\n\n\n\n\n")
            print("-" * 30)
            print("You're in the blacksmith")
            print("[1]Enhance, [2]Craft, [3]Exit")
            print("-" * 30)
            choice = input()
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                map1.village()

    def vil_enh():
        print("\n\n\n\n\n")
        print("-" * 30)
        print("Coming Soon")
        print("[1]Back")
        print("-" * 30)
        choice = input()
        if choice == "1":
            map1.blacksmith()

    def vil_craft():
        print("\n\n\n\n\n")
        print("-" * 30)
        print("Coming Soon")
        print("[1]Back")
        print("-" * 30)
        choice = input()
        if choice == "1":
            map1.blacksmith()

    def forest():
        while True:
            preset.area("You're in Forest", "[1]Explore, [2]Cave, [3]Deep Forest")
            choice = input()
            if choice == "1":
                pass
            elif choice == "2":
                map1.grassland()
            elif choice == "3":
                map1.cave()
            elif choice == "4":
                map1.deep_forest()

    def cave():
        while True:
            preset.area("You're in Cave", "[1]Explore, [2]Deep Cave, [3]Forest")
            choice = input()
            if choice == "1":
                pass
            elif choice == "2":
                map1.deep_cave()
            elif choice == "3":
                map1.forest()

    def deep_cave():
        while True:
            preset.area("You're in Deep Cave", "[1]Explore, [2]Go Deeper, [3]Go Back")
            choice = input()
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                map1.cave()

    def deep_forest():
        while True:
            preset.area("You're in Deep Forest", "[1]Explore, [2]Go Back")
            choice = input()
            if choice == "1":
                pass
            elif choice == "2":
                map1.forest()

    def grassland():
        while True:
            preset.area("You're in Grassland", "[1]Village [2]Forest,")
            if choice == "1":
                map1.village()
            elif choice == "2":
                map1.forest()


class map2:
    def city():
        while True:
            preset.area(
                "You're in City",
                "[0]Guild, [1]Village, [2]Shop, [3]Blacksmith [4]City Sewers, [5]Dark Forest",
            )
            choice = input()
            if choice == "0":
                pass  # will make guild def later
            elif choice == "1":
                map1.village()
            elif choice == "2":
                map2.city_shop()
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                map2.dark_forest()
            elif choice == "6":
                map3.castle()

    def city_shop():
        while True:
            preset.area(
                "You're in City Shop", "[1]Weapon, [2]Armor, [3]Potion, [4]Back"
            )
            choice = input()
            if choice == "1":
                map1.vil_weap()
            elif choice == "2":
                map1.vil_arm()
            elif choice == "3":
                map1.vil_pot()
            elif choice == "4":
                map1.village()

    def city_weap():
        print("\n\n\n\n\n")
        print("-" * 30)
        print("Coming Soon")
        print("[1]Back")
        print("-" * 30)
        choice = input()
        if choice == "1":
            map1.in_city_shop()

    def city_arm():
        print("\n\n\n\n\n")
        print("-" * 30)
        print("Coming Soon")
        print("[1]Back")
        print("-" * 30)
        choice = input()
        if choice == "1":
            map1.in_city_shop()

    def city_pot():
        print("\n\n\n\n\n")
        print("-" * 30)
        print("Coming Soon")
        print("[1]Back")
        print("-" * 30)
        choice = input()
        if choice == "1":
            map1.in_city_shop()

    def dark_forest():
        while True:
            preset.area("You're in Dark Forest", "[1]City, [2]Deep Dark Forest")
            print("-" * 30)
            choice = input()
            if choice == "1":
                map1.city()
            elif choice == "2":
                map1.deep_dark_forest()

    def deep_dark_forest():
        while True:
            preset.area("You're in Deep Dark Forest", "[1]City, [2]Go Back")
            choice = input()
            if choice == "1":
                map1.dark_forest()
            elif choice == "2":
                pass


class map3:
    def castle():
        while True:
            preset.area(
                "You're in Castle",
                "[0]Guild, [1]City, [2]Shop, [3]Blacksmith [4]Sewers",
            )
            choice = input()
            if choice == "0":
                pass  # city guild
            elif choice == "1":
                map2.city()
            elif choice == "2":
                pass

    def sewer():
        while True:
            preset.area("You're in Sewer", "[1]Go Back, [2]Go Deeper")
            choice = input()
            if choice == "1":
                map3.castle()
            elif choice == "2":
                pass


while True:
    print("\n"*40*40)
    print("-" * 40)
    print("|[1]Village, [2]Grassland, [3]Forest")
    print("-" * 30)
    player = input("where do you want to go?: ")
    if player == "1":
        map1.village()
    elif player == "2":
        map1.grassland()
    elif player == "3":
        map1.forest()
