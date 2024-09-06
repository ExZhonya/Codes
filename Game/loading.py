import sys
import time

def print_progress_bar(length, current, bar_length=20):
    """Prints a progress bar to the terminal.
    
    Args:
        length (int): The total length of the task or progress (e.g., 100%).
        current (int): The current progress value.
        bar_length (int): The length of the progress bar in characters.
    """
    # Calculate the percentage completion
    percent = (current / length)
    # Calculate the number of filled blocks
    filled_length = int(bar_length * percent)
    # Create the progress bar string
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    # Print the progress bar
    sys.stdout.write(f'\r[{bar}] {current}/{length}')
    sys.stdout.flush()

def main():
    total_length = 100  # Total length of the task (e.g., 100%)
    for i in range(total_length + 1):
        print_progress_bar(total_length, i)
        time.sleep(0.04)  # Simulate work by sleeping for 0.1 seconds

if __name__ == "__main__":
    main()
