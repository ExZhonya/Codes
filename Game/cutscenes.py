import sys
import time
import os

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


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
    slow_print("One of them says, 'Hello there! Welcome to our village. We need your help. There is a monster in the forest that is terrorizing the villagers. Can you help us defeat it?'\n")
    time.sleep(0.5)
    slow_print("You agree to help and start your journey to defeat the monster.\n")



if __name__ == "__map__":
    spawn()