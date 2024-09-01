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
    hints = input("would you like to activate hints? (y/n) ")
    #This while loop will continue to run until the player has defeated all the enemies
    while True:
        try:
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
                archer_fight(bow, arrow, enemy, amarrows, hints)

            #Allow the player to eat food to regain health and strength
            elif do.lower() == "2":
                while True:
                    try:
                        options = [item for item in inventory if item.type == "food"]
                        if not options:
                            print("You have no food.")
                            break
                        print("You have the following food items in your inventory:")
                        for i, item in enumerate(options, start=1):
                            print(f"{i}. {item.name}")
                        eat = int(input("What food do you want to eat? Enter the number: "))
                        if eat in range(1, len(options)+1):
                            item = options[eat-1]
                            bonus = item.health_increase
                            bonusstr = item.strength_increase
                            print(f"You eat the {item.name} and gain {bonus} health and {bonusstr} strength.")
                            stats_dict["strength"] += bonusstr
                            stats_dict["health"] += bonus
                            inventory.remove(item)
                            continue
                    except ValueError:
                        print("invalid input")
                        continue
            #Allow the player to run away from the battle
            elif do.lower() == "3":
                #Generate a random number between 1 and 20 and add the player's dexterity to it. If the result is 15 or higher the player successfully runs away.
                roll = random.randint(1,20)
                if roll + stats_dict["dexterity"] >= 15:
                    print("You successfully run away.")
                    return
                else:
                    print("You fail to run away. The enemy captures and kills you.")
                    exit()
            #Allow the player to quit the game
            elif do.lower() == "q":
                print("thanks for playing!")
                exit()
            else:
                print("Invalid input. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue




def archer_fight(bow, arrow, enemy, am_arrows, hints):
    #if the player wants to activate hints, set the hint variable to True
    if hints.lower() == "y":
        hint = True
    else:
        hint = False
    while True:
        try:
            #if there are no more enemies in the dictionary, the player wins
            if not enemy_dict:
                print("You have defeated all the enemies. Well done!")
                return
            #get the dictionary of enemies
            enemies = enemy_dict
            #print the enemy's distance and height
            print(f"Enemy distance: {enemy.distance} Enemy height: {enemy.height}")
            #if the player wants hints, print a hint about the pull force
            if hint:
                print(f"Hint: make sure to keept the pull force between 400 and {bow.max_draw_force}N")
            #ask the player how much force they want to apply, and make sure it is within the valid range
            force = get_valid_force_input("how much force do you want to apply? ", bow.max_draw_force)
            #if the player wants hints, print a hint about the pull distance
            if hint:
                print(f"Hint: the maximum pull distance is {bow.draw_length}cm (don't include units)")
            #ask the player how far they want to pull the string back, and make sure it is within the valid range
            length = get_valid_length_input("how far do you pull the string back in cm? ", bow.draw_length)
            #ask the player what angle they want to shoot the arrow at
            angle = get_valid_angle_input("what angle do you want to shoot the arrow? ")
            #calculate the trajectory of the arrow
            distances = [i for i in range(0, int(enemy.distance) + 1, 2)]
            heights = [
                calculate_trajectory(force, length, arrow.weight, angle, dist) for dist in distances
            ]
            #plot the results
            plot_results(distances, heights, enemy.distance, enemy.height)
            #get the final height of the arrow
            final_height = heights[-1]
            #if the arrow hits the enemy, print a message and apply damage
            if final_height <= enemy.height and final_height > 0:
                print("your arrow hits the enemy")
                damage = force / 5
                print(f"You hit the enemy with {damage} N force.")
                enemy_dict[enemy.name]["health"] -= damage
                #if the enemy has 0 or less health, the player wins
                if enemy_dict[enemy.name]["health"] <= 0:
                    print("you killed the enemy")
                    del enemy_dict[enemy.name]
                    break
            #if the arrow misses the enemy, print a message
            else:
                print("your arrow misses the enemy")
                if final_height > enemy.height:
                    print(f"your arrow flies {abs(final_height - enemy.height):.1f} m above the enemy")
                elif final_height < 0:
                    print(f"your arrow does not reach the enemy, try aiming higher")
            return
        except Exception:
            #if anything goes wrong, print the error and ask the player to press enter to continue
            traceback.print_exc()
            input("press enter to continue")


def get_valid_integer_input(prompt: str, valid_options: List[int] = []) -> int:
    """Prompt the user for an integer input and return it.

    Args:
        prompt (str): The prompt to show to the user.
        valid_options (List[int], optional): The list of valid options. Defaults to []

    Returns:
        int: The validated input.
    """
    while True:  # Loop until the user enters a valid integer
        user_input = input(prompt)  # Ask the user for input
        try:
            valid_input = int(user_input)  # Try to convert the input to an integer
            if valid_options and valid_input not in valid_options:  # If the user has to choose from a list of options
                raise ValueError  # Raise an error if the input is not in the list
            return valid_input  # Return the valid input
        except ValueError:  # If the input is not an integer
            print("Invalid input. Please enter an integer.")  # Print an error message
            continue  # Loop again

def get_valid_force_input(prompt: str, draw_force: int) -> int:
    """Prompt the user for a valid force input and return it.

    Args:
        prompt (str): The prompt to show to the user.
        draw_force (int): The maximum force the bow can handle.

    Returns:
        int: The validated input.
    """
    while True:  # Loop until the user enters a valid force
        user_input = input(prompt)  # Ask the user for input
        try:
            valid_input = int(user_input)  # Try to convert the input to an integer
            if 400 <= valid_input <= draw_force:  # If the input is within the valid range
                return valid_input  # Return the valid input
            else:  # If the input is not within the valid range
                print("Invalid input. Please enter a force between 400 and 710.")  # Print an error message
        except ValueError:  # If the input is not an integer
            print("Invalid input. Please enter an integer.")  # Print an error message

def get_valid_length_input(prompt: str, draw_length: int) -> int:
    while True:  # Loop until the user enters a valid length
        user_input = input(prompt)  # Ask the user for input
        try:
            valid_input = int(user_input)  # Try to convert the input to an integer
            if 0 <= valid_input <= draw_length:  # If the input is within the valid range
                return valid_input  # Return the valid input
            else:  # If the input is not within the valid range
                print("Your string snaps, you now need to replace it. Next time don't pull it back too far")  # Print an error message
        except ValueError:  # If the input is not an integer
            print("Invalid input. Please enter an integer.")  # Print an error message

def get_valid_angle_input(prompt: str) -> int:
    """
    Prompt the user for a valid angle input and return it.

    Args:
        prompt (str): The prompt to show to the user.

    Returns:
        int: The validated input.
    """
    while True:  # Loop until the user enters a valid angle
        user_input = input(prompt)  # Ask the user for input
        try:
            valid_input = int(user_input)  # Try to convert the input to an integer
            if 0 <= valid_input <= 360:  # If the input is within the valid range
                return valid_input  # Return the valid input
            else:  # If the input is not within the valid range
                print("Invalid input. Please enter an angle between 0 and 360.")  # Print an error message
        except ValueError:  # If the input is not an integer
            print("Invalid input. Please enter an integer.")  # Print an error message

def calculate_trajectory(force: int, length: int, weight: float, angle: int, distance: float) -> Optional[float]:
    """
    Calculate the trajectory of the arrow given the force, length, weight, angle, and distance of the arrow.

    Args:
        force (int): The force applied to the arrow.
        length (int): The length of the arrow.
        weight (float): The weight of the arrow.
        angle (int): The angle of the arrow relative to the ground.
        distance (float): The distance the arrow needs to travel.

    Returns:
        Optional[float]: The height of the arrow if it can reach the target, or None if it cannot.
    """
    try:
        X = length / 100  # Calculate the length of the arrow in cm
        k = force / X  # Calculate the force per cm of the arrow
        ep = k / 2 * pow(X, 2)  # Calculate the energy of the arrow
        vi = 2 * ep / weight  # Calculate the initial velocity of the arrow
        vi = math.sqrt(vi)  # Calculate the initial velocity of the arrow
        assert vi is not None, "vi cannot be negative or None"
        vix = vi * math.cos(math.radians(angle))  # Calculate the horizontal velocity of the arrow
        viy = vi * math.sin(math.radians(angle))  # Calculate the vertical velocity of the arrow
        t = -vix / -9.8  # Calculate the time it takes for the arrow to reach its maximum height
        d = vix * t  # Calculate the distance the arrow will travel horizontally
        t = distance / viy  # Calculate the time it takes for the arrow to reach the target
        h = viy * t + -4.9 * pow(t, 2)  # Calculate the height of the arrow
        return h
    except Exception:
        return None
def plot_results(distances: List[float], heights: List[float], enemy_distance: float, enemy_height: float):
    """
    Plot the trajectory of the arrow given the distances and heights of the arrow.

    Args:
        distances (List[float]): The distances the arrow needs to travel.
        heights (List[float]): The heights of the arrow at each distance.
        enemy_distance (float): The distance the arrow needs to travel to reach the enemy.
        enemy_height (float): The height of the enemy.
    """
    fig, ax = plt.subplots()

    # Plot the trajectory of the arrow
    ax.plot(distances, heights, color='blue', marker='o')
    # Plot the final position of the arrow
    ax.plot([distances[-1]], [heights[-1]], color='red', marker='o')
    # Plot the position of the enemy
    ax.plot([enemy_distance], [enemy_height], color='black', marker='x')

    # Set the x-axis label and range
    ax.set_xlabel('Distance (m)')
    ax.set_xlim(0, distances[-1])
    # Set the y-axis label and range
    ax.set_ylabel('Height (m)')
    ax.set_ylim(0, max(max(heights), heights[-1], enemy_height))

    # Set up the grid
    ax.grid(True, linestyle='dashed', linewidth=0.5, color='gray', alpha=0.7)

    # display the graph
    plt.show()

