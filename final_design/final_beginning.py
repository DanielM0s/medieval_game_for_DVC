import final_shop
from character_stats import stats_dict, inventory
import character_stats
import random
import time
import pyfiglet
import os
import enemy_stats

# Class representing a location in the game
class Location:
    def __init__(self, name, description):
        # Name of the location
        self.name = name
        # Description of the location
        self.description = description
        # List of locations connected to this location
        self.connections = []

    # Add a connection to another location
    def add_connection(self, location):
        self.connections.append(location)

# Dictionary containing the base probability of encountering enemies
# at each location
encounter_probabilities = {
    # Higher probability of encountering enemies at the village entrance
    "Village Entrance": 0.9,
    # Lower probability of encountering enemies in the forest
    "Forest": 0.4,
    # Medium probability of encountering enemies in the communal areas
    "Communal areas": 0.7,
    # Default probability of encountering enemies if no other location is
    # specified
    "default": 0.5
}




class Player:
    def __init__(self, name):
        # Set the player's starting location to the village
        self.location = enemy_village
        # Initialize the player's inventory as an empty list
        self.inventory = []
        # Set the player's starting level to 1
        self.level = 1
        # Set the player's starting XP to 0
        stats_dict["xp"] = 460
        # Set the amount of XP needed to level up to 10
        self.xp_to_next_level = self.level * 500
        # Set the set of locations the player has visited to an empty set
        self.visited_locations = set()

    def gain_xp(self, amount):
        # Add the given amount of XP to the player's current XP
        """
        Add the given amount of XP to the player's current XP.

        Args:
            amount (int): The amount of XP to add to the player's current XP.
        """
        stats_dict["xp"] += amount
        # Print out a message to the player that they gained XP
        print(f"You gained {amount} XP!")
        # Check if the player has leveled up
        self.check_level_up()

    def check_level_up(self):
        # Check if the player's current XP is greater than or equal to the amount of XP needed to level up
        if stats_dict["xp"] >= self.xp_to_next_level:
        
            # Call the level_up method to level up the player
            self.level_up()

    def level_up(self):
        # Increment the player's level by 1
        self.level += 1
        character_stats.lvl = self.level
        # Subtract the amount of XP needed to level up from the player's current XP
        stats_dict["xp"] -= self.xp_to_next_level
        # Set the amount of XP needed to level up to double its current value
        self.xp_to_next_level *= 2
        # Print out a message to the player that they leveled up
        print(f"you have leveled up to level {character_stats.lvl}. You have 5 points to split between your stats. your stats are: ")
        while True:
            try:
                for index, stat in enumerate(main_stats):
                    print(f"{index+1}. {stat}")
                choice = int(input("Choose a number to allocate points to: "))
                if choice < 1 or choice > len(main_stats):
                    print("Invalid input. Please enter a valid number.")
                    continue
                stat = main_stats[choice-1]
                value = int(input(f"{stat}: "))
                if value < 0:
                    print("Invalid input. Please enter a valid number.")
                    continue
                else:
                    stats_dict[stat] = int(stats_dict[stat]) + value * 30
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            stats_dict["points"] = minus_points(stats_dict["points"], value)
            print(f"{stat} now has {stats_dict[stat]}")
            print(f"You have {stats_dict['points']} points left.")
            if stats_dict["points"] < 0:
                print("you have used up more points than you have. Please try again")
                stats_dict[stat] = int(stats_dict[stat]) - value * 20
                stats_dict["points"] = 5
                continue
            elif stats_dict["points"] == 0:
                break
        # Call the unlock_new_areas method to unlock new areas for the player
        self.unlock_new_areas()

    def unlock_new_areas(self):
        # Check if the player has reached level 2
        if self.level == 2:
            # Add the forest to the list of locations connected to the village
            enemy_village.add_connection(forest)
            # Add the village to the list of locations connected to the forest
            forest.add_connection(enemy_village)
            # Add the forest to the list of locations connected to the village entrance
            forest.add_connection(village_entrance)
            # Add the forest to the list of locations connected to the huts
            forest.add_connection(huts)
            # Print out a message to the player that they have unlocked the forest
            print("You have unlocked the Forest!")
            # Generate a random reward for the player to receive
            reward = random.randint(1, stats_dict["wisdom"])
            # Generate a random number to determine the type of reward to give the player
            reward_decider = random.random()
            # Check if the player should receive the mushroom reward
            if reward_decider < 0.5:
                # Print out a message to the player that they found a mushroom and gained 10 strength
                print("You found a mushroom. You decide to eat it and gain 10 strength.")
                # Add 10 to the player's strength
                stats_dict["strength"] += 10
            # Check if the player should receive the berry bush reward
            elif reward_decider < 0.8:
                # Print out a message to the player that they found a berry bush and gained 2 dexterity
                print("You found a berry bush. You decide to eat a few berries and gain 2 dexterity.")
                # Add 2 to the player's dexterity
                stats_dict["dexterity"] += 2
            # Check if the player should receive the small rock reward
            else:
                # Print out a message to the player that they found a small rock and gained 1 charisma
                print("You found a small rock. You decide to keep it as a good luck charm and gain 1 charisma.")
                # Add 1 to the player's charisma
                stats_dict["charisma"] += 1
        # Check if the player has reached level 3
        elif self.level == 3:
            # Add the communal areas to the list of locations connected to the forest
            forest.add_connection(communal_areas)
            # Add the village to the list of locations connected to the communal areas
            communal_areas.add_connection(enemy_village)
            # Add the communal areas to the list of locations connected to the huts
            communal_areas.add_connection(huts)
            # Add the communal areas to the list of locations connected to the family homesteads
            communal_areas.add_connection(family_homesteads)
            # Add the village to the list of locations connected to the communal areas
            enemy_village.add_connection(communal_areas)
            # Add the cattle kraal to the list of locations connected to the communal areas
            cattle_kraal.add_connection(communal_areas)
            # Add the huts to the list of locations connected to the communal areas
            huts.add_connection(communal_areas)
            # Add the family homesteads to the list of locations connected to the communal areas
            family_homesteads.add_connection(communal_areas)
            # Print out a message to the player that they have unlocked the communal areas
            print("You have unlocked the communal areas!")
        # Check if the player has reached level 4
        elif self.level == 4:
            # Add the chief's hut to the list of locations connected to the cattle kraal
            cattle_kraal.add_connection(chief_hut)
            # Print out a message to the player that they have unlocked the chief's hut
            print("You have unlocked the Chief's Hut!")
    def move(self, new_location):
        if new_location in self.location.connections:
            self.location = new_location
            print(f"You move to {new_location.name}.")
            print(new_location.description)
            if new_location not in self.visited_locations:
                self.visited_locations.add(new_location)
                self.gain_xp(3)  # Gain XP for visiting a new location
            # Determine the base probability of encountering soldiers
            base_probability = encounter_probabilities.get(new_location.name, encounter_probabilities["default"])
            # Adjust probability based on player level
            encounter_chance = base_probability + (self.level * 0.3)
            if random.random() < encounter_chance:
                encounter_soldiers(self)

        else:
            print("You can't go there from here.")
    

