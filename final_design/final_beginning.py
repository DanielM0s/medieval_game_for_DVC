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
                for stat in main_stats:
                    print(stat)
                stat = input("Choose a stat to allocate points to: ")
                if stat in main_stats:
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
                print(f"{stat} now has {stats_dict[stat]}")
                print(f"You have {stats_dict['points']} points left.")
                if stats_dict["points"] == 0:
                    break
                elif stats_dict["points"] < 0:
                    print("you have exceeded your allocated points please try again")
                    stats_dict["points"] = 20
                    stats_dict[stat] = stats_dict[stat] - value
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid statistic.")
                value = None
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
            encounter_chance = base_probability + (self.level * 0.1)
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


global train_points

def game_loop(player):
    while True:
        print(f"\nYou are at: {player.location.name}")
        print(player.location.description)
        print("Options:")
        for i, location in enumerate(player.location.connections):
            print(f"{i + 1}. Go to {location.name}")
        print("Q. Quit")

        choice = input("Enter your choice: ").strip().lower()
        if choice == 'q':
            print("Thanks for playing!")
            break
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(player.location.connections):
                new_location = player.location.connections[choice - 1]
                if new_location == village:
                    player.location = new_location
                    train_points = character_stats.lvl * 2
                    return home()
                
                else:
                    player.move(new_location)
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please try again.")

def fight_flight():
    while True:
        try:
            fighting = input("You are spotted by a group of enemy soldiers! You can either 1. Fight them, 2. sneak past them, or 3. run away.")
            if fighting.isdigit():
                fighting = int(fighting)
                if fighting == 1:
                    return 1
                elif fighting == 2:
                    return 2
                elif fighting == 3:
                    return 3
                else:
                    print("Invalid input. Please enter a digit between 1 and 3.")
                    continue
            elif "fight" in fighting.lower():
                return 1
            elif "sneak" in fighting.lower():
                return 2
            elif "run" in fighting.lower():
                return 3
            elif "q" in fighting.lower():
                exit()
            else:
                print("Invalid input.")
                continue
        except Exception as e:
            print("An error occurred. Please try again.")
            print(e)

def encounter_soldiers(player):
    try:
        from enemy_stats import enemy_dict
        number_of_enemies = random.randint(character_stats.lvl*1, character_stats.lvl*3)
        enemy_dict.update(enemy_stats.new_enemy(number_of_enemies))

        fighting = fight_flight()                
        if fighting == 1:
            print("You have the following weapons in your inventory:")
            sword_list = [item for item in inventory if item.type == "sword"]
            bow_list = [item for item in inventory if item.type == "bow"]
            if not sword_list and not bow_list:
                print("You need a sword or bow to fight")
                return encounter_soldiers(player)
            for i, item in enumerate(sword_list, 1):
                print(f"{i}. {item.name}")
            for i, item in enumerate(bow_list, 1+len(sword_list)):
                print(f"{i}. {item.name}")
            try:
                choice = int(input("Which weapon would you like to use? (Enter the number) "))
                if 1 <= choice <= len(inventory):
                    chosen_weapon = inventory[choice - 1]
                    if chosen_weapon.type == "sword":
                        print(f"You have chosen to use your {chosen_weapon.name}. Good luck!")
                        print(f"You draw your {chosen_weapon.name} and prepare to fight. The enemy soldiers charge at you. You swing your sword and prepare to face them.")
                        from fighting_final import fight
                        fight()             
                    elif chosen_weapon.type == "bow":
                        print("You have chosen to use your Bow. Good luck!")
                        hints = input("would you like to activate hints? y/n ")
                        import bow_calculator
                        from bow_calculator import archer_fight
                        archer_fight()
                else:
                    print("Invalid input. Please enter a number of a sword or bow in your inventory.")
                    return encounter_soldiers(player)
            except ValueError:
                print("Invalid input. Please enter a number.")
                return encounter_soldiers(player)
        elif fighting == 2:
            sneak =random.randint(1, stats_dict["dexterity"])
            if sneak >= 5:
                print("You successfully sneak past the enemy soldiers.")
                game_loop(player)
            else:
                print("You failed to sneak past the enemy soldiers. You now have to fight them.")
                return encounter_soldiers(player)
        elif fighting == 3:
            print("You turn around and run away. You manage to escape the enemy village.")
            village_entry()
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
print("\033[36;1m" + "{:^80}".format(pyfiglet.figlet_format("Rise of Shaka Zulu", font='slant', justify='center')) + "\033[0m")
print("""
================================================================================
""")

