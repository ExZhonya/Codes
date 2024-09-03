import time
import sys
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

def fast_print(text, delay=0.010):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after finishing

def forest_scene():
    fast_print(r"""
__        _______ _     ____ ___  __  __ _____ _ 
\ \      / / ____| |   / ___/ _ \|  \/  | ____| |
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _| | |
  \ V  V / | |___| |__| |__| |_| | |  | | |___|_|
   \_/\_/  |_____|_____\____\___/|_|  |_|_____(_)
   """)
    time.sleep(0.5)
   
def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def forest_scene_2():
    slow_print("\n This is a test")
    slow_print("\n Press any key to continue")
    getch()

def test(): #to check if it works
    print("\n\n Code has run sucessfully")
    
forest_scene()
forest_scene_2()
test()