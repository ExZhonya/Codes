# Creator: @ExZhonya
# Co-Creator: @Pilgrimir
import time
import os
import msvcrt
import sys
""" OUR FILE IMPORT"""
import quest_check as quest
import ascii_preset as ap
import welcome as w

#========PLAYER ENTER GAME SCREEN========
w.welc_ascii()
w.confirm()
from cutscenes import spawn
spawn()
#========================================

#=====================NO INPUT TECHNIQUE===============================
if sys.platform == "win32":
    import msvcrt

    def getch():
        return msvcrt.getch().decode('utf-8')

else:
    import tty
    import termios

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
#=====================================================================

def start():
    while True:
        os.system('cls;clear')
        print("=============")
        print("[1]Village")
        print("=============")
        a = getch()
        if a == '1':
            map1.village()


class preset:
    def area(name, option):
        print("\n" * 40)
        os.system("cls;clear")
        print("-" * 30)
        print(name)
        print(option)
        print("-" * 30)

class map1:
    def village():
        while True:
            preset.area(
                "You're in the Village",
                "[0]Elder, [1]Inn, [2]Shop, [3]Blacksmith, [4]Grassland, [5]City",
            )
            choice = getch()
            if choice == "0":
                map1.vil_quest()
            elif choice == "1":
                map1.vil_inn()
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
            os.system("cls")
            print("-" * 30)
            print(
                "Elder:\nAdventurer! Please help us eradicate monsters destroying our fields.. we will reward you!"
            )
            print("[1]Quests [2]Go Back")
            print("-" * 30)
            choice = getch()
            if choice == "1":
                os.system("cls")
                quest.show()
                quest_choice = int(input("Which quest will you do?\n"))
                quest.update(quest_choice)
                continue
            elif choice == "2":
                map1.village()

    def vil_inn():
        while True:
            preset.area(
                "You're in the Inn",
                "[1]Rest, [2]Chest, [3]Back",
            )
            choice = getch()
            if choice == "1":
                os.system("cls;clear")
                print("-"*30)
                print("Eating... \n")
                time.sleep(3)
                print("Drinking... \n")
                time.sleep(2)
                print("Sleeping... \n")
                print("-"*30)
                time.sleep(5)
                continue
            elif choice == "2":
                pass
            elif choice == "3":
                map1.village()

    def vil_shop():
        while True:
            ap.shop_v.shop()
            choice = getch()
            if choice == "1":
                map1.vil_weap()
            elif choice == "2":
                map1.vil_arm()
            elif choice == "3":
                map1.vil_pot()
            elif choice == "4":
                map1.village()

    def vil_weap():
        ap.weapon_v.weapon()
        choice = getch()
        if choice == "1":
            map1.vil_shop()

    def vil_arm():
        ap.armor_v.armor()
        choice = getch()
        if choice == "1":
            map1.vil_shop()

    def vil_pot():
        ap.potion_v.potion()
        choice = getch()
        if choice == "1":
            map1.vil_shop()

    def blacksmith():
        while True:
            ap.blacksmith_v.blacksmith()
            choice = getch()
            if choice == "1":
                map1.vil_enh()
            elif choice == "2":
                map1.vil_craft()
            elif choice == "3":
                map1.village()

    def vil_enh():
        os.system("cls;clear")
        preset.area(
            "Coming Soon",
            "[1]Back"
        )
        choice = getch()
        if choice == "1":
            map1.blacksmith()

    def vil_craft():
        os.system("cls;clear")
        preset.area(
            "Coming Soon",
            "[1]Back"
        )
        choice = getch()
        if choice == "1":
            map1.blacksmith()

    def forest():
        while True:
            preset.area("You're in Forest", "[1]Explore, [2]Grassland, [3]Cave, [4]Deep Forest")
            choice = getch()
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
            choice = getch()
            if choice == "1":
                pass
            elif choice == "2":
                map1.deep_cave()
            elif choice == "3":
                map1.forest()

    def deep_cave():
        while True:
            preset.area("You're in Deep Cave", "[1]Explore, [2]Go Deeper, [3]Go Back")
            choice = getch()
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                map1.cave()

    def deep_forest():
        while True:
            preset.area("You're in Deep Forest", "[1]Explore, [2]Go Back")
            choice = getch()
            if choice == "1":
                pass
            elif choice == "2":
                map1.forest()

    def grassland():
        while True:
            preset.area("You're in Grassland", "[1]Village [2]Forest,")
            choice = getch()
            if choice == "1":
                map1.village()
            elif choice == "2":
                map1.forest()


class map2:
    def city():
        from cutscenes import city_first
        city_first()
        while True:
            preset.area(
                "You're in City",
                "[0]Guild, [1]Village, [2]Shop, [3]Blacksmith [4]City Sewers, [5]Dark Forest",
            )
            choice = getch()
            if choice == "0":
                guild()
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

    def guild():
        while True:
            preset.area(
                "You're in the Guild",
                "[1]Exit, [2]Receptionist, [3]Quest Board",
            )
            choice = getch()
            if choice == "1":
                map2.city()
            elif choice == "2":
                pass
            elif choice == "3":
                pass

    def city_shop():
        while True:
            ap.shop_v.shop()
            choice = getch()
            if choice == "1":
                map2.city_weap()
            elif choice == "2":
                map2.city_arm()
            elif choice == "3":
                map2.city_pot()
            elif choice == "4":
                map2.city()

    def city_weap():
        ap.weapon_v.weapon()
        choice = getch()
        if choice == "1":
            map2.city_shop()

    def city_arm():
        ap.armor_v.armor()
        choice = getch()
        if choice == "1":
            map2.city_shop()

    def city_pot():
        ap.potion_v.potion()
        choice = getch()
        if choice == "1":
            map2.city_shop()

    def dark_forest():
        while True:
            preset.area("You're in Dark Forest", "[1]City, [2]Deep Dark Forest")
            choice = getch()
            if choice == "1":
                map2.city()
            elif choice == "2":
                map2.deep_dark_forest()

    def deep_dark_forest():
        while True:
            preset.area("You're in Deep Dark Forest", "[1]Go Back [2]??????")
            choice = getch()
            if choice == "1":
                map2.dark_forest()
            elif choice == "2":
                pass


class map3:
    def castle():
        while True:
            preset.area(
                "You're in Castle",
                "[0]Guild, [1]City, [2]Shop, [3]Blacksmith [4]Sewers",
            )
            choice = getch()
            if choice == "0":
                pass  # city guild
            elif choice == "1":
                map2.city()
            elif choice == "2":
                pass

    def sewer():
        while True:
            preset.area("You're in Sewer", "[1]Go Back, [2]Go Deeper")
            choice = getch()
            if choice == "1":
                map3.castle()
            elif choice == "2":
                pass

#==========START========
start()
#=======================