# Define game locations
village = Location("Your home village", "The familiar smells of home greet you like an old friend.")
cattle_kraal = Location("Cattle Kraal", "You are in the central cattle kraal, where the village's cattle are kept. The air is filled with the sounds of livestock.")
huts = Location("Huts", "You are among the round huts of the villagers, each made from mud and thatch. The huts are arranged in a circular pattern.")
family_homesteads = Location("Family Homesteads", "You are in the area where families have their own homesteads, consisting of several huts for different purposes.")
chief_hut = Location("Chief's Hut", "You stand before the chief's hut, larger and more elaborately decorated than the others. It is located at a prominent position in the village.")
village_entrance = Location("Village Entrance", "You are at the entrance of the village, a single guarded point that leads directly to the cattle kraal.")
communal_areas = Location("Communal Areas", "You are in the communal areas where villagers gather for meetings, ceremonies, and social activities.")
forest = Location("Forest", "You enter a dense forest, the trees towering above you.")
enemy_village = Location("Enemy Village", "You see the enemy village, soldiers scattered around.")

# Initial connections
enemy_village.add_connection(cattle_kraal)
enemy_village.add_connection(huts)
enemy_village.add_connection(family_homesteads)
enemy_village.add_connection(village_entrance)
village_entrance.add_connection(village)
enemy_village.add_connection(village)
cattle_kraal.add_connection(enemy_village)
cattle_kraal.add_connection(village_entrance)
cattle_kraal.add_connection(huts)

