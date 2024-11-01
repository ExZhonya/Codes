import os
import time
from no_input import getch

class Player:
    def __init__(self, name="Player", hp=20, mp=15, strength=1, intelligence=1, defense=1, level=1, stat_points=0, exp=0, exp_needed=300, gold=0):
        self.name = name
        self.hp = hp
        self.max_hp = self.hp
        self.mp = mp
        self.max_mp = self.mp
        self.strength = strength
        self.intelligence = intelligence
        self.defense = defense
        self.level = level
        self.stat_points = stat_points
        self.exp = exp
        self.exp_needed = exp_needed
        self.gold = gold

    def display_stats(self):  # FOR WHILE IN INN/HOUSE
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{'=' * 30}")
        print(f"Character: {self.name}")
        print(f"{'=' * 30}")
        print(f"{'Stat':<10} | {'Value':<5}")
        print(f"{'-' * 30}")
        print(f"{'Health (HP)':<10}| {self.max_hp:<5}")
        print(f"{'Mana (MP)':<10} | {self.max_mp:<5}")
        print(f"{'Strength':<10} | {self.strength:<5}")
        print(f"{'Int':<10} | {self.intelligence:<5}")
        print(f"{'Defense':<10} | {self.defense:<5}")
        print(f"{'Level':<10} | {self.level:<5}")
        print(f"{'Exp':<10} | {self.exp}/{self.exp_needed}")
        print(f"Stat Points Available: {self.stat_points}")
        print(f"{'=' * 30}")
        
        if self.stat_points:
            print("[1] Allocate Stats")
            a = getch()
            if a == "1":
                self.stats_up()
            else:
                self.stats_up()

    def level_up(self):
        if self.exp >= self.exp_needed:
            print(f"Congratulations! You are now level {self.level + 1}")
            time.sleep(3)
            self.level += 1
            self.exp -= self.exp_needed
            self.exp_needed = int(self.exp_needed * 1.2)
            self.exp = 0
            self.stat_points += 2

    def stats_up(self):
        choice_display = """
            Choose a stat to increase:
            [1] HP(+5)
            [2] MP(+5)
            [3] Strength(+1)
            [4] Intelligence(+1)
            [5] Defense(+1)
        """
        
        while self.stat_points > 0:
            print(choice_display)
            x = getch()
            
            if x == "1":
                os.system("cls" if os.name == "nt" else "clear")
                self.max_hp += 5
                print(f"You now have {self.max_hp} Max HP!")
                print(f"[-]Stat Points: {self.stat_points}")
                self.stat_points -= 1
            elif x == "2":
                os.system("cls" if os.name == "nt" else "clear")
                self.max_mp += 5
                print(f"You now have {self.max_mp} Max MP!")
                print(f"[-]Stat Points: {self.stat_points}")
                self.stat_points -= 1
            elif x == "3":
                os.system("cls" if os.name == "nt" else "clear")
                self.strength += 1
                print(f"You now have {self.strength} Strength!")
                print(f"[-]Stat Points: {self.stat_points}")
                self.stat_points -= 1
            elif x == "4":
                os.system("cls" if os.name == "nt" else "clear")
                self.intelligence += 1
                print(f"You now have {self.intelligence} Intelligence!")
                print(f"[-]Stat Points: {self.stat_points}")
                self.stat_points -= 1
            elif x == "5":
                os.system("cls" if os.name == "nt" else "clear")
                self.defense += 1
                print(f"You now have {self.defense} Defense!")
                print(f"[-]Stat Points: {self.stat_points}")
                self.stat_points -= 1
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("Invalid input.")
                print(f"[-]Stat Points: {self.stat_points}")
        
        input("You have no more points left.\nEnter any to continue")
        self.display_stats()

    def get_exp(self, exp):
        self.exp += exp
        print(f"You have received {exp} exp!")
        if self.exp >= self.exp_needed:
            self.level_up()
            self.display_stats()


player = Player()

if __name__ == "__main__":
    player = Player()
    player.stat_points += 2
    player.display_stats()
