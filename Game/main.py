import map_ as m
import monster_pick as monster
from no_input import getch
from presets import welcome as w
from presets import cutscenes as c
from explore_handler import handle_single

if __name__ == '__main__':
    #w.welc_ascii()
    #w.confirm()
    #c.spawn()

    while True:
        result = handle_single(monster.goblin)
        if result != 'win':
            print("You had died. Respawn or Skip?[1]Respawn [2]Skip\n")
            match getch():
                case "1": continue
                case "2": result = 'win'
        elif result == 'win': m.start()