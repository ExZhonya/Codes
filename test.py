class map1:
 def __innit__(self):
  pass
 def village(self):
  while True:
    print('\n\n\n\n\n')
    print('-'*30)
    print("You're in the village")
    print("[1]Home, [2]Shop, [3]Blacksmith, [4]Grassland, [5]City")
    print('-'*30)
    choice = input()
    if choice == "1":
        map1.home()
    elif choice == "2":
        map1.vil_shop()
    elif choice == "3":
        map1.blacksmith()
    elif choice == "4":
        map1.grassland()
    elif choice == "5":
        map2.city()

def playeraction():
    Map = map1()
    Map.village()