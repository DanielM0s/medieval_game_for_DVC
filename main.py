import random

player = {
    "name": "Player",
    "health": 100,
    "gold": 10,
    "wood": 0,
    "food": 0,
    "level": 1,
    "bonus": 0,
    "defense": 0
}
enemy = {
    "health": 100,
    "enemy distance": random.randint(100, 366),
}
if player["health"] <= 0:
    print("You died.")
    exit()
inventory = {}
def battle_melee():
def battle_ranged():
    while enemy_amount > 0:
        while weapon_chooser == "sword" or "axe":
            print()

def explore_village():
    print("You are exploring the village...")
    resources_found = ["gold", "wood", "food"]
    found_resource = random.choice(resources_found)
    player[found_resource] += 1
    print(f"You found 1 {found_resource}.")
   

def visit_shop():
    print(f"You have {player['gold']} gold.")
    print("Welcome to the village shop!")
    typeofweapon = input("would you like to buy a ranged weapon or a melee weapon? ")
    if typeofweapon == "ranged":
        print("1. Bow (25 gold)")
        print("2. Crossbow (35 gold)")
        print("3. arrow x20 (8 gold)")
        print("4. dart x20 (5 gold)")
        weapon = input("what type of weapon do you want to buy")
        if weapon == "bow":
            bow = input("do you want to buy a ")
    elif typeofweapon == "melee":
        print("3. wooden Sword (10 gold)")
        print("4. iron Sword (15 gold)")
        print("5. Steel Sword (30 gold)")
        print("6. Axe (20 gold)")
    else:
        print("please choose ranged or melee")
   
   
    print("10. sheild(10 gold)")
    choice = input("Choose an option: ")
    if choice == "1" and player["gold"] >= 5:
        player["gold"] -= 5
        player["wood"] += 1
        print("You bought 1 wood.")
    elif choice == "2" and player["gold"] >= 3:
        player["gold"] -= 3
        player["food"] += 1
        print("You bought 1 food.")
    elif choice == "3" and player["gold"] >= 10:
        player["gold"] -= 10
        inventory["sword"] = "wooden"
        print("You bought a wooden sword.")
        player["bonus"] += 1
    elif choice == "4" and player["gold"] >= 15:
        player["gold"] -= 15
        inventory["sword"] = "iron"
        print("You bought an iron sword.")
        player["bonus"] += 5
    elif choice == "5" and player["gold"] >= 30:
        player["gold"] -= 30
        inventory["sword"] = "steel"
        print("You bought a steel sword.")
        player["bonus"] += 10
    elif choice == "6" and player["gold"] >= 20:
        player["gold"] -= 20
        inventory["axe"] = "axe"
        print("You bought an axe.")
        player["bonus"] += 16
    elif choice == "7" and player["gold"] >= 25:
        player["gold"] -= 25
        inventory["bow"] = "bow"
        print("You bought a bow.")
        player["bonus"] += 20
    elif choice == "8" and player["gold"] >= 35:
        player["gold"] -= 35
        inventory["crossbow"] = "crossbow"
        print("You bought a crossbow.")
        player["bonus"] += 30
    elif choice == "9" and player["gold"] >= 8:
        player["gold"] -= 8
        inventory["arrow"] = "arrow"
        print("You bought 20 arrows.")
        player["bonus"] += 5
    elif choice == "10":
        player["gold"] -= 10
        inventory["sheild"] = "sheild"
        print("You bought a sheild.")
        player["defense"] = 10
    else:
        print("Not enough gold.")

# Game loop
while player["health"] > 0:
    print("\nDay starts.")
    command = input("you wake up in you house. all is quite. Suddenly you hear the alarm being sounded, the enemies are coming. Do you want to explore (e), defend (d), visit shop (s), or quit (q)? ").lower().strip()

    if command == "e":
        explore_village()
    elif command == "d":
        for item in inventory:
            print(f"you have {inventory[item]} of {item}")
        if len(inventory) == 0:
            print("you have no weapons, please go to the store to buy a sword")
        else:
            print("Enemies are attacking the village!")
            allies = random.randint(1, 10)
            enemy_amount = random.randint(5, 15)
            for weapon in inventory:
                print(f"you have {inventory[weapon]} of {weapon}")
            weapon_chooser = input("which weapon do you want to use? ")
            if weapon_chooser == "sword" or "axe":
                print(f"you stand at the gate gazing out at the {enemy_amount} enemies. you have {allies} allies")
                battle_start = input("the gate starts to open, which enemy do you want to fight first")
                battle_melee()
            elif weapon_chooser == "bow" or "crossbow":
                battle_ranged()
    elif command == "s":
        visit_shop()
        if visit_shop() == "quit":
            command = input("you wake up in you house. all is quite. Suddenly you hear the alarm being sounded, the enemies are coming. Do you want to explore (e), defend (d), visit shop (s), or quit (q)? ").lower().strip()
    elif command == "q":
        break

    # Day-night cycle
    if random.random() < 0.3:
        print("Night falls. Enemies are preparing to attack!")
        command = "d"

    # Level up
    if player["gold"] >= 20 * player["level"]:
        player["level"] += 1
        print(f"Congratulations! You leveled up to level {player['level']}.")

    print(f"\nHealth: {player['health']}")
    print("Resources:")
    for resource, amount in player.items():
        if resource not in ["name", "health", "level"]:
            print(f"{resource}: {amount}")