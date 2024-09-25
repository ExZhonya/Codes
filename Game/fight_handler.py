import os, time, random, sys
#=====================NO INPUT TECHNIQUE===============================
if sys.platform == "win32":
    import msvcrt

    def getch():
        return msvcrt.getch().decode('utf-8')

else:
    import tty
    import termios

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
#=====================================================================

import monster_pick as m
m.rabbit.spawn()
current_monster = m.rabbit
from player import Player
player = Player()

global dead
dead = False

def enemy_hp_bar():
    hp = current_monster.hp  # Current HP as an integer
    max_hp = current_monster.max_hp  # Ensure max_hp is part of current_monster attributes
    max_hp_bar_length = 10  # Total number of bars

    hp_perc = hp / max_hp  # HP as a percentage

    filled_bars = int(hp_perc * max_hp_bar_length)  # Each bar represents 10%

    # Create the HP bar based on the filled bars
    hp_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))
    return hp_bar

def player_hp_bar():
    hp = player.hp  # Current HP as an integer
    max_hp = player.max_hp  # Ensure max_hp is part of current_monster attributes
    max_hp_bar_length = 10  # Total number of bars

    hp_perc = hp / max_hp  # HP as a percentage

    filled_bars = int(hp_perc * max_hp_bar_length)  # Each bar represents 10%

    # Create the HP bar based on the filled bars
    hp_bar = "[{}{}]".format('▆' * filled_bars, ' ' * (max_hp_bar_length - filled_bars))
    return hp_bar

def start():
    global dead
    while not dead:
        enemy_hp = enemy_hp_bar
        player_hp = player_hp_bar
        os.system("cls;clear")
        print(f"{'='*30}")
        print(f"{'Monster Stats':<10}")
        print(f"{'-'*30}")
        print(f"{'Name':<10}| {current_monster.name}")
        print(f"{'Health':<10}| {enemy_hp()}{current_monster.hp}/{current_monster.max_hp}")
        print(f"{'Level':<10}| {current_monster.level}")
        print(f"{'='*30}")
        print(f"{'Player Stats':<10}")
        print(f"{'-'*30}")
        print(f"{'HP':<10}| {player_hp()}{player.hp}/{player.max_hp}")
        print(f"{'MP':<10}| {player.mp}/{player.max_mp}")
        print(f"{'Level':<10}| {player.level}")
        print(f"{'-'*30}")
        print(f"{'[1]Fight, [2]Defend, [3]Run':<10}")
        print(f"{'='*30}")
        opt = getch()

        match opt:
            case '1': dead = enemy_response(attack())
            case '2': dead = enemy_response(defend())
            case '3': dead = flee()


def attack():
    damage = int(player.strength // 2)
    print(f"You attacked the {current_monster.name}...")
    time.sleep(1)
    return damage

def defend():
    print(f"You defend the next attack...")
    time.sleep(1)
    return -1

def flee():
    flee_chance = random.random()
    evasion = 0.30
    if flee_chance < evasion:
        print("You successfully escaped!")
        time.sleep(1)
        return True
    else:
        print("You failed to escape.")
        time.sleep(1)
        enemy_response(0)

        
def enemy_response(damage):
    name = current_monster.name

    if damage >= current_monster.hp:
        print(f"{name} took too much dmg, it cannot fight anymore.")
        time.sleep(1)
        return True

    move = random.random()
    print(move)
    if move >= 0.30:
        current_monster.hp -= damage
        print(f"{name} took {damage} dmg!")
        time.sleep(1)

        # attack
        monster_dmg = current_monster.dmg
        if damage < 0:
            monster_dmg = current_monster.dmg // 2
        player.hp -= int(monster_dmg)
        print(f"{name} dealt {monster_dmg} dmg!")
        time.sleep(1)
    elif move <= 0.30:
        # defend
        if damage != 0:
            current_monster.hp -= damage // 2
            print(f"{name} blocked and took {damage // 2} dmg!")
            time.sleep(1)
        else:
            print("Enemy had blocked.")
            time.sleep(1)

start()
