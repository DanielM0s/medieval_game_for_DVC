import math
import random
import traceback
from typing import List, Optional
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image, ImageDraw
from enemy_stats import enemy_dict
from enemy_stats import inventory as enemy_inventory
from character_stats import inventory, stats_dict

def archer_fight():
    """Allow the user to choose an enemy to fight with an archer."""
    bow_list = [item for item in inventory if item.name == "Bow"]
    arrow_list = [item for item in inventory if item.name == "arrow x10"]
    if not bow_list or not arrow_list:
        print("You need a Bow and an arrow to fight")
        return
    enemies = list(enemy_dict.keys())
    learn = input("Would you like to learn how to use the bow? (y/n) ")
    if learn == "y":
        print("The distance your arrow is dependant on three factors, how much force you apply, how far you pull the string back and the angle at which you fire the bow. Beware, if you apply too much force, or pull the string back too far, you will break the bow and will have to buy a new one. If your bow breaks you will have to use a melee weapon in order to defen yourself from the enemy. the recommended angle to shoot the bow is 45 degrees.")
    elif learn == "n":
        print("Good luck!")
    do = int(input("Would you like to: 1. Attack 2. Eat food 3. Run? "))
    while True:    
        try:
            if do == 1:
                while True:
                    try:
                        print("Choose an enemy to fight:")
                        for i, name in enumerate(enemies):
                            print(f"{i+1}. {name}")
                        
                        #This input will ask the user which enemy they want to attack
                        target = int(input("Which enemy do you want to attack? "))
                        #This if statement will check if the user's input is valid and if it is not then it will print an error message and continue to the next iteration of the loop
                        if target < 1 or target > len(enemies):
                            print("Invalid input")
                            continue
                        #This line of code will get the name of the enemy that the user wants to attack and assign it to the variable enemy_name
                        enemy_name = enemies[target - 1]
                        #This line of code will create a new instance of the Enemy class and assign it to the variable enemy
                        enemy = Enemy(enemy_name)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    for item in inventory:
                        if item.name == "Bow":
                            bow = Bow(item.name, item.length, item.draw_length)
                    for item in inventory:
                        if item.type == "arrow":
                            arrow = Arrow(item.weight)
                    enemy = Enemy(enemy_name)
                    archer = Archer(bow, arrow, enemy)
                    archer.attack()
            elif do == 2:
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
                    stats_dict["strength"] += bonusstr
                    stats_dict["health"] += bonus
                    inventory.remove(item)
                    continue
            elif do == 3:
                roll = random.randint(1,20)
                if roll + stats_dict["dexterity"] >= 15:
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

