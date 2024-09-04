import sys
import time
import os



# Cutscene based functions-----------------------
cutscenes_state = {
    1: 'Incomplete',
    2: 'Incomplete'
}
display_scene = {
    1: 'Spawn',
    2: 'City'
}

def display_hub(): 
    for key, value in display_scene.items(): # checks the current key and values of the display_scene dictionary
        if cutscenes_state[key] == 'Completed': # checks a different dictionary named cutscenes_state if the current key is 'Completed'
            print(f"[{key}] {value} (Completed)") # if it is, it runs this print
        else:
            print(f"[{key}] {value}") # this is the default print
    run = int(input("Enter the number of the scene you want to continue."))
    run_cutscene(run)


def check(scene_number): # given scene no.
    if scene_number in cutscenes_state: # checks if the given scene no. is in the cutscenes_state dictionary 
        if cutscenes_state[scene_number] == 'Incomplete': # if so, it checks if it's incomplete
            pass # if it is, then it'll continue to the rest of the dialogue
        else:
            next_(scene_number) # if not, it'll skip to the next dialogue.
    else:
        print("Scene does not exist.") # if a next dialogue doesn't exit, this will run. 

def update(scene_number):
    cutscenes_state[scene_number] = 'Completed' # just updates the dictionary to complete once the dialogue has completely finished.

def next_(scene_number):
    if scene_number in cutscenes_state: # checks if the given no. is in the dictionary
        run_cutscene(scene_number + 1) # if it is, then it runs the consecutive/the next scene
    else:
        print("Scene does not exist.") # if the given no. doesn't exist, this shows up

def run_cutscene(next_number):
    match next_number: # this is the backbone of the whole thing, the rest are only checking, and this thing runs and gives meaning to the checking above.
        case 1:
            spawn()
        case 2:
            city_first()
        case _: # this is a default value for match functions.
            unknown_scene() # redirects to a function i made.

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

def unknown_scene():
    os.system("cls;clear")
    slow_print("All cutscenes are completed.")
    time.sleep(1)
    display_hub()

def spawn():
    id_ = 1
    check(id_)
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
    slow_print("One of them says, 'Hello there! Welcome to our village. We need your help. There is a monster in the forest that is terrorizing the villagers. Can you help us defeat it?'\n")
    time.sleep(0.5)
    slow_print("You agree to help and start your journey to defeat the monster.\n")
    update(id_)
    next_(id_)

def city_first():
    id_ = 2
    check(id_)
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
    update(id_)
    next_(id_)



if __name__ == "__main__":
    display_hub() # could be started from the spawn(), no need to use this in the future codes.
