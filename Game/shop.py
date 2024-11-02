import inventory as inv
from player import player as p
from presets import ascii_preset as ap
from no_input import getch


def show_weapon_to_sell():
    items_to_sell = [inv.wooden_sword, inv.stone_sword, inv.iron_sword]
    ap.weapon_v.weapon(p.gold, items_to_sell[0], items_to_sell[1], items_to_sell[2])
    choice = getch()


if __name__ == '__main__':
    show_weapon_to_sell()