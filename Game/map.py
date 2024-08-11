class map:
 def village():
  while True:
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the village")
    print("[1]Home, [2]Shop, [3]Blacksmith [4]Forest")
    print('-'*30)
    choice = input()
    if choice == "1":
        map.home()
    elif choice == "2":
        map.shop()
    elif choice == "3":
        map.blacksmith()
    elif choice == "4":
        map.forest()

 def home():
  while True:
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in your house")
    print("[1]Bed, [2]Chest, [3]Back")
    print('-'*30)
    choice = input()
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        map.village()

 def shop():
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
        map.village()

 def blacksmith():
  while True:
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the blacksmith")
    print("[1]Buy, [2]Enhance, [3]Craft, [4]Exit")
    print('-'*30)
    choice = input()
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        map.village()


 def forest():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Forest")
        print("[1]Village, [2]Cave, [3]Go Deeper")
        print('-'*30)
        choice = input()
        if choice == "1":
            map.village()
        elif choice == "2":
            map.cave()
        elif choice == "3":
            map.deep_forest()

 def cave():
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the Cave")
    print("[1]Go Deeper, [2]Go Back")
    print('-'*30)
    choice = input()
    if choice == "1":
        pass
    elif choice == "2":
        map.forest()

 def deep_forest():
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the Deep Forest")
    print("[1]Go Deeper, [2]Go Back")
    print('-'*30)
    choice = input()
    if choice == "1":
        pass
    elif choice == "2":
        map.forest()

 def grassland():
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the Grassland")
    print("[1]Village [2]Forest, [3]Mountain")
    print('-'*30)
    choice = input()
    if choice == "1":
        map.village()
    elif choice == "2":
        map.forest()
    elif choice == "3":
        pass


while True:
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('-' * 30)
    print('|[1]Village, [2]Grassland, [3]Forest')
    print('-' * 30)
    player = input('where do you want to go?: ')
    if player == "1":
        map.village()
    elif player == "2":
        pass
    elif player == "3":
        map.forest()
