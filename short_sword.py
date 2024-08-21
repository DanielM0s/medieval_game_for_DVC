# This script simulates a medieval combat game.

# Importing necessary modules
import math
import random

# Class representing an opponent
class Opponent:
    """Represents an opponent in the game."""

    def __init__(self, name, health, max_force, max_sword_length):
        """Initialize the Opponent class."""
        self.name = name
        self.health = health
        self.max_force = max_force
        self.max_sword_length = max_sword_length

    def attack(self, force):
        """Calculate the opponent's attack."""
        counter_force = random.randint(1, self.max_force)
        damage = force * self.max_sword_length
        player.lose_health(damage)
        # Check if the opponent's attack is a counter attack
        if random.random() < self.max_sword_length/self.max_force and counter_force > force:
            return f"{self.name} counter attacked you for {force - counter_force} damage."
        else:
            return f"{self.name} hit you for {force} damage."

# Class representing the player
class Player:
    """Represents the player in the game."""

    def __init__(self, name, health, max_force):
        """Initialize the Player class."""
        self.name = name
        self.health = health
        self.max_force = max_force

    def lose_health(self, damage):
        """Reduce the player's health."""
        self.health -= damage

# Dictionary representing a short sword
shortsword = {
    "name": "Seax",
    "length(mm)": 3,
    "weight(g)": 450,
}

# Instantiating players and opponents
player = Player("You", 100, 500)
opponents = [
    Opponent("Enemy", 100, 1000, shortsword["length(mm)"]),
    Opponent("Dragon", 200, 1500, shortsword["length(mm)"]*2),
    Opponent("King", 300, 2000, shortsword["length(mm)"]*3)
]

# Main game loop
def main():
    """Main game loop."""
    while True:
        # Display the list of opponents and ask the player to choose one
        print("Choose an opponent:")
        for index, opponent in enumerate(opponents):
            print(f"{index}: {opponent.name}")
        opponent_choice = int(input("Enter opponent number: "))
        current_opponent = opponents[opponent_choice]
        while current_opponent.health > 0 and player.health > 0:
            # Display the current health of both the player and the opponent
            print(f"Your health: {player.health} Enemy health: {current_opponent.health}")
            force = int(input("Enter how much force you want to apply: "))
            damage = force * shortsword["length(mm)"]
            response = current_opponent.attack(force)
            if response.startswith(current_opponent.name + " counter attacked you for"):
                player.lose_health(int(response.split()[-1]))
            elif current_opponent.health <= 0:
                print(f"You defeated {current_opponent.name}!")
                break
            else:
                print(response)
            if player.health <= 0:
                print("You have been defeated!")
                break

# Running the game
if __name__ == "__main__":
    main()


