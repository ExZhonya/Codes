from presets import welcome as w
import map as m
from presets import cutscenes as c
import monster_pick as monster
from handlers.explore_handler import handle_single
#from explore_handler import handle_single

if __name__ == '__main__':
    #w.welc_ascii()
    #w.confirm()
    #c.spawn()

    current_monster = monster.goblin
    handle_single(current_monster)
    m.start()