import random
import math

class Player:
    def __init__(self, name: str):
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
        self.name = input("what is your character's name? ")
        print("you have 10 points to spend between your main stats. choose between strength, luck, charisma and defense: ")
        self.strength = int(input("strength: "))
        self.strength * 20
        points -= self.strength
        if points < 0:
            print("you do not have enough points to set up your character")
            exit()
        self.fortune = int(input("luck: "))
        self.fortune * 20
        points -= self.fortune
        if points < 0:
            print("you do not have enough points to set up your character")
            exit()
        self.charisma = int(input("charisma: "))
        self.charisma * 20
        points -= self.charisma
        if points < 0:
            print("you do not have enough points to set up your character")
            exit()
        self.defense = int(input("defense: "))
        self.defense * 20
        points -= self.defense
        if points < 0:
            print("you do not have enough points to set up your character")
            exit()

    def display_stats(self):
        print(f"your character name is {self.name} your strength is {self.strength} your luck is {self.fortune} your charisma is {self.charisma} your defense is {self.defense}")

    def set_difficulty(self):
        difficulty = input("would you like to play easy or hard? ").lower()
        if difficulty == "easy":
            self.fortune += 20
        elif difficulty == "hard":
            self.fortune -= 20
        else:
            print("Invalid input")

class Enemy:
    def __init__(self, name, height, distance):
        self.name = name
        self.health = 100
        self.strength = 10
        self.fortune = 10
        self.sword = Sword(3)
        self.height = height
        self.distance = distance
        

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


def fighting_main():
    player = Player("Player")
    enemies = []

    for i in range(3):
        enemies.append(Enemy(f"Enemy {i+1}", 2.5, random.randint(300, 400)))

    while True:
        if not player.check_health():
            break
        if not enemies:
            break
        for i, enemy in enumerate(enemies):
            print(f"{i+1}. {enemy.name}")
        try:
            target = int(input("Which enemy do you want to attack? "))
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

class Arrow:
    def __init__(self, weight):
        self.weight = weight


class Bow:
    def __init__(self, name, max_pull_force, max_pull_distance):
        self.name = name
        self.max_pull_force = max_pull_force
        self.max_pull_distance = max_pull_distance





class Archer:
    def __init__(self, bow, arrow, enemy, health):
        self.bow = bow
        self.arrow = arrow
        self.enemy = enemy
        self.health = health

    def safe_sqrt(self, number):
        if number >= 0:
            return math.sqrt(number)
        else:
            return None

    def safe_calculate(self, force, length, weight, angle, ed):
        try:
            X = length / 100
            k = force / X
            ep = k / 2
            ep = ep * pow(X, 2)
            vi = 2 * ep / weight
            vi = self.safe_sqrt(vi)
            vix = vi * math.cos(math.radians(angle))
            viy = vi * math.sin(math.radians(angle))
            t = -vix
            t = t / -9.8
            t = t * 2
            d = vix * t
            t = ed / viy
            h = viy * t + -4.9 * pow(t, 2)
            return h
        except (ValueError, ZeroDivisionError):
            return None

    def plot_results(self, distance, height):
        try:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()

            # Plot the figure movement
            ax.plot(distance, height, color='blue', marker='o')
            # Set up the x-axis
            ax.set_xlabel('Distance (m)')
            ax.set_xlim(0, max(distance))
            # Set up the y-axis
            ax.set_ylabel('Height (m)')
            ax.set_ylim(0, max(height))

            # Set up the grid
            ax.grid(True, linestyle='dashed', linewidth=0.5, color='gray', alpha=0.7)

            # Show the plot
            plt.show()
        except Exception:
            pass

    def attack(self):
        while True:
            try:
                print(f"Enemy distance: {self.enemy.distance} Enemy height: {self.enemy.height}")
                hint = input("would you like to activate hints? y/n ")
                if hint.lower() == "y":
                    print("hint: the pull force is the force that makes the string pull back")
                    hint2 = input("would you like another hint? y/n ")
                    if hint2.lower() == "y":
                        print("hint: the maximum pull force is 710N, and the minimum pull force is 400N")
                force = int(input("how much force do you want to apply?"))
                if not 400 < force < 710:
                    print("Invalid force value")
                    continue
                if hint.lower() == "y":
                    print("hint: the maximum pull distance is 76cm")
                length = int(input("how far do you pull the string back in cm? "))
                if length > 76:
                    print("Your string snaps, you now need to replace it. Next time don't pull it back too far")
                    break
                if hint.lower() == "y":
                    print("hint: the maximum angle is 90 degrees")
                angle = int(input("what angle do you want to shoot the arrow? "))
                if angle > 90:
                    print("your arrow flies straight up into the sky. It then hits you. You take 10 damage")
                    self.health -= 10
                height_of_arrow = [self.safe_calculate(force, length, self.arrow.weight, angle, dist) for dist in range(1, int(self.enemy.distance) + 1)]
                self.plot_results(range(1, int(self.enemy.distance) + 1), height_of_arrow)
                final_height = height_of_arrow[-1]
                if final_height > 0:
                    print(f"you arrow went {round((final_height - self.enemy.height), 1)} meters higher than the enemy")
                elif final_height < 0:
                    print("you did not apply enough force, your arrow did not reach the enemy")
                if final_height is not None and final_height >= 0 and final_height < self.enemy.height:
                    print("your arrow hits the enemy")
                else:
                    print("your arrow misses the enemy")
                contin = input("do you want to continue? y/n ")
                if contin.lower() != "y":
                    break
            except Exception:
                pass