huts.add_connection(enemy_village)
huts.add_connection(cattle_kraal)
family_homesteads.add_connection(enemy_village)

village_entrance.add_connection(enemy_village)
village_entrance.add_connection(cattle_kraal)




def game_loop(player):
    """
    Main game loop.

    This function will loop until the user chooses to quit.

    Parameters
    ----------
    player : Player
        The player object to move around the game world.
    """
    
    while True:
        #[print the current location and description]
        print(f"\nYou are at: {player.location.name}")
        print(player.location.description)

        #[print the available options]
        print("Options:")
        for i, location in enumerate(player.location.connections):
            print(f"{i + 1}. Go to {location.name}")
        #[print the option to quit]
        print("Q. Quit")

        #[get the user's input]
        choice = input("Enter your choice: ").strip().lower()
        #[if the user wants to quit, end the game]
        if choice == 'q':
            print("Thanks for playing!")
            break
        #[if the user entered a number, move to that location]
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(player.location.connections):
                new_location = player.location.connections[choice - 1]
                #[if the user wants to go home, return to the home function]
                if new_location == village:
                    player.location = new_location
                    train_points = character_stats.lvl * 2
                    return home()
                #[otherwise, move to the new location]
                else:
                    player.move(new_location)
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please try again.")

def fight_flight():
    # This function asks the player if they want to fight, sneak past, or run away from a group of enemy soldiers
    while True:
        try:
            # Ask the player what they want to do
            fighting = input("You are spotted by a group of enemy soldiers! You can either 1. Fight them, 2. sneak past them, or 3. run away. ")
            # If the player enters a digit, convert it to an integer and check if it is a valid choice
            if fighting.isdigit():
                fighting = int(fighting)
                if fighting == 1:
                    # If the player chooses to fight, return 1
                    return 1
                elif fighting == 2:
                    # If the player chooses to sneak past, return 2
                    return 2
                elif fighting == 3:
                    # If the player chooses to run away, return 3
                    return 3
                else:
                    # If the player enters an invalid digit, print an error message and continue to loop
                    print("Invalid input. Please enter a digit between 1 and 3.")
                    continue
            # If the player enters a string, check if it contains the words "fight", "sneak", or "run"
            elif "fight" in fighting.lower():
                # If the player types "fight", return 1
                return 1
            elif "sneak" in fighting.lower():
                # If the player types "sneak", return 2
                return 2
            elif "run" in fighting.lower():
                # If the player types "run", return 3
                return 3
            elif "q" in fighting.lower():
                # If the player types "q", exit the game
                exit()
            else:
                # If the player enters an invalid string, print an error message and continue to loop
                print("Invalid input.")
                continue
        except Exception as e:
            # If an error occurs, print an error message and continue to loop
            print("An error occurred. Please try again.")
            print(e)

