import time, random
from fight_handler import fight
import monster_pick as monster
from quest_check import *


def handle(location):
	if random.random() < 0.80:
		print("You found a few monsters lying around.")
		time.sleep(1)
		for repetition in range(3):
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
			else:
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

def quest_updater(monster, location):
	if 'Ongoing' in quest_states.values():
		match location:
			case monster.grassland:
				if monster in grass_progress: grass_progress[monster] += 1
			case monster.forest:
				if monster in forest_progress: forest_progress[monster] += 1
			case monster.caves:
				if monster in cave_progress: cave_progress[monster] += 1


if __name__ == '__main__':
	from player import player
	player.strength += 100
	handle(monster.grassland)