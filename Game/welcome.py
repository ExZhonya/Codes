import sys
import time

# Cross-platform getch
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

def fast_print(text, delay=0.010):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after finishing

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def welc_ascii():
    import os
    os.system("cls;clear")
    fast_print(r"""
__        _______ _     ____ ___  __  __ _____ _ 
\ \      / / ____| |   / ___/ _ \|  \/  | ____| |
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _| | |
  \ V  V / | |___| |__| |__| |_| | |  | | |___|_|
   \_/\_/  |_____|_____\____\___/|_|  |_|_____(_)
   """)
    time.sleep(0.5)
   

def confirm():
    slow_print("\n Press any key to continue")
    getch()

def test():
    print("Code has completed")

if __name__ == "__main__":
    welc_ascii()
    confirm()
    test()