def encounter_soldiers(player):
    try:
        # import the enemy stats module
        from enemy_stats import enemy_dict
        # generate a random number of enemies between 2 and 3 times the player's level
        number_of_enemies = random.randint(character_stats.lvl*2, character_stats.lvl*3)
        # add the new enemies to the enemy dictionary
        enemy_dict.update(enemy_stats.new_enemy(number_of_enemies))

        # ask the player if they want to fight, sneak, or run
        fighting = fight_flight()                
        if fighting == 1:
            # list the player's swords and bows
            print("You have the following weapons in your inventory:")
            sword_list = [item for item in inventory if item.type == "sword"]
            bow_list = [item for item in inventory if item.type == "bow"]
            # if the player doesn't have a sword or bow, tell them they need one to fight
            if not sword_list and not bow_list:
                print("You need a sword or bow to fight")
                return encounter_soldiers(player)
            # list the swords and bows in the player's inventory
            for i, item in enumerate(sword_list, 1):
                print(f"{i}. {item.name}")
            for i, item in enumerate(bow_list, 1+len(sword_list)):
                print(f"{i}. {item.name}")
            # ask the player which weapon they want to use
            try:
                while True:
                    choice = int(input("Which weapon would you like to use? (Enter the number) "))
                    # if the player enters a valid number, use the chosen weapon
                    if 1 <= choice <= len(inventory):
                        chosen_weapon = inventory[choice - 1]
                        if chosen_weapon.type == "sword":
                            print(f"You have chosen to use your {chosen_weapon.name}. Good luck!")
                            print(f"You draw your {chosen_weapon.name} and prepare to fight. The enemy soldiers charge at you. You swing your sword and prepare to face them.")
                            from fighting_final import fight
                            fight()
                            break  
                        elif chosen_weapon.type == "bow":
                            print("You have chosen to use your Bow. Good luck!")
                            import bow_calculator
                            from bow_calculator import start_archery
                            start_archery()
                            break
                        else:
                            print("Invalid input. Please enter a valid number.")
                            continue
                    else:
                        print("Invalid input. Please enter a number of a sword or bow in your inventory.")
                        return encounter_soldiers(player)
            except ValueError:
                print("Invalid input. Please enter a number.")
                return encounter_soldiers(player)
        elif fighting == 2:
            # if the player chooses to sneak, roll a dexterity check
            # if the roll is >= 5, the player successfully sneaks past
            # the enemy soldiers
            sneak =random.randint(1, stats_dict["dexterity"])
            if sneak >= 5:
                print("You successfully sneak past the enemy soldiers.")
                game_loop(player)
            else:
                print("You failed to sneak past the enemy soldiers. You now have to fight them.")
                return encounter_soldiers(player)
        elif fighting == 3:
            print("You turn around and run away. You manage to escape the enemy village.")
            home()
            return
        else:
            print("Invalid input. Please enter 'fight', 'run', or 'sneak'")
            return encounter_soldiers(player)

    except ModuleNotFoundError:
        print("You don't have a sword or bow to fight. You now have to run away.")
        village_entry()
            

    except ValueError:
        print("Invalid input. Please try again.")
        encounter_soldiers()

    except KeyboardInterrupt:
        print("Thanks for playing!")


print ("""
=========================================================================================
                                Welcome
                                  to
""")
print("\033[36;1m" + "{:^80}".format(pyfiglet.figlet_format("Vengeance Against the Zulu King", font='slant', justify='center')) + "\033[0m")
print("""
================================================================================
""")

stats_dict["name"] = input("What is your character's name? ")
while not stats_dict["name"]:
    print("Name cannot be empty. Please try again.")
    stats_dict["name"] = input("What is your character's name? ")

        
print(f"""
In the heart of Zululand, a young warrior named {stats_dict["name"]} lived a peaceful life in his village, surrounded by the warmth of their family and the strength of their community. Their father, a respected warrior, taught them the ways of the Zulu, instilling in them the values of honor, courage, and loyalty.

One fateful night, the tranquility of {stats_dict["name"]}'s village was shattered by the fierce attack of a neighboring tribe. Flames engulfed the huts, and the air was filled with the cries of the people. Amidst the chaos, {stats_dict["name"]} witnessed the brutal slaying of their father by the chieftain of the rival clan, Shaka Zulu. The once vibrant village was left in ruins, and {stats_dict["name"]}'s world was turned upside down.

With nothing left but the memories of their fallen family and the burning desire for justice, {stats_dict["name"]} vowed to restore their honor and avenge their father's death. They embarked on a perilous journey, determined to become a warrior worthy of their father's legacy. Along the way, they would face numerous challenges, forge alliances, and uncover the secrets of their heritage.

In "Rise of Shaka Zulu," players will guide {stats_dict["name"]} through their journey, making critical decisions that will shape their destiny. Will {stats_dict["name"]} become the hero their people need, or will the path of vengeance consume them? The fate of Zululand rests in your hands.
""")


def display_stats():
    """Prints the current stats of the player."""
    print(f"Your character name is {stats_dict['name']}. You have {stats_dict['coins']} gold, your strength is {stats_dict['strength']}, your charisma is {stats_dict['charisma']}, your constitution is {stats_dict['constitution']}, your dexterity is {stats_dict['dexterity']}, your intelligence is {stats_dict['intelligence']}, and your wisdom is {stats_dict['wisdom']}.")

def set_difficulty(difficulty):
    """Adjusts the player's stats based on the difficulty level."""
    if difficulty == "easy":
        # Increase all stats by 5 if the difficulty is set to easy
        for stat in stats_dict:
            if isinstance(stats_dict[stat], int):
                stats_dict[stat] += 5
    elif difficulty == "hard":
        # Decrease all stats by 5 if the difficulty is set to hard
        for stat in stats_dict:
            if isinstance(stats_dict[stat], int):
                stats_dict[stat] -= 5
    else:
        raise ValueError("Invalid input")

