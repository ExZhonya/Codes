import os
import time
import random

current_monster = None

def hp_bar():
	hp = current_monster.hp  # Current HP as an integer
	max_hp = current_monster.max_hp  # Ensure max_hp is part of current_monster attributes
	max_hp_bar_length = 10  # Total number of bars

	hp_perc = hp / max_hp  # HP as a percentage

	filled_bars = int(hp_perc * max_hp_bar_length)  # Each bar represents 10%

	# Create the HP bar based on the filled bars
	hp_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))
	return hp_bar


def start():
	while current_monster.hp >= 1:
		hp = hp_bar
		os.system("cls;clear")
		print(f"==============================")
		print(f"| {current_monster.name} | Lv. {current_monster.level} |")
		print(f"==============================")
		print(f"| HP: {current_monster.hp}/{current_monster.max_hp} {hp()} |")
		print(f"==============================")
		print(f"| [1] Attack  [2] Defend  [3] Run |")
		print(f"==============================")
		opt = input()
		if opt == '1':
			move_type, dmg = attack()
			enemy_response(move_type, dmg)
		elif opt == '2':
			move_type, dmg = defend()
			enemy_response(move_type, dmg)
		elif opt == '3':
			break
			return
		else:
			continue

def attack():
	move_type = 'attack'
	damage = 10 # Test value
	print(f"You attacked the monster! (Raw dmg: {damage} dmg)")
	time.sleep(1)
	return move_type, damage

def defend():
	move_type = 'defend'
	damage = 0 # Added so the enemy_response function doesn't return an error.
	print(f"You defend the next attack. (+50% dmg reduction on the next attack)")
	time.sleep(1)
	return move_type, damage

def enemy_response(move_type, damage):
	move = random.randint(1,2)
	if move == 1:
		enemy_damage = int(current_monster.dmg)
		if move_type == 'defend':
			enemy_damage //= 2
			print(f"monster attacked for {enemy_damage} dmg!")
			time.sleep(1)
			return
		else:
			current_monster.hp -= int(damage)
			print(f"monster took {damage} dmg!")
			print(f"monster attacked for {enemy_damage} dmg!")
			time.sleep(1)
			return
	else:
		if move_type == 'attack':
			damage = int(damage / 2)
			current_monster.hp -= int(damage)
			print(f"monster defended, and took {damage} dmg!")
			time.sleep(1)
			return
		else:
			print("monster blocked as well.")
			time.sleep(1)
			return

