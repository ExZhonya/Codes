import time
import random
import monster_pick as m
import fight_handler as f

def handle(location):
	rng = random.random()
	chance = 0.90
	if rng < chance:
		print("You found a few monsters lying about.")
		time.sleep(1)
		repetition = 0
		while repetition in range(3):
			monster = m.randomize(location)
			monster.spawn()
			f.current_monster = monster
			f.start()
			quest_updater(str(monster), location)
			if repetition == 2:
				print('There was no more monsters, you left the area.')
				time.sleep(1)
				repetition = 0 
				break
				return
			else:
				print('You moved on to the next monster you saw.')
				time.sleep(1)
				repetition += 1
				continue
	else:
		print("You found nothing.")
		time.sleep(1)
		return

def quest_updater(monster, location):
	import quest_check as qc
	if 'Ongoing' in qc.quest_states.values():
		if location == m.grassland and monster in qc.grass_progress:
			qc.grass_progress[monster] += 1
			return
		elif location == m.forest and monster in qc.forest_progress:
			qc.grass_progress[monster] += 1
			return
		elif location == m.caves and monster in qc.cave_progress:
			qc.grass_progress[monster] += 1
			return
	else:
		return
	