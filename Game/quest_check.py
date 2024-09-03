# Made by: Pilgrimir
# Co-owner/Intelectual Property: Exzhonya

quests = {
	1: 'Grassland',
	2: 'Forest',
	3: 'Cave'
}

quest_states = {
	1: 'Incomplete',
	2: 'Incomplete',
	3: 'Incomplete'
}

def show_quests(list):
	for key, value in quests.items():
		state = quest_states[key]
		if state == 'Activated':
			print(f"[{key}] {value} (Activated)")
		else:	
			print(f"[{key}] {value}")

def quest_updater(value):
	if value in quests:
		if 'Activated' in quest_states.values():
			print("Please complete the other quest first.")
		else:
			quest_states[value] = 'Activated'
	else:
		print("There's no such quest")
