import time
import random
import monster_pick as m
import fight_handler as f

def handle(location):
	rng = random.random()
	chance = 0.75
	if rng <= chance:
		print("You found a few monsters lying about.")
		time.sleep(1)
		repetition = 0
		while repetition in range(3):
			monster = m.randomize(location)
			monster.spawn()
			f.current_monster = monster
			f.start()
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