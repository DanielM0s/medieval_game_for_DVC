import random
class Player:
    def __init__(self, name):
        self.name = ""
        self.money = 10
        self.health = 100
        self.strength = 0
        self.defense = 0
        self.fortune = 0
        self.charisma = 0
        self.sword = Sword(3)

    def attack(self, force):
        damage = force * self.sword.length
        self.strength -= force
        return damage

    def counter_attack(self, force):
        damage = force * self.sword.length
        self.strength -= damage
        return damage

    def check_health(self):
        if self.health <= 0:
            return False
        return True
    def set_stats(self):
        points = 10
        name = input("what is your character's name? ")
        self.name = name
        print("you have 10 points to spend between your main stats. choose between strength, luck, charisma and defense: ")
        strength = input("strength: ")
        self.strength = int(strength)
        points = points - self.strength
        print(points)
        if points < 0:
            print("you do not have enough points to set up your character")
            print("please try again")
            exit()
        luck = input("luck: ")
        self.fortune = int(luck)
        points = points - self.fortune
        print(points)
        if points < 0:
            print("you do not have enough points to set up your character")
            print("please try again")
            exit()
        charisma = input("charisma: ")
        self.charisma = int(charisma)
        points = points - self.charisma
        print(points)
        if points < 0:
            print("you do not have enough points to set up your character")
            print("please try again")
            exit()
        defense = input("defense: ")
        self.defense = int(defense)
        points = points - self.defense
        print(points)
        if points < 0:
            print("you do not have enough points to set up your character")
            print("please try again")
            exit()

    def display_stats(self):
        print(f"your character name is {self.name} your strength is {self.strength} your luck is {self.fortune} your charisma is {self.charisma} your defense is {self.defense}")

    def set_difficulty(self):
        difficulty = input("would you like to play easy or hard? ")

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 40
        self.fortune = 40
        self.sword = Sword(3)

    def attack(self, force):
        damage = force * self.sword.length
        self.strength -= force
        return damage
    
    def check_health(self):
        if self.health <= 0:
            return False
        return True

    def end_turn(self):
        self.strength = 0

class Sword:
    def __init__(self, length):
        self.length = length





def main():
    player = Player("Player")
    enemies = []

    for i in range(3):
        enemies.append(Enemy(f"Enemy {i+1}"))

    while True:
        if not player.check_health():
            break
        if not enemies:
            break
        for i, enemy in enumerate(enemies):
            print(f"{i+1}. {enemy.name}")
        try:
            target = int(input("Which enemy do you want to attack? ")) - 1
            if target < 0 or target >= len(enemies):
                print("Invalid input")
                continue
            enemy = enemies[target]
        except ValueError:
            print("Invalid input")
            continue
        while enemy.check_health():
            while True:
                if not enemy.check_health():
                    break
                attack_types = {
                    "1": "Slash",
                    "2": "Stab",
                    "3": "Chop",
                    "4": "Counter",
                    "5": "Block",
                    "6": "Parry",
                    "7": "Riposte",
                    "8": "Feint"
                }
                print("\n".join(f"{key}. {value}" for key, value in attack_types.items()))
                attack = input(f"What type of attack do you want to use against {enemy.name}? ")
                if attack in attack_types:
                    try:
                        force = int(input(f"How much force do you want to hit {enemy.name} with? "), base=0)
                    except ValueError:
                        print("Invalid input")
                        continue
                    if force < 0:
                        print("You do not have any strength left")
                    elif force > player.strength:
                        print("You do not have enough strength to hit the enemy with that force")
                    else:
                        try:
                            chance_of_block_enemy = random.randint(1, enemy.fortune)
                            enemyblock = enemy.attack(random.randint(1, enemy.strength))
                            if chance_of_block_enemy < 30:
                                enemy.health -= player.attack(force)
                                print(f"You hit {enemy.name} for {player.attack(force)} damage, {enemy.name} has {enemy.health} health left")
                            elif chance_of_block_enemy > 30:
                                if enemyblock < force:
                                    enemy.health -= player.attack(force)
                                    print(f"You hit {enemy.name} for {player.attack(force)} damage, {enemy.name} has {enemy.health} health left")
                                elif enemyblock > force:
                                    print(f"{enemy.name} blocks the attack")
                        except ValueError:
                            print("Invalid input")
                            continue
                else:
                    print("Invalid attack type")
                if enemy.health <= 0:
                    enemies.remove(enemy)
                    print("You defeated the enemy, next enemy coming up...")
                    break
                try:
                    chance_of_block_player = random.randint(1, player.fortune)
                    enemydamage = enemy.attack(random.randint(1, enemy.strength))
                    if chance_of_block_player < 30:
                        print(f"{enemy.name} hits you for {enemydamage} damage")
                    elif chance_of_block_player > 30:
                        counter = input(f"{enemy.name} attempts to block your attack, you have the chance to defend yourself, do you want to block or counter attack? ")
                        if counter.lower() == "block":
                            try:
                                blockdamage = int(input("How much damage do you want to block with? "))
                            except ValueError:
                                print("Invalid input")
                                continue
                            if blockdamage < enemydamage:
                                print("You do not block the attack")
                                player.health -= enemydamage
                                print(f"{enemy.name} hit you for {enemydamage} damage, you have {player.health} health left")
                            elif blockdamage > enemydamage:
                                print("You successfully block the attack")
                        elif counter.lower() == "counter":
                            try:
                                counterdamage = int(input("How much damage do you want to counter with? "))
                            except ValueError:
                                print("Invalid input")
                                continue
                            if counterdamage < enemydamage:
                                print("You do not counter the attack")
                                player.health -= enemydamage
                                print(f"{enemy.name} hit you for {enemydamage} damage, you have {player.health} health left")
                            elif counterdamage > enemydamage:
                                print("You successfully counter the attack")
                                enemy.health -= counterdamage
                        else:
                            print("Please type 'block' or 'counter'")
                except ValueError:
                    print("Invalid input")
            if player.health <= 0:
                print("You died")
                break
            enemy.end_turn()

player = Player("player")
player.set_stats()
player.display_stats()
player.set_difficulty()
if __name__ == "__main__":
    main()