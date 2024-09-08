#Original creator: Pilgrimir
#Editor/Co-creator: Lua
#Original creator: Pilgrimir
#Editor/Co-creator: Lua
import random
import time
import sys

if sys.platform == 'win32':
    def clear():
        os.system("cls")
else:
    def clear():
        os.system("clear")


enemy= "Spider" #replaceabe
battlefield= "Suspicious Cave" #replaceable
current_enemy_ap= 10 #temporary
current_enemy_hp= 100 #temporary
current_player_ap= 10 #temporary
current_player_hp= 100 #temporary

def player_input(value): #contains all of the player inputs
    global current_enemy_hp #helps updte the enemy hp var
    global dealt_damage #helps update the player's damage to the enemy
    global player_display #helps update the displayed damage, blocks, dodges, etc.

    if value == "1": 
        dealt_damage= random.randint(1,20) #picks a value from 1-20
        current_enemy_hp = current_enemy_hp - dealt_damage #updates the enemy hp after the damage has been picked
        player_display = f"struck for {dealt_damage} dmg." #displayes the player dmg
    if value == "2":
        return none
    if value == "3":
        return none
    if value == "4":
        return none
    pass

def enemy_input(value): #contains all of the player inputs, uses a random function
    global enemy_display #updates enemy display, like player's
    global dealt_damage_e #updates the damage of the enemy
    global current_player_hp #takes the updated player hp and updates the player's hp too
    global current_enemy_hp #updates the enemy's hp while taking updates from player_input
    if value == 1: #Attack
        dealt_damage_e = random.randint(1,20) #takes a value from 1-20 for the dealt damage, plans to add max and min values
        current_player_hp = current_player_hp - dealt_damage_e #update's the player hp for the final time
        enemy_display = f"struck back for {dealt_damage_e} dmg!" #changes the string value of enemy display
    elif value == 2: #Block
        block_damage_e = random.randint(2,9) #same with dealt_damage_e
        if block_damage_e > dealt_damage: #activates when the blocked damage is below 0
            block_damage_e = dealt_damage #turns the blocked damage same as the dealt_damage by the player, dealing 0 damage
        current_enemy_hp = current_enemy_hp + block_damage_e #updates the enemy hp
        enemy_display = f"blocked {block_damage_e} dmg!" #updates the enemy displayed values 

while True: #clock, and text visuals
    print(f"Area: {battlefield}")
    print(f"-" * 30)
    print(f"|{enemy}")
    print(f"|Health: {current_enemy_hp} Actionpts: {current_enemy_ap}")
    print(f"-" * 30)
    print(f"|Player: ")
    print(f"|Health: {current_player_hp} Actionpts: {current_player_ap}")
    print(f"-" * 30)
    print("[1]- attack [2]- block [3]- dodge [4]- flee")
    next_move= input("Next move: ")
    player_input(next_move) #this is a define function, hard to explain to you
    print(f"Player {player_display}") 
    time.sleep(1) #waits for a second after displaying the player's actions
    enemy_input(2) #generates a random value for their attack, it's set to 2 for now 
    print(f"{enemy} {enemy_display}") #prints the enemy actions
    time.sleep(1) #waits for a second 
    #clears the screen
    continue   #repeats
