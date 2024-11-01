import map as m

last_save_point = None

def update_save_point(location):
    global last_save_point
    last_save_point = location

def respawn_player():
    if last_save_point == 1:
        map1.village()
    elif last_save_point == 2:
        map2.city()