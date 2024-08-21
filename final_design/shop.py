import random
from character_stats import stats_dict, inventory
# Define the MedievalShop class
class MedievalShop:
    """
    A class representing a medieval shop.
    """
    def __init__(self, name):
        self.name = name
        self.items = []

    def start_shop(self):
        """
        Prints a welcome message to the shop.
        """
        print(f"Welcome to the {self.name}!")

    def add_item(self, item):
        """
        Adds an item to the shop's inventory.
        """
        self.items.append(item)

    def get_item_price(self, item_name):
        """
        Returns the price of an item in the shop's inventory.
        """
        for item in self.items:
            if item.name == item_name:
                return item.price

    def get_random_item(self):
        """
        Returns a random item from the shop's inventory.
        """
        if self.items:
            return random.choice(self.items)
        else:
            return None


# Define the MedievalShopItem class
class MedievalShopItem:
    """
    A class representing an item that can be bought in the shop.
    """
    def __init__(self, name, price, weight, length=None, draw_length=None, max_draw_force=None):
        self.name = name
        self.price = price
        self.weight = weight
        self.length = length
        self.draw_length = draw_length
        self.max_draw_force = max_draw_force

    def __str__(self):
        """
        Returns a string representation of the item.
        """
        return f"{self.name}: {self.price} coins, {self.weight} lbs, {self.length} cm"
    
    # Define the Food class, which is a subclass of MedievalShopItem
class Food(MedievalShopItem):
    def __init__(self, name, price, weight, health_increase):
        super().__init__(name, price, weight)
        self.health_increase = health_increase

    def increase_health(self, player):
        """
        Increases the player's health by the amount specified in the food item.
        """
        player["health"] += self.health_increase

class Sword(MedievalShopItem):
    def __init__(self, name, price, weight, length):
        super().__init__(name, price, weight, length)

class Bow(MedievalShopItem):
    def __init__(self, name, price, weight, draw_length, max_draw_force):
        super().__init__(name, price, weight, draw_length, max_draw_force)
class Arrow(MedievalShopItem):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)
# Create instances of the classes
items = {
    "Ilkwa": {"price": 50, "weight": 3, "length": 3, "type": "sword"},
    "armour": {"price": 150, "weight": 10, "protection": 10, "type": "armour"},
    "Bow": {"price": 50, "weight": 13.6, "draw length": 76, "max draw force": 710, "type": "bow"},
    "arrow x10": {"price": 10, "weight": 0.1, "type": "arrow"},
    "bread": {"price": 2, "weight": 0.5, "health_increase": 5, "type": "food"},
    "pap": {"price": 10, "weight": 0.5, "health_increase": 30, "type": "food"},
    "wild meat": {"price": 5, "weight": 0.2, "health_increase": 5, "type": "food"},
    "egg": {"price": 3, "weight": 0.1, "health_increase": 2, "type": "food"},
    "wheat": {"price": 5, "weight": 0.5, "type": "ingrediant"},
    "bread loaf": {"price": 10, "weight": 0.5, "health_increase": 15, "type": "food"},
    "apples": {"price": 10, "weight": 0.5, "health_increase": 10, "type": "food"},
    "health potion": {"price": 10, "weight": 0.1, "health_increase": 20, "type": "food"},
}

shop = MedievalShop("The Medieval Shop")
for name, item_info in items.items():
    item_type = item_info.get("type")
    if item_type == "food":
        food_item = Food(name, item_info["price"], item_info["weight"], item_info["health_increase"])
        shop.add_item(food_item)
    elif item_type == "sword":
        sword_item = Sword(name, item_info["price"], item_info["weight"], item_info.get("length"))
        shop.add_item(sword_item)
    elif item_type == "bow":
        bow_item = Bow(name, item_info["price"], item_info["weight"], item_info.get("draw length"), item_info.get("max draw force"))
        shop.add_item(bow_item)
    elif item_type == "arrow":
        arrow_item = Arrow(name, item_info["price"], item_info["weight"])
        shop.add_item(arrow_item)
    else:
        shop_item = MedievalShopItem(name, item_info["price"], item_info["weight"])
        shop.add_item(shop_item)



# Define the medieval_shop function

def medieval_shop():
    while True:
        print("-------------------------------------")
        print("Welcome to the medieval shop!")
        print(f"You have {stats_dict['coins']} coins.")
        print("-------------------------------------")
        print("What would you like to do?")
        print("1. Buy an item")
        print("2. Sell an item")
        print("3. Upgrade your inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            buy_item(stats_dict["coins"], inventory, shop)
        elif choice == "2":
            sell_item(stats_dict["coins"], inventory, shop)
        elif choice == "3":
            upgrade_inventory(stats_dict["coins"], inventory, shop)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Define the buy_item function
def buy_item(coins, inventory, shop):
    print("Which item would you like to buy?")
    for i, item in enumerate(shop.items):
        print(f"{i+1}. {item.name}: {item.price} coins")
    try:
        choice = int(input("Enter the number of the item you want: ")) - 1
        if 0 <= choice < len(shop.items):
            item = shop.items[choice]
            price = shop.get_item_price(item.name)
            print(f"You found a {item.name}!")
            print(f"Price: {price} coins")
            if item.price <= coins:
                answer = input(f"Do you want to buy the {item.name} for {price} coins? (y/n) ")
                if answer.lower() == "y":
                    coins -= price
                    if item.name not in [i.name for i in inventory]:
                        inventory.append(item)
                        for key, value in item.__dict__.items():
                            stats_dict[key] = value
                    print(f"You bought the {item.name}!")
                    print(f"You have {coins} coins left.")
                    stats_dict["coins"] = coins
            else:
                print("You do not have enough money for that item.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")


# Define the sell_item function
def sell_item(coins, inventory, shop):
    print("You have the following items:")
    for i, (item, quantity) in enumerate(inventory.items(), start=1):
        print(f"{i}. {item}: {shop.get_item_price(item)} coins")
    try:
        choice = int(input("Enter the number of the item you want to sell: ")) - 1
        if 0 <= choice < len(inventory):
            item_name = list(inventory.keys())[choice]
            price = shop.get_item_price(item_name)
            if price:
                coins += price
                inventory[item_name] -= 1
                if inventory[item_name] == 0:
                    del inventory[item_name]
                print(f"You sold the {item_name}!")
                print(f"You have {coins} coins now.")
                stats_dict["coins"] = coins
        else:
            print("Invalid choice.")
    except Exception as e:
        print("Invalid choice.")


# Define the upgrade_inventory function
def upgrade_inventory(coins, inventory, shop):
    try:
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
    except Exception as e:
        print("Invalid choice.")



# medieval_shop()



