import random
from final_shop import items
from typing import Any
def generate_random_attributes(name: str) -> dict[str, Any]:
    attributes = {
        "name": name,
        "coins": random.randint(10, level * 20),
        "strength": random.randint(20, level),
        "dexterity": random.randint(20, level),
        "constitution": random.randint(20, level),
        "intelligence": random.randint(20, level),
        "wisdom": random.randint(20, level),
        "health": random.randint(30, health_level),
        "distance": random.randint(300, 500),
        "xp": level * 2
    }
    return attributes
inventory: dict[str, Any] = {"Ilkwa": {"price": 50, "weight": 3, "length": 0.9, "type": "sword"},}
from character_stats import lvl
level = lvl * 40
health_level = lvl * 50
def make_enemies(num_enemies: int) -> dict[str, Any]:
    enemy_dict = {}
    names = [f"Enemy {i}" for i in range(1, num_enemies + 1)]
    for i, name in enumerate(names):
        enemy_dict[name] = generate_random_attributes(name)
    return enemy_dict

def new_enemy(num_enemies: int) -> dict[str, Any]:
    enemy_dict = make_enemies(num_enemies)
    return enemy_dict
enemy_dict = {}


