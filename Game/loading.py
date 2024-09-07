import sys
import time
import os

def print_progress_bar(length, current, bar_length=20): #bar length is the bar length, unlike total length
    """Prints a progress bar to the terminal.
        length (int): The total length of the task or progress (e.g., 100%).
        current (int): The current progress value.
        bar_length (int): The length of the progress bar in characters.
    """
    percent = (current / length)
    filled_length = int(bar_length * percent)
    # Create the progress bar string
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    # Print the progress bar
    sys.stdout.write(f'\r[{bar}] {current}/{length}')
    sys.stdout.flush()

def main_explore():
    total_length = 100  #just the bar number
    for i in range(total_length + 1):
        os.system("cls;clear")
        print_progress_bar(total_length, i)
        print("\nExploring...")
        
        time.sleep(0.04)  # print speed

def main():
    total_length = 100  #just the bar number
    for i in range(total_length + 1):
        os.system("cls;clear")
        print_progress_bar(total_length, i)
        print("\nAdventuring...")
        
        time.sleep(0.04)  # print speed

if __name__ == "__main__":
    main_explore()
    main()
