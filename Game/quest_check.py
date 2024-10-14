import time, os, sys
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
quest_dataline = {
	'names': {
		1: 'Trouble in the tall grass',
		2: 'Ambush behind the trees',
		3: 'Something lurking on the caves'
	},
	'states': {
		1: 'Incomplete',
		2: 'Unavailable',
		3: 'Unavailable'
	},
	'progress': {
		1: {1: {'current': 5, 'final': 5}, 2: {'current': 3, 'final': 3}},
		2: {1: {'current': 0, 'final': 5}, 2: {'current': 0, 'final': 5}},
		3: {1: {'current': 0, 'final': 15}}
	}
}

names = quest_dataline['names']
states = quest_dataline['states']
progress = quest_dataline['progress']

grassland = f"""===============================
Quest:
Kill 5 rabbits ({quest_dataline['progress'][1][1]['current']}/{quest_dataline['progress'][1][1]['final']})
Kill 3 deers ({quest_dataline['progress'][1][2]['current']}/{quest_dataline['progress'][1][2]['final']})
Reward: 10 bronze coins, 30 exp
==============================="""

forest = f"""===============================
Quest:
Kill 5 wolves ({quest_dataline['progress'][2][1]['current']}/{quest_dataline['progress'][2][1]['final']})
Kill 5 foxes ({quest_dataline['progress'][2][1]['current']}/{quest_dataline['progress'][2][2]['final']})
Reward: 80 bronze coins, 90 exp
==============================="""

caves = f"""===============================
Quest:
Kill 15 spiders ({quest_dataline['progress'][3][1]['current']}/{quest_dataline['progress'][3][1]['final']})
Reward: 10 silver coins, 300 exp
==============================="""

def quest_handler():
	os.system('cls;clear')
	print("--------Quest:-------")
	for quest, name in names.items():
		if states[quest] == 'Ongoing': print(f'[{quest}] (Ongoing){name}')
		elif states[quest] == 'Unavailable': print(f'[{quest}] {name}')
		elif states[quest] == 'Incomplete': print(f'[{quest}] {name}')
		else: print(f'[{quest}] (Completed){name}')
	print(f"[`]Back")
	print("---------------------")
	print("Which quest would you like to do, Traveler?\n")
	
	option = getch()
	if option == '`': return
	else: confirm(int(option))

def confirm(option):
	os.system('cls;clear')

	process_display(option)
	
	if states[option] == 'Incomplete':
		states[option] = 'Ongoing' if input('Take quest? [1]Yes [2]No ') == '1' else quest_handler()
		print(f'Quest taken: {names[option]}!')
		time.sleep(2)
	elif states[option] == 'Ongoing': submit(option)
	else: 
		print('Quest Unavailable, please complete previous quests first.')
		time.sleep(2)

	quest_handler()

def process_display(option):
	if option == 1:
		print(grassland)
	elif option == 2:
		print(forest)
	elif option == 3:
		print(caves)

def submit(option):
	submittable_quest = 0

	for animal_id, animal_progress in progress[option].items():
		if animal_progress['current'] == animal_progress['final']:
			submittable_quest += 1

	if submittable_quest == len(progress[option]):
		if input('Submit quest? [1]Y [2]N ') == '1':
			states[option] = 'Completed'
			states[option+1] = 'Incomplete'
			print(f'Quest [{names[option]}] Completed!')
			time.sleep(2)
		else:
		 	quest_handler()
	else:
		print('Not enough progress.')
		time.sleep(1)

if __name__ == '__main__':
	quest_handler()