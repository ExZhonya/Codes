import welcome as w
import map as m
import cutscenes as c


w.welc_ascii()
w.confirm()
c.spawn()
import explore_handler as explore
import monster_pick as monster
explore.handle(monster.spawn)
m.start()