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
        self.sword = fighting.Sword(3)

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

class fighting:
    class Enemy:
        def __init__(self, name):
            self.name = name
            self.health = 100
            self.strength = 40
            self.fortune = 40
            self.sword = fighting.Sword(3)

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

class shop_main:
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
    short_sword = MedievalShopItem("short sword", 50, 3, 20)
    armor = MedievalShopItem("armour", 150, 10)
    longbow = MedievalShopItem("longbow", 710, 0.762, 2)
    food = Food("bread", 2, 0.5, 5)
    bacon = Food("bacon", 10, 0.5, 10)
    cheese = Food("cheese", 5, 0.2, 5)
    egg = Food("egg", 3, 0.1, 2)
    wheat = MedievalShopItem("wheat", 5, 0.5)
    bread_loaf = Food("bread loaf", 10, 0.5, 15)
    apples = Food("apples", 10, 0.5, 10)
    health_potion = MedievalShopItem("health potion", 10, 0.1, 20)

    shop.add_item(short_sword)
    shop.add_item(armor)
    shop.add_item(longbow)
    shop.add_item(food)
    shop.add_item(health_potion)

    coins = 100
    inventory = {}



def main():
    player = Player("Player")
    enemies = []

    for i in range(3):
        enemies.append(fighting.Enemy(f"Enemy {i+1}"))

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
            buy_item(coins, inventory, shop_main.shop)
        elif choice == "2":
            sell_item(coins, inventory, shop_main.shop)
        elif choice == "3":
            upgrade_inventory(coins, inventory, shop_main.shop)
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




player = Player("player")
player.set_stats()
player.display_stats()
player.set_difficulty()
medieval_shop()
if __name__ == "__main__":
    main()