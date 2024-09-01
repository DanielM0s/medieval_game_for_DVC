# This is a dictionary of the player's stats
# The keys are the names of the stats and the values are the values of the stats
# The values are all integers except for the name which is a string
stats_dict: dict[str, int|str] = {
    # The player's name
    'name': '',
    # The player's points
    "points": 0,
    # The player's coins
    "coins": 0,
    # The player's strength
    "strength": 0,
    # The player's dexterity
    "dexterity": 0,
    # The player's constitution
    "constitution": 0,
    # The player's intelligence
    "intelligence": 0,
    # The player's wisdom
    "wisdom": 0,
    # The player's charisma
    "charisma": 0,
    # The player's experience points
    "xp": 0
}

# This is a list of the items in the player's inventory
inventory = []

# This is the player's level
lvl = 1

# This is the player's total strength
total_strength = 0

