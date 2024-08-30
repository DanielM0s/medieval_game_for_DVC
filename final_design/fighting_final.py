import random
# from character_stats import stats_dict
from character_stats import inventory, stats_dict
#from enemy_stats import enemy_list
from enemy_stats import enemy_dict
from enemy_stats import inventory as enemy_inventory
import time
import math
import traceback
from typing import List, Optional
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image, ImageDraw




class character:
    # the character class, which contains the player's stats
    def __init__(self, stats_dict):
        # constructor method, called when an instance of the class is created
        # set the player's name, points, coins, strength, dexterity, constitution, intelligence, and wisdom
        # set the player's health to 3 times their constitution
        # set the player's stunned, poisoned, and disarmed status to False
        self.name = stats_dict["name"]
        self.coins = stats_dict["coins"]
        self.strength = stats_dict["strength"]
        self.dexterity = stats_dict["dexterity"]
        self.constitution = stats_dict["constitution"]
        self.intelligence = stats_dict["intelligence"]
        self.wisdom = stats_dict["wisdom"]
        self.health = stats_dict["constitution"] * 3
        self.stunned = False
        self.poisoned = False
        self.disarmed = False

    def attack(self,force):
        # the player's attack method
        # takes a force parameter
        # if the player is disarmed, print a message and return 0
        # calculate the damage based on the force and the player's sword length
        # subtract the force from the player's strength
        # return the damage
        if self.disarmed:
            print("You are disarmed and cannot attack")
            return 0
        for item in inventory:
            if item.type == "sword":
                damage = int(force * item.length)
                sword = item
                if item.name == "Knobkerrie":
                    damage = int(damage * 2)
                break
        self.strength -= force
        return damage

    def counter_attack(self, force):
        # the player's counter attack method
        # takes a force parameter
        # if the player is disarmed, print a message and return 0
        # calculate the damage based on the force and the player's sword length
        # subtract the damage from the player's strength
        # return the damage
        if self.disarmed:
            print("You are disarmed and cannot counter attack")
            return 0
        for item in inventory:
            if item.type == "sword":
                damage = int(force * item.length)
                break
        self.strength -= force
        return damage
    def check_health(self):
        # the player's check health method
        # checks if the player's health is 0 or less
        # if it is, print a message and exit the program
        # if it is not, return True
        if self.health <= 0:
            print(f"you have been defeated!")
            exit()
        else:
            return True


class Enemy:
    # the enemy class
    # has the following methods:
    #     * __init__: takes a enemy name and sets the enemy's stats
    #     * check_health: checks if the enemy's health is 0 or less and returns False if it is
    #     * attack: takes a force parameter and returns the damage that the enemy will do
    #     * end_turn: sets the enemy's strength to 0
    def __init__(self, enemy_name):
        # takes a enemy name and sets the enemy's stats
        stats = enemy_dict[enemy_name]
        self.name = enemy_name
        self.names = stats["name"]
        self.health = stats["health"]
        self.strength = stats["strength"]
        self.dexterity = stats["dexterity"]
        self.wisdom = stats["wisdom"]
        self.sword = enemy_inventory["Ilkwa"]
        self.xp = stats["xp"]
        self.coins = stats["coins"]
        self.stunned = False
        self.poisoned = False
        self.disarmed = False
    def check_health(self, health):
        # checks if the enemy's health is 0 or less and returns False if it is
        
        if health <= 0:
            del enemy_dict[self.name]
            stats_dict["xp"] += self.xp
            print(f"{self.name} has been defeated!")
            print(f"you have earned {self.coins} coins!")
            stats_dict["coins"] += self.coins
            
            return False
        else:
            return True

    def attack(self, force):
        # takes a force parameter and returns the damage that the enemy will do
        if self.disarmed:
            print(f"{self.name} is disarmed and cannot attack")
            return 0
        damage = force * self.sword["length"]
        enemy_dict[self.name]["strength"] -= force
        return damage

    def end_turn(self):
        # sets the enemy's strength to 0
        self.strength = 0

