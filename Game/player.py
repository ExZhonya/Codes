class Player:
    def __init__(self, name, hp, mp, strength, defense, level, stat_points=0):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.defense = defense
        self.level = level
        self.stat_points = stat_points

    def display_stats(self):
        print(f"{'='*30}")
        print(f"Character: {self.name}")
        print(f"{'='*30}")
        print(f"{'Stat':<10} | {'Value':<5}")
        print(f"{'-'*30}")
        print(f"{'Health (HP)':<10}| {self.hp:<5}")
        print(f"{'Mana (MP)':<10} | {self.mp:<5}")
        print(f"{'Strength':<10} | {self.strength:<5}")
        print(f"{'Defense':<10} | {self.defense:<5}")
        print(f"{'Level':<10} | {self.level:<5}")
        print(f"Stat Points Available: {self.stat_points}")
        print(f"{'='*30}")

    def level_up(self):
        self.level += 1
        self.stat_points += 5  # Assume player gets 5 points per level up
        print(f"\n*** {self.name} leveled up to Level {self.level} ***")
        print(f"You have earned 5 stat points!")
        self.allocate_stats()

    def allocate_stats(self):
        while self.stat_points > 0:
            self.display_stats()
            print("\nAllocate your stat points:")
            print("[1] Health (HP)")
            print("[2] Mana (MP)")
            print("[3] Strength")
            print("[4] Defense")
            print(f"\nYou have {self.stat_points} points remaining.")

            choice = input("Choose a stat to increase (1-4): ")
            if choice == "1":
                self.hp += 10  
                print("Added 10 HP.")
            elif choice == "2":
                self.mp += 5 
                print("Added 5 MP.")
            elif choice == "3":
                self.strength += 1  
                print("Added 1 Strength.")
            elif choice == "4":
                self.defense += 1  
                print("Added 1 Defense.")
            else:
                print("Invalid choice. Please choose again.")
                continue

            self.stat_points -= 1  # Decrease stat points after allocation

# Create a player character
player = Player(name="Hero", hp=100, mp=50, strength=20, defense=15, level=1)

# Display initial stats
player.display_stats()

# Simulate leveling up
player.level_up()

# Display final stats after allocation
player.display_stats()
