import item_assets as item
import inventory_system as inv
# Note: we wanna have NO while loops in the assets files, only in the engine, i'll remove the while loop here in the future, and move it in the main loop of the game
# This is your domain btw, design this however you like :3 Ask me if you want any code changes



'''Displays ONLY'''
def ask_player():
	print("""=========OPTIONS===========""")
	a = input("\nWhat will you do?\n[1]Change Equipment \n[2]Access Inventory \n[3]Use Currently Holding \n[4]Switch Bags(Coming Soon)")
	match a:
		case "1":
			inv.database.select_item()
		case "2":
			inv.database.access_inventory()
		case "3":
			inv.database.h_item_use()
		case "4":
			print("Coming Soon.")

def main_display():
	print("""========EQUIPMENT==========""")
	inv.database.equipt_display()
	print("""========INVENTORY==========""")
	inv.database.show_inventory()
	print("""========HELD-ITEM==========""")
	inv.database.current_hold()
	ask_player()



'''Main Loop(Not really)'''
while True:
	main_display()
	continue
