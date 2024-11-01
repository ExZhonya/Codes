import map_ as m
from typing import Dict

last_save_point = None

def update_save_point(location):
    global last_save_point
    last_save_point = location

def respawn_player():
    if last_save_point == 1:
        m.map1.village()
    elif last_save_point == 2:
        m.map2.city()