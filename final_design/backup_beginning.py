from character_stats import stats_dict
import random
from character_stats import inventory
def point_calculator(p, n) -> int:
    return p - n
stats_dict["points"] = 20
def display_stats():
    print(f"your character name is {stats_dict['name']} you have {stats_dict['coins']} gold,  your strength is {stats_dict['strength']} your charisma is {stats_dict['charisma']} your constitution is {stats_dict['constitution']}, your dexterity is {stats_dict['dexterity']}, your intelligence is {stats_dict['intelligence']}, and your wisdom is {stats_dict['wisdom']}.")

def set_difficulty():
    difficulty = input("would you like to play easy or hard? ")
    if difficulty == "easy":
        for stats in stats_dict:
            if isinstance(stats_dict[stats], int):
                stats_dict[stats] += 5
    elif difficulty == "hard":
        for stats in stats_dict:
            if isinstance(stats_dict[stats], int):
                stats_dict[stats] -= 5
    else:
        print("Invalid input")

def check_points():
    if stats_dict["points"] < 0:
        print("You have spent all your points.")
        repeat = input("Would you like to try again? ")
        if repeat == "yes":
            for stats in stats_dict:
                if isinstance(stats_dict[stats], int):
                    stats_dict[stats] = 0
                stats_dict["points"] = 20
            return 0
        elif repeat == "no":
            return 1
    elif stats_dict["points"] > 20:
        raise ValueError
    


while True:
    try:
        (stats_dict["name"]) = input("what is your character's name? ")
        print("you have {} points to spend between your main stats. choose between strength, fortune, charisma, constitution, dexterity, intelligence and wisdom: ".format(stats_dict["points"]))
        strength = int(input("strength: "))
        (stats_dict["strength"]) = strength
        stats_dict["points"] = point_calculator(stats_dict["points"], stats_dict["strength"])
        check_digit = check_points()
        if check_digit == 1:
            break
        elif check_digit == 0:
            continue
        print(stats_dict["points"])
        fortune = int(input("fortune: "))
        (stats_dict["coins"]) = fortune
        stats_dict["points"] = point_calculator(stats_dict["points"], stats_dict["coins"])
        check_digit = check_points()
        if check_digit == 1:
            break
        elif check_digit == 0:
            continue
        print(stats_dict["points"])   
        charisma = int(input("charisma: "))
        (stats_dict["charisma"]) = charisma
        stats_dict["points"] = point_calculator(stats_dict["points"], stats_dict["charisma"])
        check_digit = check_points()
        if check_digit == 1:
            break
        elif check_digit == 0:
            continue
        print(stats_dict["points"])
        constitution = int(input("constitution: "))
        (stats_dict["constitution"]) = constitution
        stats_dict["points"] = point_calculator(stats_dict["points"],stats_dict["constitution"])
        check_digit = check_points()
        if check_digit == 1:
            break
        elif check_digit == 0:
            continue
        print(stats_dict["points"])
        dexterity = int(input("dexterity: "))
        (stats_dict["dexterity"]) = dexterity
        stats_dict["points"] = point_calculator(stats_dict["points"], stats_dict["dexterity"])
        check_digit = check_points()
        if check_digit == 1:
            break
        elif check_digit == 0:
            continue
        print(stats_dict["points"])
        intelligence = int(input("intelligence: "))
        (stats_dict["intelligence"]) = intelligence
        stats_dict["points"] = point_calculator(stats_dict["points"], stats_dict["intelligence"])
        check_digit = check_points()
        if check_digit == 1:
            break
        elif check_digit == 0:
            continue
        print(stats_dict["points"])
        wisdom = int(input("wisdom: "))
        (stats_dict["wisdom"]) = wisdom
        stats_dict["points"] = point_calculator(stats_dict["points"], stats_dict["wisdom"])
        check_digit = check_points()
        if check_digit == 1:
            break
        elif check_digit == 0:
            continue
        print(stats_dict["points"])
        for stats in stats_dict:
            if isinstance(stats_dict[stats], int):
                stats_dict[stats] *= 20
        display_stats()
        set_difficulty()
        break
    except ValueError:
        print("Please enter a valid number.")


import shop
shop.medieval_shop()

import final_fighting
difficulty = "easy"
final_fighting.fight_main()
import bow_calculator




# Attack enemy with archer
enemy = bow_calculator.Enemy(2.5, random.randint(300, 400))
bow = bow_calculator.Bow("long Bow", 710, 76)
arrow = bow_calculator.Arrow(0.1)
enemy = bow_calculator.Enemy(2.5, random.randint(300, 400))
archer = bow_calculator.Archer(bow, arrow, enemy, 100)

archer.attack()


