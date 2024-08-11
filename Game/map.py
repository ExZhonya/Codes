#Creator: @ExZhonya

class map1:
 def village():
  while True:
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the village")
    print("[1]Home, [2]Shop, [3]Blacksmith, [4]Grassland")
    print('-'*30)
    choice = input()
    if choice == "1":
        map1.home()
    elif choice == "2":
        map1.shop()
    elif choice == "3":
        map1.blacksmith()
    elif choice == "4":
        map1.grassland()

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
        map1.village()

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
        map1.village()

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
        map1.village()


 def forest():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Forest")
        print("[1]Grassland, [2]Cave, [3]Go Deeper")
        print('-'*30)
        choice = input()
        if choice == "1":
            map1.grassland()
        elif choice == "2":
            map1.cave()
        elif choice == "3":
            map1.deep_forest()

 def cave():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Cave")
        print("[1]Go Deeper, [2]Go Back")
        print('-'*30)
        choice = input()
        if choice == "1":
            map1.deep_cave()
        elif choice == "2":
            map1.forest()

 def deep_cave():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Deep Cave")
        print("[1]Go Deeper, [2]Go Back")
        print('-'*30)
        choice = input()
        if choice == "1":
            pass
        elif choice == "2":
            map1.cave()
    

 def deep_forest():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Deep Forest")
        print("[1]Go Deeper, [2]Go Back")
        print('-'*30)
        choice = input()
        if choice == "1":
            pass
        elif choice == "2":
            map1.forest()

 def grassland():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Grassland")
        print("[1]Village [2]Forest, [3]Mountain")
        print('-'*30)
        choice = input()
        if choice == "1":
            map1.village()
        elif choice == "2":
            map1.forest()
        elif choice == "3":
            pass

class map2:
    def city():
      while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the City")
        print("[1]Village, [2]Shop, [3]Blacksmith, [4]Dark Forest")
        print('-'*30)
        choice = input()
        if choice == "1":
            map1.village()
        elif choice == "2":
            pass
        elif choice == "3":
           pass
        elif choice == "4":
            map1.dark_forest()
        elif choice == "5":
           map3.castle()

    def dark_forest():
        while True:
            print('\n\n\n\n\n')
            print('-'*30)
            print("You're in the Dark Forest")
            print("[1]City, [3]Go Deeper")
            print('-'*30)
            choice = input()
            if choice == "1":
                map1.city()
            elif choice == "3":
                map1.deep_dark_forest()

    def deep_dark_forest():
        while True:
            print('\n\n\n\n\n')
            print('-'*30)
            print("You're in the Deep Dark Forest")
            print("[1]Go Back, [3]Go Deeper")
            print('-'*30)
            choice = input()
            if choice == "1":
                map1.dark_forest()
            elif choice == "2":

class map3:
    def castle():
        while True:
            print('\n\n\n\n\n')
            print('-'*30)
            print("You're in the Castle")
            print("[1]City, [2]Shop, [3]Blacksmith, [4]Sewer [5]Cemetery [6]Mountains")
            print('-'*30)
            choice = input()
            if choice == "1":
                map2.city()
            elif choice == "2":
                pass
            

    def grassland():
     while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Grassland")
        print("[1]Village [2]Forest")
        print('-'*30)
        choice = input()
        if choice == "1":
            map1.village()
        elif choice == "2":
            map1.forest()
    
  
while True:
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('-' * 30)
    print('|[1]Village, [2]Grassland, [3]Forest')
    print('-' * 30)
    player = input('where do you want to go?: ')
    if player == "1":
        map1.village()
    elif player == "2":
        pass
    elif player == "3":
       pass
