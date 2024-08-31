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
        self.distance = stats["distance"]
        self.height = stats["height"]
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
def start_archery():
    # a function to start a fight
    enemy_backup = 0
    enemies = enemy_dict
    stun_time = 0
    enemy_stun_time = 0
    amarrows = 0
    for i in inventory:
        if i.name == "Bow":
            bow = i
    for i in inventory:
        if i.name == "arrow x10":
            arrow = i
            amarrows += 1
    amarrows *= 10    
    guide = input("Would you like to learn how to fight? (y/n) ")
    if guide.lower() == "y":
        print("The distance your arrow is dependant on three factors, how much force you apply, how far you pull the string back and the angle at which you fire the bow. Beware, if you apply too much force, or pull the string back too far, you will break the bow and will have to buy a new one. If your bow breaks you will have to use a melee weapon in order to defen yourself from the enemy. the recommended angle to shoot the bow is 45 degrees.")
    #This while loop will continue to run until the player has defeated all the enemies
    while True:
        if amarrows <= 0:
            print("you have no arrows left")
            while True:
                fight_flight = int(input("would you like to 1. use your melee weapon to fightor 2. run away "))
                if fight_flight == 1:
                    for item in inventory:
                        if item.type == "sword":
                            return False
                        else:
                            print("you need a sword to fight")
                            continue
                if fight_flight == 2:
                    away = random.randint(1, stats_dict["dexterity"])
                    if away >= 1:
                        print("you managed to get away")
                        return False
                    elif away < 1:
                        print("As you try to run away the enemy captures you and kills you")
                        exit()
                else:
                    print("invalid input")
                    continue
        #If the player's health is 0 or less they lose the game
        #If the enemy's health is 0 or less they have been defeated and are removed from the list of enemies
        if Enemy.check_health == False:
            print("the enemy has been defeated, well done")
            enemy_backup += enemy["coins"]
            enemies.pop(Enemy.name)
            break
        #If the enemy's health is not 0 or less then the fight continues
        elif Enemy.check_health == True:
            print("the enemy has not been defeated yet")
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
            target = int(input("Which enemy do you want to attack? "))
            #This if statement will check if the user's input is valid and if it is not then it will print an error message and continue to the next iteration of the loop
            if target < 1 or target > len(enemies):
                print("Invalid input")
                continue
            #This line of code will get the name of the enemy that the user wants to attack and assign it to the variable enemy_name
            enemy_name = list(enemies.keys())[target - 1]
            #This line of code will create a new instance of the Enemy class and assign it to the variable enemy
            enemy = Enemy(enemy_name)
            amarrows -= 1
            print(f"you have {amarrows} arrows left")
            archer_fight(bow, arrow, enemy, amarrows)



def archer_fight(bow, arrow, enemy, am_arrows):
    while True:
        try:
            if not enemy_dict:
                print("You have defeated all the enemies. Well done!")
                return
            enemies = enemy_dict
            print(f"Enemy distance: {enemy.distance} Enemy height: {enemy.height}")
            force = get_valid_force_input("how much force do you want to apply? ")
            length = get_valid_length_input("how far do you pull the string back in cm? ")
            angle = get_valid_angle_input("what angle do you want to shoot the arrow? ")
            distances = [i for i in range(0, int(enemy.distance) + 1, 2)]
            heights = [
                calculate_trajectory(force, length, arrow.weight, angle, dist) for dist in distances
            ]
            plot_results(distances, heights, enemy.distance, enemy.height)
            final_height = heights[-1]
            if final_height <= enemy.height and final_height > 0:
                print("your arrow hits the enemy")
                damage = force / 5
                print(f"You hit the enemy with {damage} N force.")
                enemy_dict[enemy.name]["health"] -= damage
                if enemy_dict[enemy.name]["health"] <= 0:
                    print("you killed the enemy")
                    del enemy_dict[enemy.name]
                    break
            else:
                print("your arrow misses the enemy")
                if final_height > enemy.height:
                    print(f"your arrow flies {abs(final_height - enemy.height):.1f} m above the enemy")
                elif final_height < 0:
                    print(f"your arrow does not reach the enemy, try aiming higher")
            return
        except Exception:
            traceback.print_exc()
            input("press enter to continue")

def get_valid_integer_input(prompt: str, valid_options: List[int] = []) -> int:
    while True:
        user_input = input(prompt)
        try:
            valid_input = int(user_input)
            if valid_options and valid_input not in valid_options:
                raise ValueError
            return valid_input
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

def get_valid_force_input(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        try:
            valid_input = int(user_input)
            if 400 <= valid_input <= 710:
                return valid_input
            else:
                print("Invalid input. Please enter a force between 400 and 710.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_length_input(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        try:
            valid_input = int(user_input)
            if 0 <= valid_input <= 76:
                return valid_input
            else:
                print("Your string snaps, you now need to replace it. Next time don't pull it back too far")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_angle_input(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        try:
            valid_input = int(user_input)
            if 0 <= valid_input <= 360:
                return valid_input
            else:
                print("Invalid input. Please enter an angle between 0 and 360.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_trajectory(force: int, length: int, weight: float, angle: int, distance: float) -> Optional[float]:
    try:
        X = length / 100
        k = force / X
        ep = k / 2 * pow(X, 2)
        vi = 2 * ep / weight
        vi = math.sqrt(vi)
        assert vi is not None, "vi cannot be negative or None"
        vix = vi * math.cos(math.radians(angle))
        viy = vi * math.sin(math.radians(angle))
        t = -vix / -9.8
        d = vix * t
        t = distance / viy
        h = viy * t + -4.9 * pow(t, 2)
        return h
    except Exception:
        return None

def plot_results(distances: List[float], heights: List[float], enemy_distance: float, enemy_height: float):
    fig, ax = plt.subplots()

    ax.plot(distances, heights, color='blue', marker='o')
    ax.plot([distances[-1]], [heights[-1]], color='red', marker='o')
    ax.plot([enemy_distance], [enemy_height], color='black', marker='x')

    ax.set_xlabel('Distance (m)')
    ax.set_xlim(0, distances[-1])
    ax.set_ylabel('Height (m)')
    ax.set_ylim(0, max(max(heights), heights[-1], enemy_height))

    ax.grid(True, linestyle='dashed', linewidth=0.5, color='gray', alpha=0.7)

    plt.show()
