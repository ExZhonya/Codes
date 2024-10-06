import time, random
from fight_handler import Fight
import monster_pick as monster
from quest_check import *

fight = Fight()


def handle_multiple(location):
	if random.random() < 0.80 and location:
		print("You found a few monsters lying around.")
		time.sleep(1)
		repetition = 0
		while repetition in range(3):
			
			# randomizing their stats based on lvl
			current_monster = monster.randomize(location)

			# actually spawning then
			current_monster.spawn()

			# starting the fight
			can_continue = fight.start(current_monster)

			# updating the quest once the fight is over
			quest_updater(str(current_monster), location) # a function in this file

			if can_continue:
				print('You moved on to the next monster you saw.')
				time.sleep(1)
				repetition += 1
				continue
			else:
				break

		if repetition == 2:
			repetition = 0
			print("There was no more monsters, you left the area.")
			time.sleep(1)
	else:
		print("You found nothing.")
		time.sleep(1)



def handle_single(monster):
	monster.spawn()
	fight.current_monster = monster
	fight.start(monster)
	return

def quest_updater(mon, location):
	if 'Ongoing' in quest_states.values():
		match location:
			case monster.grassland:
				if mon in grass_progress: grass_progress[mon] += 1
			case monster.forest:
				if mon in grass_progress: forest_progress[mon] += 1
			case monster.caves:
				if mon in grass_progress: cave_progress[mon] += 1


if __name__ == '__main__':
	handle_multiple(monster.grassland)