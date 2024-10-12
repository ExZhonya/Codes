import time, random
from fight_handler import fight
import monster_pick as monster
from quest_check import *


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

			if result == 'win' and repetition < 2:
				print('You moved on to the next monster you saw.')
				time.sleep(1)
				repetition += 1
				continue
			elif result in ('dead', 'fled'):
				return
			else: break

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
	from player import player
	player.strength += 100
	handle(monster.grassland)