stats_dict["name"] = input("What is your character's name? ")

        
print(f"""
In the heart of Zululand, a young boy named {stats_dict["name"]} lived a peaceful life in his village, surrounded by the warmth of his family and the strength of his community. His father, a respected warrior, taught him the ways of the Zulu, instilling in him the values of honor, courage, and loyalty.

One fateful night, the tranquility of {stats_dict["name"]}'s village was shattered by the fierce attack of a neighboring tribe. Flames engulfed the huts, and the air was filled with the cries of his people. Amidst the chaos, {stats_dict["name"]} witnessed the brutal slaying of his father by the chieftain of the rival clan. The once vibrant village was left in ruins, and {stats_dict["name"]}'s world was turned upside down.

With nothing left but the memories of his fallen family and the burning desire for justice, {stats_dict["name"]} vowed to restore his honor and avenge his father's death. He embarked on a perilous journey, determined to become a warrior worthy of his father's legacy. Along the way, he would face numerous challenges, forge alliances, and uncover the secrets of his heritage.

In "Rise of Shaka Zulu," players will guide {stats_dict["name"]} through his journey, making critical decisions that will shape his destiny. Will he become the hero his people need, or will the path of vengeance consume him? The fate of Zululand rests in your hands.
""")


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
    points = stats_dict["points"]
    if points <= 0:
        print("You have spent all your points.")
        points = 20
        for stat in stats_dict:
            if all(isinstance(stats_dict[stat], int) and stats_dict[stat] > 0 for stat in main_stats):
                points = 0
                total = sum([stats_dict[stat] for stat in main_stats])
                if total != 20:
                    if total < 20:
                        print("You have used less than 20 points. Please try again.")
                    elif total > 20:
                        print("You have used more than 20 points. Please try again.")
                    return False
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
while True:
    try:
        while True:
            print(f"First off, you need to choose your stats. You have {stats_dict['points']} points to spend between your main stats. Choose between coins, strength, dexterity, constitution, intelligence, wisdom, and charisma. Choose wisely.")
            main_stats = ["coins", "strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
            stat_index = 0
            while stat_index < len(main_stats):
                stat = main_stats[stat_index]
                value = None
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
                stats_dict["points"] = minus_points(stats_dict["points"], value)
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
        for stat in stats_dict:
            if isinstance(stats_dict[stat], int):
                stats_dict[stat] *= 30
        display_stats()
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
print("Next you need to choose your weapons. You should have enough money to buy at least one weapon, choose between meele weapons and ranged weapons depending on how you want to attack your enemies, but remember to buy arrows for your ranges weapon, especially if you don't have a meele weapon, because when you run out of arrows you need to find a way to escape, or use your meele weapon, but remember to buy food as well, as it provides you with health. If you don't have enough money to buy what you want now don't worry, you can loot your enemies after you have defeated them. ")
guide = input("would you like to see the weapon guide? (recommended for beginners): ")
if guide.lower() == "y":
    weapons = [
        ("\033[31mIlkwa\033[0m", "a spear that was originally introduced by Shaka Zulu, because when they fought in his father's time they would throw their spears at each other, then use each other's spears until they were out of spears, but by using the short spear, they would hold onto there weapons", 0.9),
        ("\033[32mAssegai\033[0m", "a light throwing-spear used in both hunting and war, typically around 1.8 meters long with a 15.2 centimeter long steel head", 1.8),
        ("\033[33mKnobkerrie\033[0m", "A Knobkerrie is a strong, short wooden club with a heavy rounded knob or head on one end, traditionally used by Southern AfricanTribes including the Zulu, as a weapon in warfare. The word Knobkerrie derives from the Dutch knop (knob), and the Bushman and Hottentot kerrie (stick).The weapon is employed at close quarters, or as a throwing club. The knobkerrie was emblematic of the Zulu people. A man always carried one, a custom which has not yet disappeared in rural areas. Made of heavy wood, it was an effective weapon, and when you use it your damage is multiplied by 2", 0.5)
        
    ]
    print(" ", end='')
    print("In physics you calculate force on a lever by multiplying the force applied at the bottom by the length of the object. A sword is affectively a lever, so when picking your weapon pay careful attention to it's length, the longer the weapon the more damage you will deal to your enemies.")
    print(" ", end='')
    for i, weapon in enumerate(weapons):
        for letter in weapon[0]:
            print(letter, end='', flush=True)
            time.sleep(0.05)
        print(": ", end='', flush=True)
        time.sleep(0.1)
        for letter in weapon[1]:
            print(letter, end='', flush=True)
            time.sleep(0.01)
        print(". The ", end='', flush=True)
        time.sleep(0.05)
        print(weapon[0], end='', flush=True)
        time.sleep(0.05)
        print(" has a length of ", end='', flush=True)
        time.sleep(0.05)
        print(str(weapon[2])+" meters", end='', flush=True)
        time.sleep(0.05)
        if i != len(weapons) - 1:
            print('\n')
        else:
            print("")
else:
    print("Ok. Good luck!")

def village_entry():
    while True:
        try:
            begin = input("You start in the ruins of your home town. You can choose to 1. go to shop, 2. train, 3. fight, or Q to quit. What would you like to do? ")
            if begin.isdigit():
                begin = int(begin)
                if begin == 1:
                    return 0
                elif begin == 2:
                    return 1
                elif begin == 3:
                    return 2
                else:
                    print("Invalid input. Please enter a digit between 1 and 3.")
                    continue
            elif "shop" in begin.lower():
                return 0
            elif "train" in begin.lower():
                return 1
            elif "fight" in begin.lower():
                return 2
            elif "q" in begin.lower():
                exit()
            else:
                print("Invalid input.")
                continue
        except Exception as e:
            print("An error occurred. Please try again.")
            print(e)

def home():
    while True:            
        print("you are back to full strength and full health.")
        vil = village_entry()
        if vil == 0:
            final_shop.medieval_shop()
        elif vil == 1:
            try:
                training_points = character_stats.lvl * 3
                print("You have " + str(training_points) + " training points.")
                while training_points > 0:
                    print("You can choose to do the following activities:")
                    print("1 - practice sword fighting (Increase strength by 10)")
                    print("2 - Cardio (Increase dexterity by 10)")
                    print("3 - Meditation (Increase intelligence by 10)")
                    print("4 - Reading (Increase charisma by 10)")
                    print("5 - exit training")
                    choice = input("Choose an activity: ")
                    if choice == "1":
                        stats_dict["strength"] = int(stats_dict["strength"]) + 10
                        print("You gained 10 strength from practice sword fighting.")
                    elif choice == "2":
                        stats_dict["dexterity"] = int(stats_dict["dexterity"]) + 10
                        print("You gained 10 dexterity from Cardio.")
                    elif choice == "3":
                        stats_dict["intelligence"] = int(stats_dict["intellignece"]) + 10
                        print("You gained 10 intelligence from Meditation.")
                    elif choice == "4":
                        stats_dict["charisma"] = int(stats_dict["charisma"]) + 10
                        print("You gained 10 charisma from Reading.")
                    elif choice == "5":
                        break
                    else:
                        print("Invalid input. Please enter a valid number.")
                        continue
                    training_points -= 1
                    print("You have " + str(training_points) + " training points left.")
                    if training_points == 0:
                        print("You have run out of training points. You can't train anymore today.")
            except Exception as e:
                print("An error occurred. Please try again.")
                continue
        elif vil == 2:
            try:
                for item in inventory:
                    if item.type == "sword" or item.type == "bow":
                        print(f"You have a {item}. Good luck!")
                        print(pyfiglet.figlet_format("Welcome to the Enemy's Village"))
                        player = Player(stats_dict["name"])
                        game_loop(player)
                        break
                    else:
                        print("You didn't buy any weapons. You have been refunded your original amount of money and all items have been removed from your inventory.")
                        inventory.clear()
                        stats_dict["coins"] = coins
                        break
                
            except Exception as e:
                print("An error occurred. Please try again.")
                continue
        else:
            print("Invalid input. Please enter a valid command.")

        
try:
    final_shop.medieval_shop()
    home()
except Exception as e:
    print("An error occurred. Please try again.")