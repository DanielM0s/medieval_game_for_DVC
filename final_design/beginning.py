import character_stats
player = character_stats.stats
class Character:
    def __init__(self):
        self.name = ""
        self.money = 10
        self.health = 100

    def set_stats(self):
        points = 10
        self.name = input("What is your character's name? ")
        print("You have 10 points to spend between your main stats.")
        while points > 0:
            try:
                strength = int(input("Strength (current points: {}): ".format(points)))
                if points - strength < 0:
                    print("Not enough points. You have {} points left.".format(points))
                    continue
                player.strength = strength * 30
                points -= strength

                luck = int(input("Luck (current points: {}): ".format(points)))
                if points - luck < 0:
                    print("Not enough points. You have {} points left.".format(points))
                    continue
                player.coins = luck * 40
                points -= luck

                charisma = int(input("Charisma (current points: {}): ".format(points)))
                if points - charisma < 0:
                    print("Not enough points. You have {} points left.".format(points))
                    continue
                player.charisma = charisma * 20
                points -= charisma

                defense = int(input("Defense (current points: {}): ".format(points)))
                if points - defense < 0:
                    print("Not enough points. You have {} points left.".format(points))
                    continue
                player.defense = defense * 20
                points -= defense

                break  # Exit the loop if all inputs are successful and points are correctly allocated

            except ValueError:
                print("Please enter a valid number.")

    def display_stats(self):
        print(f"Your character name is {self.name}. Your strength is {player.strength}, your luck is {player.coins}, your charisma is {player.charisma}, and your defense is {player.defense}.")

    def set_difficulty(self):
        difficulty = input("Would you like to play easy or hard? ").lower()
        if difficulty not in ['easy', 'hard']:
            print("Invalid difficulty. Please choose 'easy' or 'hard'.")
            self.set_difficulty()

character = Character()
character.set_stats()
character.display_stats()
character.set_difficulty()

