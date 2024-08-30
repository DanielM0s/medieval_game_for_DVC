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
def archer_fight(bow, arrow, enemy):
    while True:
        try:
            if not enemy_dict:
                print("You have defeated all the enemies. Well done!")
                return
            enemies = enemy_dict
            enemy = enemy_dict[enemy["name"]]
            print(f"Enemy distance: {enemy['distance']} Enemy height: {enemy['height']}")
            force = get_valid_force_input("how much force do you want to apply? ")
            length = get_valid_length_input("how far do you pull the string back in cm? ")
            angle = get_valid_angle_input("what angle do you want to shoot the arrow? ")
            distances = [i for i in range(0, int(enemy["distance"]) + 1, 2)]
            heights = [
                calculate_trajectory(force, length, arrow["weight"], angle, dist) for dist in distances
            ]
            plot_results(distances, heights)
            final_height = heights[-1]
            if final_height <= enemy["height"] and final_height > 0:
                print("your arrow hits the enemy")
                damage = force / 5
                print(f"You hit the enemy with {damage} N force.")
                enemy_dict[enemy["name"]]["health"] -= damage
                if enemy_dict[enemy["name"]]["health"] <= 0:
                    print("you killed the enemy")
                    del enemy_dict[enemy["name"]]
                    break
            else:
                print("your arrow misses the enemy")
                if final_height > enemy["height"]:
                    print(f"your arrow flies {abs(final_height - enemy['height'])} m above the enemy")
                elif final_height < 0:
                    print(f"your arrow does not reach the enemy, try aiming higher")
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

def plot_results(distances: List[float], heights: List[float]):
    fig, ax = plt.subplots()

    ax.plot(distances, heights, color='blue', marker='o')
    ax.plot([distances[-1]], [heights[-1]], color='red', marker='o')

    ax.set_xlabel('Distance (m)')
    ax.set_xlim(0, distances[-1])
    ax.set_ylabel('Height (m)')
    ax.set_ylim(0, max(max(heights), heights[-1]))

    ax.grid(True, linestyle='dashed', linewidth=0.5, color='gray', alpha=0.7)

    plt.show()

if learn == "y":
        print("The distance your arrow is dependant on three factors, how much force you apply, how far you pull the string back and the angle at which you fire the bow. Beware, if you apply too much force, or pull the string back too far, you will break the bow and will have to buy a new one. If your bow breaks you will have to use a melee weapon in order to defen yourself from the enemy. the recommended angle to shoot the bow is 45 degrees.")