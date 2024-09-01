import random
from final_shop import items
from typing import Any

# This function generates random attributes for an enemy
# The attributes are name, coins, strength, dexterity, constitution, intelligence, wisdom, health, distance, height, and xp
# The attributes are based on the level of the player
def generate_random_attributes(name: str) -> dict[str, Any]:
    attributes = {
        # The name of the enemy
        "name": name,
        # The coins that the enemy has
        "coins": random.randint(start, level * 20),
        # The strength of the enemy
        "strength": random.randint(start, level),
        # The dexterity of the enemy
        "dexterity": random.randint(start, level),
        # The constitution of the enemy
        "constitution": random.randint(start, level),
        # The intelligence of the enemy
        "intelligence": random.randint(start, level),
        # The wisdom of the enemy
        "wisdom": random.randint(start, level),
        # The health of the enemy
        "health": random.randint(start, health_level),
        # The distance of the enemy from the player
        "distance": random.randint(300, 500),
        # The height of the enemy
        "height": 2.5,
        # The xp that the enemy gives
        "xp": level * 2,
        # The coins that the enemy gives
        "coins": random.randint(lvl*10, lvl * 100),
    }
    return attributes

# This is the inventory of the player
inventory: dict[str, Any] = {"Ilkwa": {"price": 50, "weight": 3, "length": 0.9, "type": "sword"},}

# This is the level of the player
from character_stats import lvl
level = lvl * 80
start = lvl * 30
health_level = lvl * 100
start_health = start * 70

# This function makes a certain number of enemies
# The enemies are stored in a dictionary with the name as the key
def make_enemies(num_enemies: int) -> dict[str, Any]:
    enemy_dict = {}
    names = [f"Enemy {i}" for i in range(1, num_enemies + 1)]
    for i, name in enumerate(names):
        enemy_dict[name] = generate_random_attributes(name)
    return enemy_dict

# This function makes a certain number of enemies and returns them as a dictionary
def new_enemy(num_enemies: int) -> dict[str, Any]:
    enemy_dict = make_enemies(num_enemies)
    return enemy_dict

# This is the dictionary of all enemies
enemy_dict = {}


