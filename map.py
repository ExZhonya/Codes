class map:
 def main_map_village():
  while True:
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the village")
    print("[1]House, [2]Shop, [3]Blacksmith [4]Forest")
    print('-'*30)
    choice = input()
    if choice == "1":
        pass
    elif choice == "2":
        map_shop()
    elif choice == "3":
        map_blacksmith()
    elif choice == "4":
        map_forest()

 def map_house():
  while True:
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the house")
    print("[1]Bed, [2]Chest, [3]Exit")
    print('-'*30)
    choice = input()
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        main_map_village()

 def map_shop():
  while True:
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the shop")
    print("[1]Buy, [2]Sell, [3]Exit")
    print('-'*30)
    choice = input()
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        main_map_village()

 def map_blacksmith():
  while True:
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the blacksmith")
    print("[1]Buy, [2]Sell, [3]Exit")
    print('-'*30)
    choice = input()
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        main_map_village()


 def map_forest():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Forest")
        print("[1]Village, [2]Cave, [3]Deep Forest")
        print('-'*30)
        choice = input()
        if choice == "1":
            main_map_village()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
    
  
while True:
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('-' * 30)
    print('|[1]Village, [2]Forest')
    print('-' * 30)
    player = input('where do you want to go?: ')
    if player == "1":
        main_map_village()
    elif player == "2":
        map_forest()