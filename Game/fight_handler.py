import os
import time
import random
import sys
#=====================NO INPUT TECHNIQUE===============================
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
#=====================================================================

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
		opt = getch()
		if opt == '1':
			move_type, dmg = attack()
			dead = enemy_response(move_type, dmg)
			if dead:
				break
				return
		elif opt == '2':
			move_type, dmg = defend()
			dead = enemy_response(move_type, dmg)
			if dead:
				break
				return
		elif opt == '3':
			eva_chance = random.random()
			evasion = 0.50
			if eva_chance <= evasion:
				print("You successfully escaped!")
				time.sleep(1)
				break
				return
			else:
				print("You failed to escape.")
				time.sleep(1)
				continue
		else:
			continue
	

def attack():
	move_type = 'attack'
	damage = 100000 # Test value
	print(f"You attacked the {current_monster.name}...")
	time.sleep(1)
	return move_type, damage

def defend():
	move_type = 'defend'
	damage = 0 # Added so the enemy_response function doesn't return an error.
	print(f"You defend the next attack...")
	time.sleep(1)
	return move_type, damage

def enemy_response(move_type, damage):
	move = random.randint(1,2)
	if damage >= current_monster.hp:
		print(f"{current_monster} died.")
		time.sleep(1)
		return True
	else:
		if move == 1:
			enemy_damage = int(current_monster.dmg)
			if move_type == 'defend':
				enemy_damage //= 2
				print(f"And {current_monster.name} attacked for {enemy_damage} dmg!")
				time.sleep(1)
				return False
			else:
				current_monster.hp -= int(damage)
				print(f"And {current_monster.name} took {damage} dmg!")
				time.sleep(1)
				print(f"And {current_monster.name} attacked for {enemy_damage} dmg!")
				time.sleep(1)
				return False
		else:
			if move_type == 'attack':
				damage = int(damage / 2)
				current_monster.hp -= int(damage)
				print(f"But {current_monster.name} defended, and took {damage} dmg!")
				time.sleep(1)
				return False
			else:
				print(f"And {current_monster.name} blocked as well.")
				time.sleep(1)
				return False

