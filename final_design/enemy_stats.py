import random
from shop import items
from typing import Any
def generate_random_attributes():
    attributes = {
        "name": f"Enemy {random.randint(1, enemies)}",
        "coins": random.randint(10, 30),
        "strength": random.randint(10, 30),
        "dexterity": random.randint(10, 30),
        "constitution": random.randint(10, 30),
        "intelligence": random.randint(10, 30),
        "wisdom": random.randint(10, 30),
        "health": random.randint(80, 100),
        "distance": random.randint(100, 366),
    }
    return attributes
inventory: dict[str, Any] = {"Ilkwa": {"price": 50, "weight": 3, "length": 3},}
enemies = 4
enemy_dict = {}
for i in range(1, enemies + 1):
    enemy_dict[f'Enemy {i}'] = generate_random_attributes()

