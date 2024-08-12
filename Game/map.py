#Creator: @ExZhonya


class map1:
 def village():
  while True:
    print('\n'*40)
    print('-'*30)
    print("You're in the village")
    print("[0]Elder [1]Home, [2]Shop, [3]Blacksmith, [4]Grassland, [5]City")
    print('-'*30)
    choice = input()
    if choice == "0":
    	map1.vil_quest()
    elif choice == "1":
        map1.home()
    elif choice == "2":
        map1.vil_shop()
    elif choice == "3":
        map1.blacksmith()
    elif choice == "4":
        map1.grassland()
    elif choice == "5":
        map2.city()
        
 def vil_quest():
  	while True:
	  	grassland_quest = False
	  	forest_quest = False
	  	cave_quest = False
	  	print('\n\n\n\n\n\n\n\n')
	  	print('-'*30)
	  	print('Adventurer! Please help us eradicate monsters destroying our fields.. we will reward you!')
	  	print('[1]Grassland Quest, [2]Forest Quest, [3]Cave Quest, [4]Go Back')
	  	print('-'*30)
	  	choice = input(' ')
	  	if choice == "1":
	  		print('\n\n\n\n\n\n\n')
	  		print('-'*30)
	  		print('Coming Soon')
	  		print('-'*30)
	  		back = input('[1]Go Back')
	  		print('-'*30)
	  		if back == 1:
	  			map1.vil_quest()
	  		else:
	  			map1.vil_quest()
	  	elif choice == "2":
  			print('\n\n\n\n\n\n\n')
	  		print('-'*30)
	  		print('Coming Soon')
	  		print('-'*30)
	  		back = input('[1]Go Back')
	  		print('-'*30)
	  		if back == 1:
	  			map1.vil_quest()
	  		else:
	  			map1.vil_quest()
 	 	elif choice =="3":
  			print('\n\n\n\n\n\n\n')
	  		print('-'*30)
	  		print('Coming Soon')
	  		print('-'*30)
	  		back = input('[1]Go Back')
	  		print('-'*30)
	  		if back == 1:
	  			map1.vil_quest()
	  		else:
	  			map1.vil_quest()
  		elif choice =="4":
  			map1.village()

 def home():
  while True:
    print('\n'*40)
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

 def vil_shop():
  while True:
    print('\n'*40)
    print('-'*30)
    print("""
 ____  _                 
/ ___|| |__   ___  _ __  
\___ \| '_ \ / _ \| '_ \ 
 ___) | | | | (_) | |_) |
|____/|_| |_|\___/| .__/ 
                  |_|    
				""")
    print("You're in the shop")
    print("[1]Buy, [2]Exit")
    print('-'*30)
    choice = input()
    if choice == "1":
        map1.village_shop()
    elif choice == "2":
        map1.village()

 def village_shop():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the village shop")
        print('[1]Weapons, [2]Armor, [3]Potions, [4]Back')
        print('-'*30)
        choice = input()
        if choice == "1":
            map1.vil_weap()
        elif choice == "2":
            map1.vil_arm()
        elif choice == "3":
            map1.vil_pot()
        elif choice == "4":
            map1.vil_shop()

 def vil_weap():
    print('\n\n\n\n\n')
    print('-'*30)
    print("Coming Soon")
    print('[1]Back')
    print('-'*30)
    choice = input()
    if choice == "1":
        map1.village_shop()

 def vil_arm():
    print('\n\n\n\n\n')
    print('-'*30)
    print("Coming Soon")
    print('[1]Back')
    print('-'*30)
    choice = input()
    if choice == "1":
        map1.village_shop()

 def vil_pot():
    print('\n\n\n\n\n')
    print('-'*30)
    print("Coming Soon")
    print('[1]Back')
    print('-'*30)
    choice = input()
    if choice == "1":
        map1.village_shop()



 def blacksmith():
  while True:
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the blacksmith")
    print("[1]Enhance, [2]Craft, [3]Exit")
    print('-'*30)
    choice = input()
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        map1.village()

 def vil_enh():
    print('\n\n\n\n\n')
    print('-'*30)
    print("Coming Soon")
    print('[1]Back')
    print('-'*30)
    choice = input()
    if choice == "1":
        map1.blacksmith()

 def vil_craft():
    print('\n\n\n\n\n')
    print('-'*30)
    print("Coming Soon")
    print('[1]Back')
    print('-'*30)
    choice = input()
    if choice == "1":
        map1.blacksmith()

 def forest():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Forest")
        print("[1]Explore [2]Grassland, [3]Cave, [4]Go Deeper")
        print('-'*30)
        choice = input()
        if choice == "1":
            pass
        elif choice == "2":
            map1.grassland()
        elif choice == "3":
            map1.cave()
        elif choice == "4":
            map1.deep_forest()

 def cave():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Cave")
        print("[1]Explore, [2]Go Deeper, [3]Go Back")
        print('-'*30)
        choice = input()
        if choice == "1":
            pass
        elif choice == "2":
            map1.deep_cave()
        elif choice == "3":
            map1.forest()

 def deep_cave():
    while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Deep Cave")
        print("[1]Explore, [2]Go Deeper, [3]Go Back")
        print('-'*30)
        choice = input()
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
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
        print("[0]Guild, [1]Village, [2]Shop, [3]Blacksmith [4]City Sewers, [5]Dark Forest")
        print('-'*30)
        choice = input()
        if choice == "0":
        	pass #will make guild def later
        elif choice == "1":
            map1.village()
        elif choice == "2":
            map2.city_shop()
        elif choice == "3":
           pass
        elif choice == "4":
        	pass
        elif choice == "5":
            map2.dark_forest()
        elif choice == "6":
           map3.castle()

    def city_shop():
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the City Shop")
        print("[1]Buy, [2]Exit")
        print('-'*30)
        choice = input()
        if choice == "1":
            map2.in_city_shop()
        elif choice == "2":
            map2.city()

    def in_city_shop():
        while True:
            print('\n\n\n\n\n')
            print('-'*30)
            print("You're in the City Shop")
            print('[1]Weapons, [2]Armor, [3]Potions, [4]Back')
            print('-'*30)
            choice = input()
            if choice == "1":
                map1.vil_weap()
            elif choice == "2":
                map1.vil_arm()
            elif choice == "3":
                map1.vil_pot()
            elif choice == "4":
                map1.village()

    def city_weap():
            print('\n\n\n\n\n')
            print('-'*30)
            print("Coming Soon")
            print('[1]Back')
            print('-'*30)
            choice = input()
            if choice == "1":
                map1.in_city_shop()

    def city_arm():
            print('\n\n\n\n\n')
            print('-'*30)
            print("Coming Soon")
            print('[1]Back')
            print('-'*30)
            choice = input()
            if choice == "1":
                map1.in_city_shop()

    def city_pot():
            print('\n\n\n\n\n')
            print('-'*30)
            print("Coming Soon")
            print('[1]Back')
            print('-'*30)
            choice = input()
            if choice == "1":
                map1.in_city_shop()

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
               pass

class map3:
    def castle():
        while True:
            print('\n\n\n\n\n')
            print('-'*30)
            print("You're in the Castle")
            print("[0]Guild, [1]City, [2]Shop, [3]Blacksmith, [4]Sewer [5]Cemetery [6]Mountains")
            print('-'*30)
            choice = input()
            if choice == "0":
            	pass #city guild
            elif choice == "1":
                map2.city()
            elif choice == "2":
                pass
            

    def sewer():
     while True:
        print('\n\n\n\n\n')
        print('-'*30)
        print("You're in the Sewer")
        print("[1]Go Back, [2]Go Deeper")
        print('-'*30)
        choice = input()
        if choice == "1":
            map3.castle()
        elif choice == "2":
            pass
    
  
while True:
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('-' * 30)
    print('|[1]Village, [2]Grassland, [3]Forest')
    print('-' * 30)
    player = input('where do you want to go?: ')
    if player == "1":
        map1.village()
    elif player == "2":
        map1.grassland()
    elif player == "3":
       map1.forest()
