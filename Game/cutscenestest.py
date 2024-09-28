cutscenes = {
	1: 'cutscene_a',
	2: 'cutscene_b'
}

cutscenes_state = {
	1: 'inc',
	2: 'inc'
}

def run_scene(key):
	if cutscenes_state[key] == 'inc':
		cutscene_func = globals()[cutscenes[key]]
		cutscene_func()
		cutscenes_state[key] = 'complete'
		if key + 1 in cutscenes:
			run_scene(key + 1)

#==============================

def cutscene_a():
	print("Running cutscene A...")
	# dialogue
	# actions, etc.
	pass

def cutscene_b():
	print("Running cutscene B...")
	# dialogue
	# actions, etc.
	pass

# Start the first cutscene
run_scene(1)