class MedievalShop:
    """
    A class representing a medieval shop.
    """
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_item_price(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item.price
        return None

    def get_random_item(self):
        return random.choice(self.items)


class MedievalShopItem:
    """
    A class representing an item that can be bought in the shop.
    """
    def __init__(self, name, price, weight, length=None):
        self.name = name
        self.price = price
        self.weight = weight
        self.length = length

    def __str__(self):
        return f"{self.name}: {self.price} coins, {self.weight} lbs, {self.length} cm"
    
class Food(MedievalShopItem):
    def __init__(self, name, price, weight, health_increase):
        super().__init__(name, price, weight)
        self.health_increase = health_increase

    def increase_health(self, player):
        player["health"] += self.health_increase

shop = MedievalShop("The Medieval Shop")
sword = MedievalShopItem("sword", 50, 3, 80)
armor = MedievalShopItem("armour", 150, 10)
longbow = MedievalShopItem("longbow", 50, 3, 80)
food = Food("bread", 2, 0.5, 5)
bacon = Food("bacon", 10, 0.5, 10)
cheese = Food("cheese", 5, 0.2, 5)
egg = Food("egg", 3, 0.1, 2)
wheat = MedievalShopItem("wheat", 5, 0.5)
bread_loaf = Food("bread loaf", 10, 0.5, 15)
apples = Food("apples", 10, 0.5, 10)
health_potion = MedievalShopItem("health potion", 10, 0.1, 20)

shop.add_item(sword)
shop.add_item(armor)
shop.add_item(longbow)
shop.add_item(food)
shop.add_item(health_potion)

coins = 100
inventory = {}

def medieval_shop():
    inventory = {}
    coins = 100

    while True:
        print("-------------------------------------")
        print("Welcome to the medieval shop!")
        print(f"You have {coins} coins.")
        print("-------------------------------------")
        print("What would you like to do?")
        print("1. Buy an item")
        print("2. Sell an item")
        print("3. Upgrade your inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            buy_item(coins, inventory, shop)
        elif choice == "2":
            sell_item(coins, inventory, shop)
        elif choice == "3":
            upgrade_inventory(coins, inventory, shop)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


def buy_item(coins, inventory, shop):
    print("Which item would you like to buy?")
    item_names = [item.name for item in shop.items]
    for i, item_name in enumerate(item_names):
        print(f"{i+1}. {item_name}")
    choice = int(input("Enter the number of the item you want: ")) - 1
    if choice < 0 or choice >= len(shop.items):
        print("Invalid choice.")
    else:
        item = shop.items[choice]
        print(f"You found a {item.name}!")
        print(f"Price: {item.price} coins")
        if item.price <= coins:
            answer = input(f"Do you want to buy the {item.name} for {item.price} coins? (y/n) ")
            if answer.lower() == "y":
                coins -= item.price
                if item.name not in inventory:
                    inventory[item.name] = 0
                inventory[item.name] += 1
                print(f"You bought the {item.name}!")
                print(f"You have {coins} coins left.")
        else:
            print("You do not have enough money for that item.")


def sell_item(coins, inventory, shop):
    item_name = input("What item would you like to sell? ")
    if item_name in inventory:
        price = shop.get_item_price(item_name)
        if price:
            coins += price
            inventory[item_name] -= 1
            if inventory[item_name] == 0:
                del inventory[item_name]
            print(f"You sold the {item_name}!")
            print(f"You have {coins} coins now.")
        else:
            print("We do not sell that item.")
    else:
        print("You do not have that item.")


def upgrade_inventory(coins, inventory, shop):
    for item in inventory:
        item_quantity = inventory[item]
        item_price = shop.get_item_price(item)
        if item_price:
            inventory[item] = int(inventory[item] * 1.5)
            coins -= item_price * item_quantity
            print(f"You upgraded all your {item}s!")
            print(f"You now have {inventory[item]} {item}s.")
            print(f"You have {coins} coins left.")
    else:
        print("You do not have any items to upgrade.")
contin = True
while contin == True:
    choose = input("what would you like to do? ")
    if choose == "1":  
        bow = Bow("long Bow", 710, 0.762)
        arrow = Arrow(0.1)
        enemy_a = Enemy("enemy", 2.5, random.randint(300, 400))
        archer = Archer(bow, arrow, enemy_a, 100)
        archer.attack()
    elif choose == "2":
        player = Player("Player")
        player.set_stats()
        player.display_stats()
        player.set_difficulty()
    elif choose == "3":
        fighting_main()
    elif choose == "4":
        medieval_shop()
    contin = input("would you like to continue? ")
    if contin == "n":
        break
    elif contin == "y":
        contin = True