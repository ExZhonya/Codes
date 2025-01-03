import inventory as inv
import time
from player import player as p
from presets import ascii_preset as ap
from no_input import getch


def check_price(player_gold, selected_item):

    if player_gold >= selected_item["item"].price:
        selected_item["item"].price = "Bought"
        p.weapon = selected_item["item"]
        print(f"\nYou have purchased {selected_item["item"].name}!")
        print("[-]Back")
        getch()
        return True
    elif player_gold < selected_item.price:
        print("\nYou do not have enough to buy it!")
        time.sleep(1)
        return False

def buy(chosen_index, item_list, player_gold):

    match chosen_index:
        case 1: selected_item = item_list[1]
        case 2: selected_item = item_list[2]
        case 3: selected_item = item_list[3]

    print(f"You wanna buy {selected_item["item"].name}?")
    print("[1]Yes [2]No", end=" ")
    match getch():
        case '1':
            return check_price(player_gold, selected_item)
        case '2':
            selected_item = None
            return False

def show_weapon_to_sell():

    items_to_sell = {1: {"item": inv.wooden_sword,"bought": False},
                     2: {"item": inv.stone_sword,"bought": False},
                     3: {"item": inv.iron_sword,"bought": False}}
    while True:
        ap.weapon_v.weapon(p.gold, items_to_sell[1], items_to_sell[2], items_to_sell[3])
        choice = getch()
        match choice:
            case "1": bought = buy(1, items_to_sell, p.gold)
            case "2": bought = buy(2, items_to_sell, p.gold)
            case "3": bought = buy(3, items_to_sell, p.gold)
            case '`': break
        if bought: break
        else: continue



if __name__ == '__main__':
    p.gold += 1
    show_weapon_to_sell()
    show_weapon_to_sell()