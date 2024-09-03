hp = 4  # Current HP as an integer (percentage)
max_hp_bar_length = 10  # Total number of bars

# Calculate the number of filled bars based on the current HP, with a minimum of 1 bar if hp > 0
filled_bars = max(1, hp // 10) if hp > 0 else 0

maxHP_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))

print(f"HP: {hp}%")
print(f"HP Bar: {maxHP_bar}")
