import time
import os
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


#========PROGRESS================
grass_progress= {
	"Rabbit": 4,
	"Deer": 2
}

forest_progress= {
	"Wolf": 0,
	"Fox": 0
}

cave_progress= {
	"Spider": 0
}

#==========PRESETS================

def grass_quest():
	return f"""===============================
Quest:
Kill 5 rabbits ({grass_progress["Rabbit"]}/5)
Kill 3 deers ({grass_progress["Deer"]}/3)
Reward: 10 bronze coins, 30 exp
===============================
"""

def forest_quest():
	return f"""===============================
Quest:
Kill 5 wolves ({forest_progress["Wolf"]}/5)
Kill 5 foxes ({forest_progress["Fox"]}/5)
Reward: 80 bronze coins, 90 exp
===============================
"""

def cave_quest():
	return f"""===============================
Quest:
Kill 15 spiders ({cave_progress["Spider"]}/15)
Reward: 10 silver coins, 300 exp
===============================
"""

#==========STATES==================
quests = {
	1: 'Trouble in the tall grass',
	2: 'Ambush behind the trees',
	3: 'Something lurking on the caves'
}

quest_states = {
	1: 'Pending',
	2: 'Unavailable',
	3: 'Unavailable'
}
#===================================

def quest_handler():
	os.system('cls;clear')
	print("--------Quest:-------")
	for key, value in quests.items():
		state = quest_states[key]
		if state == 'Ongoing':
			print(f"[{key}] {value} (Ongoing)")
		elif state == 'Pending':
			print(f"[{key}] {value}")
		elif state == 'Completed':
			print(f"[{key}] {value} (Completed)")
	print(f"[`]Back")
	print("---------------------")
	print("Which quest would you like to do, Traveler?\n")
	confirm(getch())
	return
	

def confirm(option):
	os.system('cls;clear')
	if option == '1' and quest_states[int(option)] in {'Pending', 'Ongoing'}:
		print(grass_quest())
		match quest_states[int(option)]:
			case 'Pending':
				print("Take quest? [1]Yes [2]No")
			case 'Ongoing':
				print("[1]Submit Quest [2]Back")
		update(getch(), 1)
	elif option == '2' and quest_states[int(option)] in {'Pending', 'Ongoing'}:
		print(forest_quest())
		match quest_states[int(option)]:
			case 'Pending':
				print("Take quest? [1]Yes [2]No")
			case 'Ongoing':
				print("[1]Submit Quest [2]Back")
		update(getch(), 2)
	elif option == '3' and quest_states[int(option)] in {'Pending', 'Ongoing'}:
		print(cave_quest())
		match quest_states[int(option)]:
			case 'Pending':
				print("Take quest? [1]Yes [2]No")
			case 'Ongoing':
				print("[1]Submit Quest [2]Back")
		update(getch(), 3)
	elif option == '`':
		return
	else:
		quest_handler()

			
def update(value, index):
	if value == '1' and 'Pending' in quest_states[index]:
		if 'Ongoing' not in quest_states.values():
			quest_states[index] = 'Ongoing'
			print(f"({quests[index]}) quest added!")
			time.sleep(1)
		else:
			print("Please complete the ongoing quest.")
			time.sleep(1)
	elif value == '1' and 'Ongoing' in quest_states[index]:
		if detect_grassland():
			print("Oh thank you adventurer! Here's what we can give you..")
			time.sleep(1)
			print("Given 10 bronze coins, also gaining an extra 30 exp.")
			time.sleep(1)
			quest_states[index] = 'Completed'
			quest_states[index+1] = 'Pending'
		elif detect_forest():
			print("Oh thank you adventurer! Here's what we can give you..")
			time.sleep(1)
			print("Given 80 bronze coins, also gaining an extra 90 exp.")
			time.sleep(1)
			quest_states[index] = 'Completed'
			quest_states[index+1] = 'Pending'
		elif detect_caves():
			print("Oh thank you adventurer! Here's what we can give you..")
			time.sleep(1)
			print("Given 10 silver coins, also gaining an extra 300 exp.")
			time.sleep(1)
			quest_states[index] = 'Completed'
			quest_states[index+1] = 'Pending'
		else:
			print("Quota not reached yet.")
			return
	elif value == '2':
		return


def detect_grassland():
	if grass_progress['Rabbit'] >= 5 and grass_progress['Deer'] >= 3:
		return True
	
def detect_forest():
	if forest_progress['Wolf'] >= 5 and forest_progress['Fox' ] >= 5:
		return True
	
def detect_caves():
	if cave_progress['Spider'] >= 15:
		return True
