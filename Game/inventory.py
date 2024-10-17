from typing import List, Dict, Tuple
from no_input import getch

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

class Armor(Item):
    def __init__(self, name:str, base_defense:int,  type:str = 'Armor',) -> None:
        super().__init__(name, type)
        self.base_defense = base_defense

    def use(self) -> str:
        return f"Equipped {self.name} (+{self.base_defense})"


class Chest:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.inventory: Dict[int: Dict[str: int]] = {}

    def add(self, item, quantity: int) -> str:
        if len(self.inventory) >= self.capacity:
            return f"Chest is full"
        
        slot = len(self.inventory) + 1

        for existing_slot, item_info in self.inventory.items():
            if item_info['name'] == item.name:
                item_info['quantity'] += quantity
                return f"Added x{quantity} of {item.name} in slot {existing_slot}."
        
        self.inventory[slot] = {'name': item.name, 'quantity': quantity}
        return f"Added {item.name} x{quantity} in slot {slot}."

    def remove(self) -> str:
        print("Select a slot to remove items from:")
        while True:
            try:
                picked_slot = int(getch())  # getch() should return the user's input
                break
            except ValueError:
                print("Please enter a valid number.")
        
        if picked_slot not in self.inventory.keys():
            return f"There is nothing in that slot."
        
        item_info = self.inventory[picked_slot]
        item_name = item_info['name']
        current_quantity = item_info['quantity']
        
        print(f"Enter quantity to remove for {item_name} (max {current_quantity}):")
        while True:
            try:
                remove_quantity = int(getch())  # getch() should capture user input
                break
            except ValueError:
                print("Please enter a valid number.")
        
        if remove_quantity > current_quantity:
            return f"Cannot remove {remove_quantity}, only {current_quantity} available."
        
        self.inventory[picked_slot]['quantity'] -= remove_quantity
        
        if self.inventory[picked_slot]['quantity'] <= 0:
            del self.inventory[picked_slot]
            return f"Removed {item_name} from chest."

        return f"Removed {remove_quantity} of {item_name} from slot {picked_slot}."


    def display(self) -> None:
        print("===Chest===")
        for slot, item_info in self.inventory.items():
            print(f"{slot}: {item_info['name']} x{item_info['quantity']}")
        print("===========")


house_chest: Chest = Chest(10) #10 is the capacity of the chest



# Add new items here.
wooden_sword = Weapon('Wooden Sword', 5)
leather_armor = Armor('Leather Armor', 2)



if __name__ == '__main__':
    print(house_chest.add(wooden_sword, 1))
    print(house_chest.add(leather_armor, 3))
    house_chest.display()
    print(house_chest.remove())
