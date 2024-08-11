class MapChoice:  # Just ignore this.
    def __init__(self, name, choice1, choice2, choice3, choice4, choice5):
        self.name = name
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4
        self.choice5 = choice5

    def __str__(self):
        return (f"You are in {self.name} \n"
                f"[1]-{self.choice1}, [1]-{self.choice2}, [1]-{self.choice3}, [1]-{self.choice4}, [1]-{self.choice5},")


# This is replaceable
default_choice = MapChoice("Village", "Home", "Shop",
                           "Blacksmith", "Grassland", "City")

choices = default_choice  # Just sets the default choice in the choices
choice_depth = 1  # This indicates how deep are we in the map

while choice_depth == 1:
    print(choices)
    choice = input("Where to go? ")
    match choice:  # A fancier if statement
        case "1":
            choices = MapChoice("your Home", "Bed", "Chest",
                                "Back to Village", "--", "--")
            choice_depth = 2
            break
        case "2":
            choices = MapChoice("the Shop", "Buy", "Sell",
                                "Exit", "--", "--")
            choice_depth = 2
            break
        case "3":
            choices = MapChoice("the Blacksmith's shop", "Weapons",
                                "Armor", "Potions", "Exit", "--")
            choice_depth = 2
            break
        case "4":
            choices = MapChoice("the Blacksmith's Anvil", "Enhance",
                                "Craft", "Exit", "", "")
            choice_depth = 2
            break
    continue

"""Means we're in the deeper layers, so uhh... you'll need to do this for all of the maps, again."""
while choice_depth == 2:
    print("You've reached depth choice 2.")
    print(choices)
    choice = input("Where to next? ")
    match choice:
        case "1":
            choices = MapChoice("your Home", "Bed", "Chest",
                                "Back to Village", "--", "--")
            choice_depth = 3
            break
        case "2":
            choices = MapChoice("the Shop", "Buy", "Sell",
                                "Exit", "--", "--")
            choice_depth = 3
            break
        case "3":
            choices = MapChoice("the Blacksmith's shop", "Weapons",
                                "Armor", "Potions", "Exit", "--")
            choice_depth = 3
            break
        case "4":
            choices = MapChoice("the Blacksmith's Anvil", "Enhance",
                                "Craft", "Exit", "", "")
            choice_depth = 3
            break
    continue
