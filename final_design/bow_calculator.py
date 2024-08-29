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
    from character_stats import inventory
    bow_list = [item for item in inventory if item.name == "Bow"]
    arrow_list = [item for item in inventory if item.name == "arrow x10"]
    if not bow_list or not arrow_list:
        print("You need a Bow and an arrow to fight")
        return
    bow = Bow(bow_list[0].name, bow_list[0].max_draw_force, bow_list[0].draw_length)
    arrow = Arrow(arrow_list[0].weight)
    enemies = list(enemy_dict.keys())
    while True:
        while True:
            try:
                print("Choose an enemy to fight:")
                for i, (name, stats) in enumerate(enemy_dict.items()):
                    print(f"{i+1}. {name}")
                enemy_index = int(input("Enter the number of the enemy: "))
                if 0 <= enemy_index < len(enemies):
                    break
                else:
                    print("Invalid input. Please enter a number between 0 and", len(enemies) - 1)
            except ValueError:
                print("Invalid input. Please enter a number.")
        enemy_name = enemies[enemy_index]
        enemy = Enemy(enemy_name)
        archer = Archer(bow, arrow, enemy, 100)
        archer.attack()

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
    def __init__(self, bow: Bow, arrow: Arrow, enemy: Enemy, health: int):
        self.bow = bow
        self.arrow = arrow
        self.enemy = enemy
        self.health = health
    
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
                    force = self._get_valid_integer_input("how much force do you want to apply? ")
                    length = self._get_valid_integer_input("how far do you pull the string back in cm? ")
                    if length > self.bow.max_pull_distance:
                        print("Your string snaps, you now need to replace it. Next time don't pull it back too far")
                        escape = input("would you like to escape back to your own village to buy a new bow, or do you want to use your sword, 1. escape, 2. use sword")
                        if escape == "1":
                            if random.randint(0, stats_dict["wisdom"]) <= 10:
                                print("you manage to escape back to your own village")
                                from final_beginning import home
                                home()
                            else:
                                print("you failed to escape back to your own village")
                                print("the enemy captures you and kills you")
                                exit()
                        elif escape == "2":
                            return
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
                valid_input = int(user_input)
                if 400 <= valid_input <= 710:
                    return valid_input
                else:
                    print("Invalid input. Please enter a force between 400 and 710.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @validate_range(0, 100)
    def _get_valid_length_input(self, prompt: str) -> int:
        while True:
            user_input = input(prompt)
            try:
                valid_input = int(user_input)
                if 0 <= valid_input <= 100:
                    return valid_input
                else:
                    print("Invalid input. Please enter a length between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @validate_range(0, 360)
    def _get_valid_angle_input(self, prompt: str) -> int:
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