# Define decorators for user input validation
def validate_positive_integer(func):
    def wrapper(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input, please enter a valid integer")
    return wrapper


def validate_range(min_val, max_val):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            val = func(self, *args, **kwargs)
            if min_val <= val <= max_val:
                return val
            else:
                print(f"Invalid input, please enter a value between {min_val} and {max_val}")
                return wrapper(self, *args, **kwargs)
        return wrapper
    return decorator


# Define classes for bow, arrow, enemy, and archer
class Arrow:
    def __init__(self, weight: float):
        self.weight = weight


class Bow:
    def __init__(self, name: str, max_pull_force: int, max_pull_distance: int):
        self.name = name
        self.max_pull_force = max_pull_force
        self.max_pull_distance = max_pull_distance


class Enemy:
    def __init__(self, enemy_name):
        # takes a enemy name and sets the enemy's stats
        stats = enemy_dict[enemy_name]
        self.name = enemy_name
        self.names = stats["name"]
        self.health = stats["health"]
        self.strength = stats["strength"]
        self.dexterity = stats["dexterity"]
        self.distance = stats["distance"]
        self.height = 2
        self.sword = enemy_inventory["Ilkwa"]
        self.xp = stats["xp"]
    
    def check_health(self, health):
        # checks if the enemy's health is 0 or less and returns False if it is
        if health <= 0:
            del enemy_dict[self.name]
            stats_dict["xp"] += self.xp
            return False
        else:
            return True

        

hint = False
class Archer:
    def __init__(self, bow: Bow, arrow: Arrow, enemy: Enemy):
        self.bow = bow
        self.arrow = arrow
        self.enemy = enemy
        self.strength = stats_dict["strength"]
        self.dexterity = stats_dict["dexterity"]
    # Calculate the safe square root of a number
    def safe_sqrt(self, number: float) -> Optional[float]:
        try:
            return math.sqrt(number) if number >= 0 else None
        except Exception:
            return None

    # Calculate the height of an arrow based on its force, length, weight, angle, and enemy distance
    def safe_calculate(self, force: int, length: int, weight: float, angle: int, ed: float) -> Optional[float]:
        try:
            X = length / 100
            k = force / X
            ep = k / 2 * pow(X, 2)
            vi = 2 * ep / weight
            vi = self.safe_sqrt(vi)
            assert vi is not None, "vi cannot be negative or None"
            vix = vi * math.cos(math.radians(angle))
            viy = vi * math.sin(math.radians(angle))
            t = -vix / -9.8
            d = vix * t
            t = ed / viy
            h = viy * t + -4.9 * pow(t, 2)
            return h
        except Exception:
            return None

    # Plot the results of the arrow's trajectory
    def plot_results(self, distances: List[float], heights: List[float]):
        fig, ax = plt.subplots()

        ax.plot(distances, heights, color='blue', marker='o')
        ax.plot([self.enemy.distance], [self.enemy.height], color='red', marker='o')

        ax.set_xlabel('Distance (m)')
        ax.set_xlim(0, self.enemy.distance)
        ax.set_ylabel('Height (m)')
        ax.set_ylim(0, max(max(heights), self.enemy.height))

        ax.grid(True, linestyle='dashed', linewidth=0.5, color='gray', alpha=0.7)

        plt.show()

    # Attack the enemy
    def attack(self):
        try:
            arrow_amount = sum(1 for item in inventory if item.name == "arrow x10")
            if arrow_amount > 0:
                arrows = arrow_amount * 10
            elif arrow_amount <= 0:
                print("You don't have any arrows.")
                print("please go to the village to buy some arrows")
                return

            while True:
                try:
                    if not enemy_dict:
                        print("You have defeated all the enemies. Well done!")
                        return

                    enemies = enemy_dict
                    enemy = self.enemy
                    print(f"Enemy distance: {enemy.distance} Enemy height: {enemy.height}")
                    if hint == True:
                        print("hint: the pull force is the force that makes the string pull back")
                        if input("would you like another hint? y/n ") == "y":
                            print("hint: the maximum pull force is 710N, and the minimum pull force is 400N")
                    force = self.get_valid_force_input("how much force do you want to apply? ")
                    length = self.get_valid_length_input("how far do you pull the string back in cm? ")
                    angle = self.get_valid_angle_input("what angle do you want to shoot the arrow? ")
                    force = self._get_valid_integer_input("how much force do you want to apply? ")
                    validate_range(400, 710)(force)
                    validate_positive_integer(force)
                    length = self._get_valid_integer_input("how far do you pull the string back in cm? ")
                    validate_range(0, self.bow.max_pull_distance)(length)
                    angle = self._get_valid_integer_input("what angle do you want to shoot the arrow? ")
                    distances = [i for i in range(0, int(enemy.distance) + 1, 2)]
                    heights = [
                        self.safe_calculate(force, length, self.arrow.weight, angle, dist) for dist in distances
                    ]
                    self.plot_results(distances, heights)
                    final_height = heights[-1]
                    if final_height <= enemy.height and final_height > 0:
                        print("your arrow hits the enemy")
                        damage = force / 5
                        print(f"You hit the enemy with {damage} N force.")
                        enemy_dict[enemy.name]["health"] -= damage
                        if enemy_dict[enemy.name]["health"] <= 0:
                            print("you killed the enemy")
                            enemies.pop(enemy.name)
                            break
                    else:
                        print("your arrow misses the enemy")
                        if final_height > self.enemy.height:
                            print(f"your arrow flies {abs(final_height - self.enemy.height)} m above the enemy")
                        elif final_height < 0:
                            print(f"your arrow does not reach the enemy, try aiming higher")
                    arrows -= 1
                    print(f"you have {arrows} arrows left")
                    archer_fight()
                    if arrows <= 0:
                        options = [
                            "Use your sword to fight the enemy",
                            "Go back to the village",
                        ]
                        print("You have used up all your arrows, you can choose to either: ")
                        for i, option in enumerate(options, start=1):
                            print(f"{i}. {option}")

                        choice = self.get_valid_integer_input(
                        choice = self._get_valid_integer_input(
                            "Enter the number of your choice: ",
                            valid_options=list(range(1, len(options) + 1)),
                        )

                        if choice == 1:
                            from fighting_final import fight as sword_fight
                            sword_fight()
                        elif choice == 2:
                            break
                except Exception:
                    traceback.print_exc()
                    input("press enter to continue")
        except Exception:
            traceback.print_exc()

    def get_valid_integer_input(self, prompt: str, valid_options: List[int] = []) -> int:
    # Get valid integer input from the user
    @validate_positive_integer
    def _get_valid_integer_input(self, prompt: str) -> int:
    # Get user input and validate it
        user_input = input(prompt)
        try:
            valid_input = int(user_input)
            return valid_input
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return self._get_valid_integer_input(prompt)  # Recursive call to retry input

    @validate_range(400, 710)
    def _get_valid_force_input(self, prompt: str) -> int:
        while True:
            user_input = input(prompt)
            try:
                user_input = int(input(prompt))
                if valid_options and user_input not in valid_options:
                    raise ValueError
                return user_input
                valid_input = int(user_input)
                if 400 <= valid_input <= 710:
                    return valid_input
                else:
                    print("Invalid input. Please enter a force between 400 and 710.")
                    for item in inventory[:]:
                        if item.name == "Bow":
                            inventory.remove(item)
                    escape = input("would you like to escape back to your own village to buy a new bow, or do you want to use your sword, 1. escape, 2. use sword")
                    if escape == "1":
                        if random.randint(0, self.dexterity) <= 10:
                            print("you manage to escape back to your own village")
                            from final_beginning import home
                            home()
                        else:
                            print("you failed to escape back to your own village")
                            print("the enemy captures you and kills you")
                            exit()
                    elif escape == "2":
                        from fighting_final import fight as sword_fight
                        sword_fight()
            except ValueError:
                print("Invalid input. Please enter an integer.")
                if valid_options:
                    print(f"Valid options are: {', '.join(map(str, valid_options))}")

    @validate_range(0, 76)
    def _get_valid_length_input(self, prompt: str) -> int:
        while True:
            user_input = input(prompt)
            try:
                valid_input = int(user_input)
                if 0 <= valid_input <= 76:
                    return valid_input
                else:
                    print("Your string snaps, you now need to replace it. Next time don't pull it back too far")
                    for item in inventory[:]:
                        if item.name == "Bow":
                            inventory.remove(item)
                    escape = input("would you like to escape back to your own village to buy a new bow, or do you want to use your sword, 1. escape, 2. use sword")
                    if escape == "1":
                        if random.randint(0, self.dexterity) <= 10:
                            print("you manage to escape back to your own village")
                            from final_beginning import home
                            home()
                        else:
                            print("you failed to escape back to your own village")
                            print("the enemy captures you and kills you")
                            exit()
                    elif escape == "2":
                        from fighting_final import fight as sword_fight
                        sword_fight()
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @validate_range(0, 360)
    def _get_valid_angle_input(self, prompt: str) -> int:
        while True:
            user_input = input(prompt)
            try:
                valid_input = int(user_input)
                if 0 <= valid_input <= 90:
                    return valid_input
                elif 90 < valid_input <= 360:
                    print("the arrow goes straight up and lands somewhere behind you")
                else:
                    print("Invalid input. Please enter an angle between 0 and 360.")
            except ValueError:
                print("Invalid input. Please enter an integer.")