class Sword:
    def __init__(self, length):
        self.length = length
def attack_menu():
    attack_types = {
        "1": {"name": "Slash", "damage": 1.2, "block": 2, "status_effect": None}, # Slash: a basic attack
        "2": {"name": "Thrust", "damage": 1.5, "block": 1, "status_effect": None}, # Thrust: a powerful attack
        "3": {"name": "Parry", "damage": 0.5, "block": 5, "status_effect": "Counter"}, # Parry: a defensive attack
        "4": {"name": "Riposte", "damage": 1.3, "block": 5, "status_effect": "Stun"}, # Riposte: a counter attack
        "5": {"name": "Feint", "damage": 0.7, "block": 4, "status_effect": "Confuse"}, # Feint: a confusing attack
        "6": {"name": "Guard Break", "damage": 1.0, "block": 3, "status_effect": "Disarm"} # Guard Break: a disarming attack
    }

    # Function to find a random attack type
    import random
    def random_attack(attack_dict):
        return random.choice(list(attack_dict.values()))
    return random_attack(attack_types)

enemy_backup = 0
def fight():
    # a function to start a fight
    enemy_backup = 0
    enemies = enemy_dict
    stun_time = 0
    enemy_stun_time = 0
    #This while loop will continue to run until the player has defeated all the enemies
    while True:
        #If the player's health is 0 or less they lose the game
        if character.check_health == True:
            continue
        #If the enemy's health is 0 or less they have been defeated and are removed from the list of enemies
        if Enemy.check_health == False:
            print("the enemy has been defeated, well done")
            enemy_backup += enemy["coins"]
            enemies.pop(Enemy.name)
            break
        #If the enemy's health is not 0 or less then the fight continues
        elif Enemy.check_health == True:
            print("the enemy has not been defeated yet")
        
        guide = input("Would you like to learn how to fight? (y/n) ")
        if guide.lower() == "y":
            print("Welcome to the Fighting Guide!")
            print("-----------------------------")
            print("In this game, you have multiple different attack types, each with their own strengths and weaknesses.")
            print("Here are the different attack types:")
            print("1. Slash: a basic attack - this is a good attack to use when you want to deal a lot of damage but aren't too worried about accuracy.")
            print("2. Thrust: a powerful attack - this is a good attack to use when you want to deal a lot of damage to a specific part of the enemy.")
            print("3. Parry: a defensive attack - this is a good attack to use when you want to block an enemy's attack and counterattack, but doesn't deal as much damage.")
            print("4. Riposte: a counter attack - this is a good attack to use when you want to counter an enemy's attack, and allows you to stun them.")
            print("5. Feint: a confusing attack - this is a good attack to use when you want to confuse an enemy and make them miss their attack.")
            print("6. Guard Break: a disarming attack - this is a good attack to use when you want to disarm an enemy and make them unable to attack you.")
            print("Remember, the best way to win a fight is to use the right attack type at the right time.")
            print("when you start you will get a choice of wich attack type you want to use. You then type how much force you want to use in Newtons, which is then taken away from your strength, then multiplied by the length of your weapon to find the damage you will deal. 20 Newtons is recommended as the amount of force, because it is enough to deal a good amount of damage, without depleting your strength too much. If you are starting to run low on strength, you can type 2 in the first menu, which then allows you to eat any food you have bought, if you don't have any food you can type 3 and try to escape, if you don't manage to escape you will be killed. Once you have defeated all the enemies it is a good idea to go back to your village(beware you may be attacked again) to replenish your food, by going to the village entrance and typing in the number of your village.")
        #This while loop will continue to run until the player has defeated the current enemy
        while True:
            if stun_time == 1:
                cha.stunned = False
            if cha.stunned == True:
                stun_time += 1
            if cha.disarmed == True:
                try:
                    if cha.strength <= 3:
                        run = input("you don't have enough strength to get your weapon back, would you like to try and run away(type y or n)? ")
                        if run.lower() == "y":
                            away = random.randint(1, cha.dexterity)
                            if away >= 10:
                                print("you managed to get away")
                                return
                            elif away < 10:
                                print("As you try to run away the enemy captures you and kills you")
                                exit()
                        elif run.lower() == "n":
                            print("the enemy easily captures you and kills you")
                            exit()
                        else:
                            print("invalid input")
                            print("please type y or n")
                            continue
                    else:
                        get_weapon = random.randint(1, cha.strength)
                        if get_weapon <= 10:
                            print("you managed to get your weapon back at the cost of 3 strength")
                            cha.strength -= 3
                        else:
                            run = input("you failed to get your weapon back. would you like to try and run away(type y or n)? ")
                            if run.lower() == "y":
                                away = random.randint(1, cha.dexterity)
                                if away >= 10:
                                    print("you managed to get away")
                                    return
                                elif away < 10:
                                    print("As you try to run away the enemy captures you and kills you")
                                    exit()
                            elif run.lower() == "n":
                                print("the enemy easily captures you and kills you")
                                exit()
                            else:
                                print("invalid input")
                                print("please type y or n")
                                continue
                except ValueError:
                    print("you didn't manage to get your weapon back")
            while cha.stunned == False:
            #This try and except block will continue to ask the user for input until they enter a valid input
                try:
                    if cha.disarmed == True:
                        weapon = input("do you want to try and get your weapon back? ")
                        if weapon.lower() == "y":
                            get_weapon = random.randint(1, cha.strength)
                            if get_weapon <= 10:
                                print("you managed to get your weapon back at the cost of 3 strength")
                                cha.strength -= 3
                            else:
                                run = input("you failed to get your weapon back. would you like to try and run away(type y or n)? ")
                                if run.lower() == "y":
                                    away = random.randint(1, cha.dexterity)
                                    if away >= 10:
                                        print("you managed to get away")
                                        return
                                    elif away < 10:
                                        print("As you try to run away the enemy captures you and kills you")
                                        exit()
                                elif run.lower() == "n":
                                    print("the enemy easily captures you and kills you")
                                    exit()
                                else:
                                    print("invalid input")
                                    print("please type y or n")
                                    continue
                    if len(enemies) == 0:
                        print("you have defeated all the enemies")
                        print("well done, onto the next battle")
                        print(f"you have earned {stats_dict['xp']} experience")
                        return                           
                    else:
                        pass
                    do = input("Would you like to: 1. Attack 2. Eat food 3. Run? ")
                    #This for loop will print out the names of all the enemies in the list of enemies and their stats
                    if do.lower() == "1":
                        for i, (name, stats) in enumerate(enemy_dict.items()):
                            print(f"{i+1}. {name}")
                        
                        #This input will ask the user which enemy they want to attack
                        target = int(input("Which enemy do you want to attack? "))
                        #This if statement will check if the user's input is valid and if it is not then it will print an error message and continue to the next iteration of the loop
                        if target < 1 or target > len(enemies):
                            print("Invalid input")
                            continue
                        #This line of code will get the name of the enemy that the user wants to attack and assign it to the variable enemy_name
                        enemy_name = list(enemies.keys())[target - 1]
                        #This line of code will create a new instance of the Enemy class and assign it to the variable enemy
                        enemy = Enemy(enemy_name)

                        #This line of code will get a random number between 8 and the enemy's dexterity and assign it to the variable enemy_chance_of_block
                        enemy_chance_of_block = random.randint(8, enemy.dexterity)
                        #This line of code will get a random number between 10 and the enemy's strength and assign it to the variable enemy_block_amount
                        enemy_block_amount = random.randint(8, enemy.strength)  
                        #This dictionary will contain all the attacks that the player can use and their stats
                        attack_types = {
                        "1": {"name": "Slash", "damage": 1.2, "block": 0.8, "status_effect": None},
                        "2": {"name": "Thrust", "damage": 1.5, "block": 0.5, "status_effect": None},
                        "3": {"name": "Parry", "damage": 0.5, "block": 1.5, "status_effect": "Counter"},
                        "4": {"name": "Riposte", "damage": 1.3, "block": 1.0, "status_effect": "Stun"},
                        "5": {"name": "Feint", "damage": 0.7, "block": 0.7, "status_effect": "Confuse"},
                        "6": {"name": "Guard Break", "damage": 1.0, "block": 0.3, "status_effect": "Disarm"}
                        }
                        #This for loop will print out all the attacks in the dictionary and their stats
                        for att, att_info in attack_types.items():
                            print(att, att_info["name"])
                        #This input will ask the user which attack they want to use
                        while True:
                            try:
                                attack = input("Select an attack: ")
                                attack_info = attack_types[attack]
                                break
                            except KeyError:
                                print("Invalid attack. Please select one from the following:")
                                for key, value in attack_types.items():
                                    print(f"{key}. {value}")
                        
                        #This while loop will continue to ask the user for input until they enter a valid attack
                        while attack not in attack_types:
                            print("Invalid attack. Please select one from the following:")
                            #This for loop will print out all the attacks in the dictionary and their stats
                            for key, value in attack_types.items():
                                print(f"{key}. {value}")
                            attack = input("Select an attack: ")
                        #This input will ask the user how much force they want to hit the enemy with
                        forces = int(input(f"How much force do you want to hit them with? "))
                        #This if statement will check if the player has any strength left
                        if cha.strength <= 0:
                            #This input will ask the user if they want to try and escape
                            if any(item["type"] == "food" for item in inventory):
                                print("You have some food in your inventory. You can eat it to regain health.")
                                for item in inventory:
                                    if item["type"] == "food":
                                        print(item["name"])
                                food_choice = input("Which food do you want to eat? ")
                                for item in inventory:
                                    if item["name"] == food_choice and item["type"] == "food":
                                        cha.health += item["health_increase"]
                                        print(f"You regained {item['health_increase']} health.")
                                        inventory.remove(item)
                                        break
                                else:
                                    print("You don't have that food in your inventory.")
                            else:
                                print("You don't have any food in your inventory.")
                            if cha.strength <= 0:
                                back = input("you have no strength left to fight. Would you like to try and escape? (y/n) ")
                                #This if statement will check if the user wants to try and escape
                                if back == "y":
                                    #This line of code will get a random number between 1 and the player's dexterity and assign it to the variable escape_chance
                                    escape_chance = random.randint(1, cha.dexterity)
                                    #This if statement will check if the escape chance is greater than 5
                                    if escape_chance > 5:
                                        print("You have escaped")
                                        #This line of code will call the game_loop function from the final_beginning file and pass the player as an argument
                                        return
                                    elif escape_chance <= 5:
                                        print("You have failed to escape")
                                        print("you are captured by the enemy and killed")
                                        exit()
                                elif back == "n":
                                    print("you do not have enough strength to fight the enemy, the enemy kills you")
                                    exit()
                        #This if statement will check if the user's input is invalid
                        #If the user's input for the force is invalid, print an error message and continue to the next iteration of the loop

                        #Call the attack method from the player class and pass the user's input for the force as an argument
                        forces = cha.attack(forces)
                        #Multiply the force by the damage amount from the attack
                        forces = forces * attack_info["damage"]
                        #Get a random number between 1 and 10 and assign it to the variable enemy_chance_of_block
                        if enemy_chance_of_block < 10:
                            #If the enemy's block chance is less than 10, then the enemy will block the attack
                            #If the attack has a status effect, then apply the status effect to the enemy
                            if attack_info["status_effect"] == "Stun":
                                enemy.stunned = True
                            elif attack_info["status_effect"] == "Poison":
                                enemy.poisoned = True
                            elif attack_info["status_effect"] == "Disarm":
                                enemy.disarmed = True
                            #Subtract the force from the enemy's health
                            enemy_dict[enemy_name]["health"] -= forces
                            #Create a string that says the player hit the enemy for the damage amount
                            damage_string = f"You hit {enemy.name} for {forces} damage"
                            #If the enemy's health is greater than 0, then add the enemy's current health to the string
                            if enemy.check_health(enemy_dict[enemy_name]["health"]) == True:
                                damage_string += f", {enemy.name} has {enemy_dict[enemy_name]['health']} health left"
                            #If the enemy's health is 0 or less, then add a message to the string saying that the enemy has been defeated
                            else:
                                damage_string += f", {enemy.name} has been defeated"
                            #Print the string
                            print(damage_string)
                            #If the enemy is stunned, print a message saying that the enemy is stunned
                            if enemy.stunned:
                                print(f"{enemy.name} is stunned")
                            #If the enemy is poisoned, print a message saying that the enemy is poisoned
                            if enemy.poisoned:
                                print(f"{enemy.name} is poisoned")
                            #If the enemy is disarmed, print a message saying that the enemy is disarmed
                            if enemy.disarmed:
                                print(f"{enemy.name} is disarmed")
                            #Continue to the next iteration of the loop
                            continue
                            
                        else:
                            if not enemy.disarmed or not enemy.stunned:
                                # If the enemy's block amount is less than the force of the attack, then the attack gets through
                                # and the enemy takes damage
                                if enemy_block_amount < forces:
                                    # Calculate the damage
                                    damage = forces - enemy_block_amount
                                    # Subtract the damage from the enemy's health
                                    enemy_dict[enemy_name]["health"] -= damage
                                    # If the attack has a status effect, then apply the status effect to the enemy
                                    if attack_info["status_effect"] == "Stun":
                                        enemy.stunned = True
                                    elif attack_info["status_effect"] == "Poison":
                                        enemy.poisoned = True
                                    elif attack_info["status_effect"] == "Disarm":
                                        enemy.disarmed = True
                                    # Create a string that says the player hit the enemy for the damage amount
                                    damage_string = f"You hit {enemy.name} for {damage} damage"
                                    # If the enemy's health is greater than 0, then add the enemy's current health to the string
                                    if enemy.check_health(enemy_dict[enemy_name]["health"]) == True:
                                        damage_string += f", {enemy.name} has {enemy_dict[enemy_name]['health']:.1f} health left"
                                    # If the enemy's health is 0 or less, then add a message to the string saying that the enemy has been defeated
                                    else:
                                        damage_string += f", {enemy.name} has been defeated"
                                    # Print the string
                                    print(damage_string)
                                    # If the enemy is stunned, print a message saying that the enemy is stunned
                                    if enemy.stunned:
                                        print(f"{enemy.name} is stunned")
                                    # If the enemy is poisoned, print a message saying that the enemy is poisoned
                                    if enemy.poisoned:
                                        print(f"{enemy.name} is poisoned")
                                    # If the enemy is disarmed, print a message saying that the enemy is disarmed
                                    if enemy.disarmed:
                                        print(f"{enemy.name} is disarmed")
                                else:
                                    # If the enemy's block amount is greater than or equal to the force of the attack, then the attack is blocked
                                    print(f"{enemy.name} blocks the attack")
                            break
                    elif do.lower() == "2":
                        print("You have the following food items in your inventory:")
                        options = []
                        for i, item in enumerate(inventory):
                            if item.type == "food":
                                print(f"{i+1}. {item.name}")
                                options.append(i+1)
                        eat = int(input("What food do you want to eat? Enter the number: "))
                        if eat in options:
                            item = next((item for item in inventory if inventory.index(item) == eat-1), None)
                            bonus = item.health_increase
                            bonusstr = item.strength_increase
                            print(f"You eat the {item.name} and gain {bonus} health and {bonusstr} strength.")
                            cha.strength += bonusstr
                            cha.health += bonus
                            inventory.remove(item)
                            continue
                    elif do.lower() == "3":
                        roll = random.randint(1,20)
                        if roll + cha.dexterity >= 15:
                            print("You successfully run away.")
                            return
                        else:
                            print("You fail to run away. The enemy captures and kills you.")
                            exit()
                    else:
                        print("Invalid input. Please try again.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            try:
                if enemy_stun_time == 1:
                    enemy.stunned = False
                if enemy.stunned == True:
                    enemy_stun_time += 1
                while enemy.health > 0 and not enemy.stunned and not enemy.disarmed:
                    # Select a random attack for the enemy to do
                    if enemy.disarmed == True:
                        print(f"{enemy.name} is unable to attack")
                        bravery = random.randint(1, enemy.wisdom) 
                        if bravery <= 10:
                            print("The enemy flees from you in terror")
                            enemies.pop(enemy.name)
                            break
                        elif bravery > 10:
                            print("The enemy manages to get his sword back")
                            enemy.disarmed = False
                            enemy_dict[enemy_name]["strength"] -= 10
                    enemy_attack = attack_menu()
                    enemy_force = random.randint(1, enemy.strength)
                    chance_of_block = random.randint(1, cha.constitution)
                    if chance_of_block < 30:
                        # If the enemy's attack is not blocked, then print a message saying the enemy is attacking the player
                        print(f"{enemy.name} starts to attack you with {enemy_attack['name']}")
                        time.sleep(1)
                        # If the enemy's attack has a status effect, then apply the status effect to the player
                        if enemy_attack["status_effect"] == "Stun":
                            cha.stunned = True
                        elif enemy_attack["status_effect"] == "Poison":
                            cha.poisoned = True
                        elif enemy_attack["status_effect"] == "Disarm":
                            cha.disarmed = True
                        enemy_damage = enemy_force * enemy_attack["damage"]
                        # Subtract the damage from the player's health
                        cha.health -= enemy_damage
                        # If the player is disarmed, print a message saying they are disarmed
                        if cha.disarmed:
                            print(f"You are disarmed")
                        # Check if the player is still alive
                        character.check_health
                        if cha.stunned:
                            print("you are still alive but stunned, you won't be able to attack for one turn")
                        
                        # Print a message saying the enemy hit the player for the damage amount
                        print(f"{enemy.name} hits you with {enemy_attack['name']} for {enemy_damage:.2f} damage, you have {cha.health:.2f} health left")
                        # Subtract the damage from the player's health
                        
                        # If the player is stunned, print a message saying they are stunned
                        if cha.stunned:
                            print(f"You are stunned")
                        # If the player is poisoned, print a message saying they are poisoned
                        if cha.poisoned:
                            print(f"You are poisoned")
                        # If the player is disarmed, print a message saying they are disarmed
                        if cha.disarmed:
                            print(f"You are disarmed")
                        # Check if the player is still alive
                        character.check_health
                    else:
                        # If the enemy's attack is blocked, then print a message saying the enemy's attack was blocked
                        # and calculate the amount of damage the player took
                        block_amount = random.randint(1, cha.dexterity)
                        
                        if block_amount < enemy_force:
                            damage = enemy_force * enemy_attack['damage'] - block_amount
                            if damage <= 0:
                                damage = 0
                            if enemy_attack["status_effect"] == "Stun":
                                cha.stunned = True
                            elif enemy_attack["status_effect"] == "Poison":
                                cha.poisoned = True
                            print(f"{enemy.name} starts to attack you with {enemy_attack['name']}")
                            time.sleep(1)
                            print(f"{enemy.name} hits you with {enemy_attack['name']} for {damage} damage, you have {cha.health - damage} health left, and{cha.strength} strength left")
                            cha.health -= damage
                            if cha.stunned:
                                print(f"You are stunned")
                            if cha.poisoned:
                                print(f"You are poisoned")
                            # Check if the player is still alive
                            character.check_health
                        else:
                            print(f"{enemy.name} tries to attack you but you succesfully manage to block him")
                    # After the enemy has finished his turn, go back to the player's turn
                    break

            except ValueError:
                # If the user enters an invalid input, then print an error message and continue to the next iteration
                print("Invalid input")
                continue
# Create a new instance of the character class with the stats dictionary
cha = character(stats_dict)
