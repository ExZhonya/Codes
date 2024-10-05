import welcome as w
import map as m
import cutscenes as c


#w.welc_ascii()
#w.confirm()
#c.spawn()
trigger = False # Added because sometimes the code runs the m.start() before fighting the goblins
if trigger == False:
    from explore_handler import handle_single
    from monster_pick import goblin
    #handle_single(goblin)
    trigger = True
if trigger == True:
    m.start()