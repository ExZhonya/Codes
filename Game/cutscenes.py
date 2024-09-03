import sys
import time
import os

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def preset_city():
    print(r"""
                           _ _.-'`-._ _
                ;.'________'.;
     _________n.[____________].n_________
    |''_''_''_''||==||==||==||''_''_''_''']
    |'''''''''''||..||..||..||'''''''''''|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
    |.. .. .. ..||..||..||..||.. .. .. ..|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
 ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
===============================================
""")

def spawn():
    os.system("cls;clear")
    slow_print("You wake up in a dark room. You can't remember how you got here, but you know you need to find a way out.\n")
    time.sleep(0.5)
    slow_print("You look around and see a door in front of you. You open it and step outside.\n")
    time.sleep(0.5)
    slow_print("You are in a forest. You can see trees all around you and the sun is shining.\n")
    time.sleep(0.5)
    slow_print("You start walking and soon you see a small village in the distance.\n")
    time.sleep(0.5)
    slow_print("You approach the village and see a group of people gathered around a building.\n")
    time.sleep(0.5)
    slow_print("You walk up to them and they turn to you.\n")
    time.sleep(0.5)
    slow_print("One of them says, 'Hello there! Welcome to our village. We need your help. There is a monster in the forest that is terrorizing the villagers. Can you help us defeat it?\n")
    time.sleep(0.5)
    slow_print("You agree to help and start your journey to defeat the monster.\n")

def city_first():
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou are in the city of Luterra. You can see the bustling streets and the tall buildings around you.\x1b[23m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou see an enormous building named 'Guild'\x1b[23m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou decided to enter, and goes to the receptionist\x1b[23m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Welcome to the guild! is there anything we can help?\033[0m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mYou: I'd like to register as Adventurer\033[0m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Sure thing! What's your name?\033[0m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou sign in your information\x1b[23m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Congratulation! you have become adventurer. you will need to do guild quest to become full fledged adventurer!\033[0m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: There are 6 tier, G>F>D>C>B>A. You will need to complete 3 quest to move to the next tier. You can choose your quest from the guild quest board\033[0m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Here are your Guild Card, stay safe adventurer!\033[0m")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mYou: Thank you!\033[0m\n")

if __name__ == "__main__":
    city_first()