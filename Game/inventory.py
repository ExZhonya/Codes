from typing import List, Dict
from player import player


class Item:
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    def __str__(self) -> str:
        return f'{self.name} (Type: {self.type})'

class Weapon(Item):
    def __init__(self, name: str, base_attack: int, type:str = 'Weapon', element= None) -> None:
        super().__init__(name, type)
        self.base_attack = base_attack
        self.element = element

    def use(self) -> str:
        return f"Used {self.name} for {self.base_attack}!"
    
    def __str__(self):
        return super().__str__()

class Armor(Item):
    def __init__(self, name:str, base_defense:int,  type:str = 'Armor',) -> None:
        super().__init__(name, type)
        self.base_defense = base_defense

    def use(self) -> str:
        return f"Equipped {self.name} (+{self.base_defense})"
    
    def __str__(self):
        return super().__str__()

class Inventory: 
    def __init__(self, inventory):
        self.chest_items = inventory
    
    def show_chest_items(self):
        print("========== Current Items ===========")
        for item in self.chest_items:
            print(item)
        print("====================================")
    

# Add new items here.
wooden_sword = Weapon('Wooden Sword', 5)
stone_sword = Weapon('Stone Sword', 10)
iron_sword = Weapon('Iron Sword', 20)
tungsten_sword = Weapon('Tungsten Sword', 50)

leather_armor = Armor('Leather Armor', 2)
chainmain_armor = Armor('Chainmail', 10)
steel_armor = Armor('Steel Armor', 25)

inventory = Inventory(player.inventory)

# debugging area
if __name__ == '__main__':
    
    # adds a new item to the player inventory
    player.inventory.append(wooden_sword) 
    player.inventory.append(leather_armor)

    # show chest items
    inventory.show_chest_items()
