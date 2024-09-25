import os
import time
import random
import sys
from player import Player
player = Player()
import monster_pick as m 
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
m.rabbit.spawn()
current_monster = m.rabbit

def enemy_hp_bar():
	hp = current_monster.hp  # Current HP as an integer
	max_hp = current_monster.max_hp  # Ensure max_hp is part of current_monster attributes
	max_hp_bar_length = 10  # Total number of bars

	hp_perc = hp / max_hp  # HP as a percentage

	filled_bars = int(hp_perc * max_hp_bar_length)  # Each bar represents 10%

	# Create the HP bar based on the filled bars
	hp_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))
	return hp_bar

def player_hp_bar():
	hp = player.hp  # Current HP as an integer
	max_hp = player.hp  # Ensure max_hp is part of current_monster attributes
	max_hp_bar_length = 10  # Total number of bars

	hp_perc = hp / max_hp  # HP as a percentage

	filled_bars = int(hp_perc * max_hp_bar_length)  # Each bar represents 10%

	# Create the HP bar based on the filled bars
	hp_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))
	return hp_bar

def start():
	while current_monster.hp >= 1:
		enemy_hp = enemy_hp_bar
		player_hp = player_hp_bar
		print(f"{'='*30}")
		print(f"{'Monster Stats':<10}")
		print(f"{'-'*30}")
		print(f"{'Name':<10}| {current_monster.name}")
		print(f"{'Health':<10}| {enemy_hp()}{current_monster.hp}/{current_monster.max_hp}")
		print(f"{'Level':<10}| {current_monster.level}")
		print(f"{'='*30}")
		print(f"{'Player Stats':<10}")
		print(f"{'-'*30}")
		print(f"{'HP':<10}| {player_hp()}{player.hp}/{player.max_hp}")
		print(f"{'MP':<10}| {player.mp}/{player.max_mp}")
		print(f"{'Level':<10}| {player.level}")
		print(f"{'-'*30}")
		print(f"{'[1]Fight, [2]Defend, [3]Run':<10}")
		print(f"{'='*30}")
		opt = getch()
		match opt:
			case '1': dead = enemy_response(attack())
			case '2': dead = enemy_response(defend())
			case '3': dead = flee()





def attack():
    damage = 100000 # Test value
    print(f"You attacked the {current_monster.name}...")
    time.sleep(1)
    return damage

def defend():
    print(f"You defend the next attack...")
    time.sleep(1)
    return 0

def flee():
    flee_chance = random.random()
    evasion = 0.50
    if flee_chance < evasion:
        print("You successfully escaped!")
        time.sleep(1)
        return True
    else:
        print("You failed to escape.")
        time.sleep(1)
        enemy_response(0)

        
def enemy_response(damage):
    name = current_monster.name

    if damage >= current_monster.hp:
        print("{name} took too much dmg, it cannot fight anymore.")
        time.sleep(1)
        return True
    else:
        print("{name} took {damage} dmg.")
        time.sleep(0.5)

    move = random.randint(1,2)
    if move == 1:
        # attack
        monster_dmg = current_monster.damage // 2
        
        # add a function to alert the player class hp attr
            
        print(f"{name} dealt {monster_dmg} dmg!")
        time.sleep(1)
    else:
        # defend
        if damage != 0:
            current_monster.hp -= damage // 2
            print(f"{name} took {damage // 2} dmg!")
            time.sleep(1)
        else:
            print("Enemy had blocked too.")
            time.sleep(1)

start()