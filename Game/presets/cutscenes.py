import sys
import time
import os

# Cutscene based functions-----------------------
cutscenes_state = {
    1: 'Incomplete',
    2: 'Incomplete',
    3: 'Incomplete',
    4: 'Incomplete',
}
display_scene = {
    1: 'Spawn',
    2: 'City',
    3: 'Forest',
    4: 'Cave',
}


def check(scene_number):
    if scene_number in cutscenes_state: 
        if cutscenes_state[scene_number] == 'Incomplete':
            return True
    else:
        print("Scene does not exist.")


def update(scene_number):
    cutscenes_state[scene_number] = 'Completed' 


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
    
def preset_village():
    print(r"""
          ~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '
================================
          """)


# Actual Cutscenes-------------------------------

def spawn():
    id_ = 1
    check(id_)
    os.system("cls;clear")
    slow_print("You woke up in a strange Forest...\n")
    time.sleep(1)
    slow_print("You woke up confused, empty... You don't remember anything.\n")
    time.sleep(1)
    slow_print("Then you suddenly something... Is that a goblin?\n")
    time.sleep(1)
    slow_print("It looked in your way, and starting rushing to attack you!")
    time.sleep(1)
    slow_print("You ready what little guard you have.")
    time.sleep(1)
    update(id_)

def city_first():
    id_ = 2
    if not check(id_):  # If check() returns False, stop the cutscene
        return
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou are in the city of Luterra. You can see the bustling streets and the tall buildings around you.\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou see an enormous building, you think it's a Guild.\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou decided to enter, and went to the receptionist.\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Welcome to the guild! is there anything we can help?\033[0m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mYou: I'd like to register as Adventurer.\033[0m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Sure thing! What's your name?\033[0m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\x1b[3mYou sign in your information...\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print(f"\033[1mRin: Congratulations ! you have become an adventurer. you will need to do guild quest to become full fledged adventurer!\033[0m\n")
    time.sleep(1.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: There are 6 tier, G>F>D>C>B>A. You will need to complete 3 quest to move to the next tier. You can choose your quest from the guild quest board\033[0m\n")
    time.sleep(1.5)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mRin: Here are your Guild Card, stay safe adventurer!\033[0m")
    time.sleep(1)
    os.system("cls;clear")
    preset_city()
    slow_print("\033[1mYou: Thank you!\033[0m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mYou walked back to the streets...\x1b[23m\n")
    time.sleep(1)
    update(id_)


def forest():
    id_ = 3
    if not check(id_):  # If check() returns False, stop the cutscene
        return
    os.system("cls;clear")
    slow_print("\x1b[3mYou are in Heart Forest... It's so dark you can barely see at all.\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mYou wander around trying to find monsters...\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mYou heard a big stomp.. and a munching sound..\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mYou slowly goes to that sound...\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3m...You are terrified, a huge monster is munching down Red Wraith so easily..\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mThey are so hopeless, they are eaten alive.\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mAfter the huge monster done eating, it goes away..\x1b[23m\n")
    time.sleep(1)
    os.system("cls;clear")
    slow_print("\x1b[3mYou are safe for now.\x1b[23m\n")
    time.sleep(1)
    update(id_)

def cave():
    id_ = 4
    if not check(id_):  # If check() returns False, stop the cutscene
        return
    os.system("cls;clear")



if __name__ == "__main__":
    spawn()
    city_first()