import math
import random
import traceback
from typing import List, Optional
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image, ImageDraw


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
    def __init__(self, height: float, distance: float):
        self.height = height
        self.distance = distance


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

        line, = ax.plot([], [], color='blue', marker='o')
        enemy_line, = ax.plot([], [], color='red', marker='o')
        ax.set_xlabel('Distance (m)')
        ax.set_xlim(min(distances), max(distances))
        ax.set_ylabel('Height (m)')
        ax.set_ylim(min(min(0)), max(max(heights), self.enemy.height))

        ax.grid(True, linestyle='dashed', linewidth=0.5, color='gray', alpha=0.7)

        def update(frame):
            line.set_data(distances[:frame+1], heights[:frame+1])
            enemy_line.set_data([self.enemy.distance], [self.enemy.height])
            return line, enemy_line,

        ani = animation.FuncAnimation(fig, update, frames=len(distances)-1, interval=1, repeat=False)

        def on_animation_finished(event):
            plt.close()

        ani.event_source.on_finished = on_animation_finished
        plt.show()

    # Attack the enemy
    def attack(self):
        try:
            while True:
                try:
                    print(f"Enemy distance: {self.enemy.distance} Enemy height: {self.enemy.height}")
                    hint = input("would you like to activate hints? y/n ")
                    if hint.lower() == "y":
                        print("hint: the pull force is the force that makes the string pull back")
                        if input("would you like another hint? y/n ") == "y":
                            print("hint: the maximum pull force is 710N, and the minimum pull force is 400N")
                    force = self._get_valid_integer_input("how much force do you want to apply? ")
                    length = self._get_valid_integer_input("how far do you pull the string back in cm? ")
                    if length > self.bow.max_pull_distance:
                        print("Your string snaps, you now need to replace it. Next time don't pull it back too far")
                        break
                    angle = self._get_valid_integer_input("what angle do you want to shoot the arrow? ")
                    distances = [i for i in range(0, int(self.enemy.distance) + 1, 2)]
                    heights = [
                        self.safe_calculate(force, length, self.arrow.weight, angle, dist) for dist in distances
                    ]
                    self.plot_results(distances, heights)
                    final_height = heights[-1]
                    if final_height <= self.enemy.height and final_height > 0:
                        print("your arrow hits the enemy")
                        damage = force / 10
                        print(f"You hit the enemy with {damage} N force.")
                    else:
                        print("your arrow misses the enemy")
                        if final_height > self.enemy.height:
                            print(f"your arrow flies {abs(final_height - self.enemy.height)} m above the enemy")
                        elif final_height < 0:
                            print(f"your arrow does not reach the enemy, try aiming higher")
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

