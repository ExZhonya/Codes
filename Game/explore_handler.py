import time, random
from fight_handler import Fight
import monster_pick as monster
from quest_check import *

fight = Fight()


def handle(location):
	if random.random() < 0.80:
		print("You found a few monsters lying around.")
		time.sleep(1)
		repetition = 0
		while repetition in range(3):
			current_monster = monster.randomize(location)
			current_monster.spawn()
			result = fight.start(current_monster)
			quest_updater(str(current_monster), location)

			if result == 'win':
				print('You moved on to the next monster you saw.')
				time.sleep(1)
				repetition += 1
				continue
			else: break

		if repetition == 2:
			repetition = 0
			print("There was no more monsters, you left the area.")
			fight.reset()
			time.sleep(1)
	else:
		print("You found nothing.")
		time.sleep(1)


def handle_single(monster):
	monster.spawn()
	fight.current_monster = monster
	fight.start(monster)
	fight.reset()
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
	handle(monster.grassland)