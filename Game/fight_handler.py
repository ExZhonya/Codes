import os

def start(monster):
	hp = monster.hp  # Current HP as an integer
	max_hp = monster.max_hp  # Ensure max_hp is part of monster attributes
	max_hp_bar_length = 10  # Total number of bars

	hp_perc = hp / max_hp  # HP as a percentage

	filled_bars = int(hp_perc * max_hp_bar_length)  # Each bar represents 10%

	# Create the HP bar based on the filled bars
	hp_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))

	while True:
		os.system("cls;clear")
		print(f"==============================")
		print(f"| {monster.name} | Lv. {monster.level} |")
		print(f"==============================")
		print(f"| HP: {hp}/{max_hp} {hp_bar} |")
		print(f"==============================")
		print(f"| [1] Attack  [2] Defend  [3] Run |")
		print(f"==============================")
		opt = input() # Will add the fight feature in the future
		if opt == '3':
			break
		else:
			continue
