class Player:
    def __init__(self, name, hp, mp, strength, defense, level):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.defense = defense
        self.level = level

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
        print(f"{'='*30}")

#stats and the variable, to activate it just put player.display_stats()
player = Player(name="Hero", hp=100, mp=50, strength=20, defense=15, level=5)

player.display_stats()