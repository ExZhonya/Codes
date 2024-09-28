import welcome as w
import map as m
import cutscenes as c


w.welc_ascii()
w.confirm()
c.spawn()
from explore_handler import handle_single
from monster_pick import rabbit

handle_single(rabbit)
m.start()