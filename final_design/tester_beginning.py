import shop
from character_stats import stats_dict, inventory
import random

print("welcome to The Rise of Shaka Zulu.")
def display_stats():
    print(f"Your character name is {stats_dict['name']}. You have {stats_dict['coins']} gold, your strength is {stats_dict['strength']}, your charisma is {stats_dict['charisma']}, your constitution is {stats_dict['constitution']}, your dexterity is {stats_dict['dexterity']}, your intelligence is {stats_dict['intelligence']}, and your wisdom is {stats_dict['wisdom']}.")

def set_difficulty(difficulty):
    if difficulty == "easy":
        for stat in stats_dict:
            if isinstance(stats_dict[stat], int):
                stats_dict[stat] += 5
    elif difficulty == "hard":
        for stat in stats_dict:
            if isinstance(stats_dict[stat], int):
                stats_dict[stat] -= 5
    else:
        raise ValueError("Invalid input")
def minus_points(p, n):
    return p - n

def check_points():
    if stats_dict["points"] <= 0:
        print("You have spent all your points.")
        repeat = input("Would you like to try again? ")
        if repeat.lower() == "yes":
            stats_dict.update({stat: 0 for stat in stats_dict if isinstance(stats_dict[stat], int)})
            stats_dict["points"] = 20
            return False
        elif repeat.lower() == "no":
            return True
        else:
            print("Invalid input.")
            return False
    elif stats_dict["points"] > 20:
        raise ValueError
stats_dict["points"] = 20
while True:
    try:
        stats_dict["name"] = input("What is your character's name? ")
        print(f"You have {stats_dict['points']} points to spend between your main stats. Choose between coins, strength, dexterity, constitution, intelligence,wisdom, charisma")
        for stat in ["coins", "strength", "dexterity", "constitution","intelligence","wisdom","charisma"]:
            value = int(input(f"{stat}: "))
            stats_dict[stat] = value
            stats_dict["points"] = minus_points(stats_dict["points"], value)
            print(f"You have {stats_dict['points']} points left.")
            checker = check_points()
            if checker is False:
                continue
            elif checker is True:
                break
        else:
            continue
        for stat in stats_dict:
            if isinstance(stats_dict[stat], int):
                stats_dict[stat] *= 20
        display_stats()
        set_difficulty(input("Would you like to play easy or hard? "))
        break
    except ValueError as e:
        print(e)


shop.medieval_shop()
n = input("what would you like to do next")
if n == "fight":
    from fighting_final import fight
    fight()
elif n == "bow":
    import bow_calculator
    bow_list = [item for item in inventory if item.name == "Bow"]
    arrow_list = [item for item in inventory if item.name == "arrow x10"]
    bow = bow_calculator.Bow(bow_list[0].name, bow_list[0].max_draw_force, bow_list[0].draw_length)
    arrow = bow_calculator.Arrow(arrow_list[0].weight)
    enemy = bow_calculator.Enemy(2.5, random.randint(300, 400))
    archer = bow_calculator.Archer(bow, arrow, enemy, 100)

    archer.attack()
