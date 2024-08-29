from typing import Any
# create a dictionary of the stats
stats_dict: dict[str, int|str] = {
    'name': '',
    "points": 0,
    "coins": 0,
    "strength": 0,
    "dexterity": 0,
    "constitution": 0,
    "intelligence": 0,
    "wisdom": 0,
    "charisma": 0,
    "xp": 0
}
inventory = []
lvl = 1

def level_up(stats_dict):
    points = stats_dict["points"]
    for key in stats_dict:
        if key == "name" or key == "xp":
            continue
        stats_dict[key] += 1
    stats_dict["points"] -= 1
    print("You have leveled up!")
    print(f"You have {stats_dict['points']} points left.")
    print(stats_dict)
    return stats_dict
