import time
import random
import monster_pick as monster
import fight_handler as fight
import map as m

def handle(location): # encounter
    rng = random.random()
    encounter_chance = 0.80
    if rng < encounter_chance:
        print("You found a few monsters lying about.")
        time.sleep(1)
        repetition = 0
        while repetition in range(3):
            current_monster = monster.randomize(location) # it's this
            current_monster.spawn()
            fight.current_monster = monster
            fight.start()
            quest_updater(str(current_monster), location)
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

def handle_single(monster):
    rng = random.random()
    encounter_chance = 0.80
    if rng < encounter_chance:
        print(f"You found a {monster} lying about.")
        time.sleep(5)
        monster.spawn()
        fight.current_monster = monster
        fight.start()
        print('There was no more monsters, you left the area.')
        time.sleep(1)

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
	