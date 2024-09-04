import sys
import time
import os



# Cutscene based functions-----------------------
"""this are just dictionaries for the available cutscenes."""
cutscenes = {
    1: 'Spawn',
    2: 'City'
}
cutscenes_state = {
    1: 'Incomplete',
    2: 'Incomplete'
}

"""this uses a for loop that prints every possible items in the dictionaries mentioned above."""
def cutscenes_show():
    # Can be removed in the future, no need for the player to choose scenes.

    print("----Scenes-----")
    for key, value in cutscenes.items():
        if cutscenes_state[key] == 'Completed':
            print(f"[{key}] {value} (Completed)")
        else:
            print(f"[{key}] {value}")
    print("---------------")
    cutscene_runner()

"""just takes the input of what the scene the player wants, can be removed in the future."""
def cutscene_updater():
    print("Which scene do you wanna visit?\n")
    scene = int(input())
    if scene in cutscenes_state:
        if cutscenes_state[scene] == 'Completed':
            print("Already read scene.")
        else:
            scene_runner(scene)
    else:
        print('scene does not exist.')

"""This is pretty straightforward."""
def cutscene_runner(scene):
    # Can be removed in the future
    if scene == 1:
        spawn()
    elif scene == 2:
        city_first()



# Text based functions-------------------------
def slow_print(text, delay=0.03):
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


# Actual Cutscenes-------------------------------

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
    cutscenes_state[1] = 'Completed'

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
    slow_print("\x1b[3mYou decided to enter, and went to the receptionist.\x1b[23m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Welcome to the guild! is there anything we can help?\033[0m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mYou: I'd like to register as Adventurer.\033[0m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Sure thing! What's your name?\033[0m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3m<You sign in your information>\x1b[23m\n")
    time.sleep(0.5)
    os.system("cls;clear")
    preset_city()
    slow_print(f"\033[1mRin: Congratulations ! you have become an adventurer. you will need to do guild quest to become full fledged adventurer!\033[0m\n")
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
    cutscenes_state[2] = 'Completed'



if __name__ == "__main__":
    while True:
        cutscenes_show()