def minus_points(p, n):
    """Subtracts n points from p."""
    return p - n


def check_points():
    # Check if the player has spent all of their points
    points = stats_dict["points"]
    if points <= 0:
        print("You have spent all your points.")
        points = 20
        # Check if the player has not allocated any points to any of their stats
        for stat in stats_dict:
            if all(isinstance(stats_dict[stat], int) and stats_dict[stat] > 0 for stat in main_stats):
                points = 0
                total = sum([stats_dict[stat] for stat in main_stats])
                # Check if the player has not allocated the correct number of points
                if total != 20:
                    if total < 20:
                        print("You have used less than 20 points. Please try again.")
                    elif total > 20:
                        print("You have used more than 20 points. Please try again.")
                    return False
                # Ask the player if they want to try again
                while True:
                    repeat = input("Would you like to try again?(If you are happy with your stats, type 'no') ")
                    if repeat.lower() in {"yes", "y"}:
                        return False
                    elif repeat.lower() == "no":
                        stats_dict["points"] = 0
                        return True
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                print("All stats must have a value above 0.")
                return False
        return True
    elif points > 20:
        raise ValueError("Too many points. Maximum is 20.")
stats_dict["points"] = 20
# Start the loop to allocate points to main stats
while True:
    try:
        # Loop to allocate points to main stats
        while True:
            print(f"First off, you need to choose your stats. You have {stats_dict['points']} points to spend between your main stats. To do this, you will be asked to allocate points to each of your stats. You can choose how many points you want to allocate to each stat, you have 7 stats, coins, strength, dexterity, constitution, intelligence, wisdom, and charisma. When you have finished allocating all of your points, you will have the option to go back and change your allocations if you want to. If you are happy with your allocations, you can choose to keep them and continue with the game.")
            main_stats = ["coins", "strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
            stat_index = 0
            # Loop through each stat in the main stats list
            while stat_index < len(main_stats):
                stat = main_stats[stat_index]
                value = None
                # Loop to get the number of points to allocate to each stat
                while value is None:
                    try:
                        value = int(input(f"{stat}: "))
                        if value < 0:
                            print("Invalid input. Please enter a valid number.")
                            value = None
                        else:
                            stats_dict[stat] = value
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        value = None
                # Subtract the allocated points from the total points
                stats_dict["points"] = minus_points(stats_dict["points"], value)
                # Check if the player has finished allocating all of their points
                checker = check_points()
                if checker == True:
                    break
                elif checker == False:
                    stat_index = 0
                    stats_dict["points"] = 20
                    continue
                print(f"You have {stats_dict['points']} points left.")
                stat_index += 1
            break
        # Loop to allocate points to main stats if the player wants to change their allocations
        while int(stats_dict["points"]) > 0:
            stat = input("Choose a stat to allocate points to: ")
            if stat in main_stats:
                value = None
                while value is None:
                    try:
                        value = int(input(f"{stat}: "))
                        if value < 0:
                            print("Invalid input. Please enter a valid number.")
                            value = None
                        else:
                            stats_dict[stat] = int(stats_dict[stat]) + value
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        value = None
                stats_dict["points"] = minus_points(stats_dict["points"], value)
                print(f"You have {stats_dict['points']} points left.")
            else:
                print("Invalid stat. Please choose a main stat.")
        # Multiply each stat by 30 to get the final stat value
        for stat in stats_dict:
            if isinstance(stats_dict[stat], int):
                stats_dict[stat] *= 30
        display_stats()
        # Ask the player if they want to play on easy or hard difficulty
        while True:
            difficulty = input("Would you like to play easy or hard? ")
            if difficulty.lower() in {"easy", "hard"}:
                set_difficulty(difficulty)
                break
            else:
                print("Invalid input. Please choose 'easy' or 'hard'.")
        break
    except Exception as e:
        print("An error occurred. Please try again.")
        print(e)
coins = stats_dict["coins"]
print("Next you need to choose your weapons. You should have enough money to buy at least one weapon, choose between melee weapons and ranged weapons depending on how you want to attack your enemies, but remember to buy arrows for your ranges weapon, especially if you don't have a melee weapon, because when you run out of arrows you need to find a way to escape, or use your meele weapon, but remember to buy food as well, as it provides you with health. If you don't have enough money to buy what you want now don't worry, you can loot your enemies after you have defeated them. ")
print(" ", end='')
weapons = [
    ("\033[31mIlkwa\033[0m", "a spear that was originally introduced by Shaka Zulu, because when they fought in his father's time they would throw their spears at each other, then use each other's spears until they were out of spears, but by using the short spear, they would hold onto there weapons", 0.9),
    ("\033[32mAssegai\033[0m", "a light throwing-spear used in both hunting and war, typically around 1.8 meters long with a 15.2 centimeter long steel head", 1.8),
    ("\033[33mKnobkerrie\033[0m", "A Knobkerrie is a strong, short wooden club with a heavy rounded knob or head on one end, traditionally used by Southern AfricanTribes including the Zulu, as a weapon in warfare. The word Knobkerrie derives from the Dutch knop (knob), and the Bushman and Hottentot kerrie (stick).The weapon is employed at close quarters, or as a throwing club. The knobkerrie was emblematic of the Zulu people. A man always carried one, a custom which has not yet disappeared in rural areas. Made of heavy wood, it was an effective weapon, and when you use it your damage is multiplied by 2", 0.5)
    
]
# This code prints out a list of weapons to the user with their names
# and descriptions. The user can then choose which weapon to buy
# based on the information provided. The code also prints out a
# warning to the user about the length of the weapon and how it
# effects the damage it deals to enemies.
print(" ", end='')
# Explain how force is calculated on a lever and how it applies to
# weapons
print("In physics you calculate force on a lever by multiplying the force applied at the bottom by the length of the object. A sword is affectively a lever, so when picking your weapon pay careful attention to it's length, the longer the weapon the more damage you will deal to your enemies.")
print(" ", end='')
for i, weapon in enumerate(weapons):
    # Print out the weapon name with a delay between each letter
    for letter in weapon[0]:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print(": ", end='', flush=True)
    time.sleep(0.1)
    # Print out the weapon description with a delay between each letter
    for letter in weapon[1]:
        print(letter, end='', flush=True)
        time.sleep(0.01)
    print(". The ", end='', flush=True)
    time.sleep(0.05)
    # Print out the weapon name with a delay between each letter
    print(weapon[0], end='', flush=True)
    time.sleep(0.05)
    print(" has a length of ", end='', flush=True)
    time.sleep(0.05)
    # Print out the weapon length with a delay between each letter
    print(str(weapon[2])+" meters", end='', flush=True)
    time.sleep(0.05)
    if i != len(weapons) - 1:
        print('\n')
    else:
        print("")
def village_entry():
    """
    This function is the main loop of the game, it will continue to run until the player chooses to quit
    """
    while True:
        try:
            # Print a warning to the player that if they don't have any weapons
            # in their inventory all items from their inventory will be removed
            # and they will be given the money to buy a weapon
            print("\033[91mWarning, if you don't have any weapons in your inventory all items from your inventory will be removed and you will be given the money to buy a weapon\033[0m")
            
            # Ask the player what they want to do
            begin = input("You start in the ruins of your home town. You can choose to 1. go to shop, 2. train, 3. fight, or Q to quit. What would you like to do? ")

            # If the player enters a digit try to convert it to an integer
            if begin.isdigit():
                begin = int(begin)
                # If the player chooses 1, 2, or 3 return the corresponding value
                if begin == 1:
                    return 0
                elif begin == 2:
                    return 1
                elif begin == 3:
                    return 2
                else:
                    # If the player enters a digit outside of the range, print a
                    # message saying "Invalid input. Please enter a digit between 1 and 3."
                    print("Invalid input. Please enter a digit between 1 and 3.")
                    continue
            # If the player enters a string try to parse it as a command
            elif "shop" in begin.lower():
                return 0
            elif "train" in begin.lower():
                return 1
            elif "fight" in begin.lower():
                return 2
            elif "q" in begin.lower():
                # If the player enters "q" exit the game
                exit()
            else:
                # If the player enters a string that doesn't match any of the above
                # print a message saying "Invalid input."
                print("Invalid input.")
                continue
        except Exception as e:
            # If an error occurs, print a message saying "An error occurred. Please try again."
            # and print the error message
            print("An error occurred. Please try again.")
            print(e)

def home():
    # This function is the main loop of the game, it will continue to run until the player chooses to quit
    while True:            
        # Print a message to the player indicating that they are back to full strength and full health
        print("You are back to full strength and full health.")
        # 
        
        # Call the village_entry function to get the player's choice of what to do
        vil = village_entry()
        # If the player chooses to go to the shop, call the medieval_shop function
        if vil == 0:
            final_shop.medieval_shop()
        # If the player chooses to train, call the training function
        elif vil == 1:
            try:
                # Get the total amount of training points from the character_stats module
                training_points = character_stats.lvl * 3
                # Print a message to the player indicating how many training points they have
                print("You have " + str(training_points) + " training points.")
                # While the player has training points, continue to loop
                while training_points > 0:
                    # Print a list of activities the player can choose from
                    print("You can choose to do the following activities:")
                    print("1 - practice sword fighting (Increase strength by 10)")
                    print("2 - Cardio (Increase dexterity by 10)")
                    print("3 - Meditation (Increase intelligence by 10)")
                    print("4 - Reading (Increase charisma by 10)")
                    print("5 - exit training")
                    # Get the player's choice of activity
                    choice = input("Choose an activity: ")
                    # If the player chooses to practice sword fighting, increase their strength by 10
                    if choice == "1":
                        stats_dict["strength"] += 10
                        print("You gained 10 strength from practice sword fighting.")
                    # If the player chooses to do Cardio, increase their dexterity by 10
                    elif choice == "2":
                        stats_dict["dexterity"] += 10
                        print("You gained 10 dexterity from Cardio.")
                    # If the player chooses to practice Meditation, increase their intelligence by 10
                    elif choice == "3":
                        stats_dict["intelligence"] += 10
                        print("You gained 10 intelligence from Meditation.")
                    # If the player chooses to practice Reading, increase their charisma by 10
                    elif choice == "4":
                        stats_dict["charisma"] += 10
                        print("You gained 10 charisma from Reading.")
                    # If the player chooses to exit training, break out of the loop
                    elif choice == "5":
                        break
                    # If the player enters an invalid choice, print an error message and continue to the next iteration
                    else:
                        print("Invalid input. Please enter a valid number.")
                        continue
                    # Decrement the player's training points by 1
                    training_points -= 1
                    # Print a message to the player indicating how many training points they have left
                    print("You have " + str(training_points) + " training points left.")
                    # If the player has run out of training points, print a message and break out of the loop
                    if training_points == 0:
                        print("You have run out of training points. You can't train anymore today.")
            except Exception as e:
                # If an error occurs, print an error message and continue to the next iteration
                print("An error occurred. Please try again.")
                continue
        # If the player chooses to fight, call the game_loop function
        elif vil == 2:
            try:
                # Initialize a variable to keep track of the number of weapons the player has in their inventory
                weapo = 0
                # Loop until the player has at least one weapon in their inventory
                while True:
                    # Loop through the player's inventory and increment the weapo variable for each weapon found
                    for item in inventory:
                        if item.type == "sword" or item.type == "bow":
                            weapo += 1
                            it = item
                    # If the player has at least one weapon in their inventory, print a message and break out of the loop
                    if weapo >= 1:    
                        print(f"You have an {it.name} in your inventory. Good luck!")
                        print(pyfiglet.figlet_format("Welcome to the Enemy's Village"))
                        # Create a new Player object with the player's name from the stats_dict
                        player = Player(stats_dict["name"])
                        # Call the game_loop function with the player object
                        game_loop(player)
                        break
                    # If the player doesn't have any weapons in their inventory, print a message and remove all items from the player's inventory
                    elif weapo == 0:
                        print("You didn't buy any weapons. You have been refunded your original amount of money and all items have been removed from your inventory.")
                        inventory.clear()
                        # Set the player's coins back to the original amount
                        stats_dict["coins"] = coins
                        # Call the medieval_shop function to let the player buy a weapon
                        final_shop.medieval_shop()
                        break
            
            
            except Exception as e:
                # Print an error message if an exception occurs
                print("An error occurred. Please try again.")
                # Continue to the next iteration of the loop
                continue
        else:
            # Print an error message if the player's choice is invalid
            print("Invalid input. Please enter a valid command.")

        
try:
    # Call the medieval_shop function to let the player buy a weapon
    final_shop.medieval_shop()
    # Call the home function to start the game loop
    home()
except Exception as e:
    # Print an error message if an exception occurs
    print("An error occurred. Please try again.")
