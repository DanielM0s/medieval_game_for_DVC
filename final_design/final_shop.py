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
    def get_item_type(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item.type

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
    def __init__(self, name, price, weight, type, length=None, draw_length=None, max_draw_force=None):
        self.name = name
        self.price = price
        self.weight = weight
        self.length = length
        self.draw_length = draw_length
        self.max_draw_force = max_draw_force
        self.type = type

    def __str__(self):
        """
        Returns a string representation of the item.
        """
        return f"{self.name}: {self.price} coins, {self.weight} lbs, {self.length} cm"
    
    # Define the Food class, which is a subclass of MedievalShopItem
class Food(MedievalShopItem):
    def __init__(self, name, price, weight, health_increase, strength_increase, type):
        super().__init__(name, price, weight, type)
        self.health_increase = health_increase
        self.strength_increase = strength_increase

    def increase_health(self, player):
        """
        Increases the player's health by the amount specified in the food item.
        """
        player["health"] += self.health_increase

    def increase_strength(self, player):
        """
        Increases the player's strength by the amount specified in the food item.
        """
        player["strength"] += self.strength_increase

class Sword(MedievalShopItem):
    def __init__(self, name, price, weight, type, length):
        super().__init__(name, price, weight, type, length)

class Bow(MedievalShopItem):
    def __init__(self, name, price, weight, type, draw_length, max_draw_force):
        super().__init__(name, price, weight, type, draw_length, max_draw_force)
class Arrow(MedievalShopItem):
    def __init__(self, name, price, weight, type):
        super().__init__(name, price, weight, type)
# Create instances of the classes
items = {
    "Ilkwa (short spear)": {"price": 50, "weight": 3, "length": 0.9, "type": "sword"},
    "Assegai (spear)": {"price": 100, "weight": 0.5, "length": 1.97, "type": "sword"},
    "Knobkerrie (club)": {"price": 150, "weight": 5, "length": 0.52, "type": "sword"},
    "isihlangu (shield)": {"price": 20, "weight": 5, "protection": 5, "type": "shield"},
    "armour": {"price": 150, "weight": 10, "protection": 10, "type": "shield"},
    "Bow": {"price": 50, "weight": 13.6, "draw length": 76, "max draw force": 710, "type": "bow"},
    "arrow x10": {"price": 10, "weight": 0.1, "type": "arrow"},
    "mielie bread": {"price": 2, "weight": 0.5, "health_increase": 5, "strength_increase": 30, "type": "food"},
    "pap": {"price": 30, "weight": 0.5, "health_increase": 30, "strength_increase": 300, "type": "food"},
    "droeworse": {"price": 5, "weight": 0.2, "health_increase": 5, "strength_increase": 100, "type": "food"},
    "egg": {"price": 3, "weight": 0.1, "health_increase": 2, "strength_increase": 20, "type": "food"},
    "rusk": {"price": 10, "weight": 0.5, "health_increase": 15, "strength_increase": 40, "type": "food"},
    "apples": {"price": 10, "weight": 0.5, "health_increase": 10, "strength_increase": 20, "type": "food"},
}

shop = MedievalShop("The Medieval Shop")
for name, item_info in items.items():
    item_type = item_info.get("type")
    if item_type == "food":
        food_item = Food(name, item_info["price"], item_info["weight"], item_info["health_increase"], item_info["strength_increase"], item_info.get("type"))
        shop.add_item(food_item)
    elif item_type == "shield":
        shield_item = MedievalShopItem(name, item_info["price"], item_info["weight"], item_info["protection"], item_info.get("type"))
    elif item_type == "sword":
        sword_item = Sword(name, item_info["price"], item_info["weight"], item_info.get("type"), item_info["length"])
        shop.add_item(sword_item)
    elif item_type == "bow":
        bow_item = Bow(name, item_info["price"], item_info["weight"], item_info.get("type"), item_info["draw length"], item_info["max draw force"])
        shop.add_item(bow_item)
    elif item_type == "arrow":
        arrow_item = Arrow(name, item_info["price"], item_info["weight"], item_info.get("type"))
        shop.add_item(arrow_item)
    else:
        shop_item = MedievalShopItem(name, item_info["price"], item_info["weight"], item_info.get("type"))
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
    print("Which item would you like to buy? (type 0 to exit)")

    for i, item in enumerate(shop.items):
        print(f"{i+1}. {item.name}: {item.price} coins")
        
    try:
        choice = int(input("Enter the number of the item you want: ")) - 1
        if 0 <= choice < len(shop.items):
            item = shop.items[choice]
            price = shop.get_item_price(item.name)
            typ = shop.get_item_type(item.name)
            print(f"You found a {item.name}!")
            print(f"Price: {price} coins")
            if item.price <= coins:
                answer = input(f"Do you want to buy the {item.name} for {price} coins? (y/n) ")
                if answer.lower() == "y":
                    coins -= price
                    inventory.append(item)
                    for key, value in item.__dict__.items():
                        if isinstance(value, int):
                            stats_dict[f"{item.name}_{key}"] = value
                    print(f"You bought the {item.name}!")
                    print(f"You have {coins} coins left.")
                    stats_dict["coins"] = coins
                    if item.name == "Bow":
                        print("Remember to buy arrows with your bow")
                else:
                    print("You did not buy the item")
            else:
                print("You do not have enough money for that item.")
        elif choice == 0:
            return
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")


# Define the sell_item function
def sell_item(coins, inventory, shop):
    print("You have the following items:")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item}: {shop.get_item_price(item)} coins")
    try:
        choice = int(input("Enter the number of the item you want to sell: ")) - 1
        if 0 <= choice < len(inventory):
            item = inventory[choice]
            price = shop.get_item_price(item.name)
            if price:
                coins += price
                inventory[choice] = None
                inventory.remove(None)
                print(f"You sold the {item.name} for {price} coins!")
                print(f"You have {coins} coins now.")
                stats_dict["coins"] = coins
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")



# Define the upgrade_inventory function
def upgrade_inventory(coins, inventory, shop):
    upgraded = False
    print("You have the following items:")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item.name}")
        while True:
            try:
                item_choice = int(input("Enter the name or number of the item you want to upgrade(type n to exit): "))
                if item_choice == 0:
                    break
                for i, item in enumerate(inventory, start=1):
                    if i == item_choice or item_choice == item.name:
                        item_data = item
                        item_quantity = sum(1 for i in inventory if i.name == item.name)
                        item_price = shop.get_item_price(item.name) / 4
                        break
                else:
                    raise ValueError
                break
            except (ValueError, IndexError):
                print("Item not found in inventory. Try again.")
        print(f"Upgrading {item_data.name} would cost {item_price * item_quantity:.2f} coins.")
        if coins < item_price * item_quantity:
            print("You do not have enough coins to upgrade.")
            break
        answer = input("Do you want to upgrade this item? (y/n) ")
        if answer.lower() == "y" or "yes":
            if item_data.type == "sword":
                item_data.length += 1
                coins -= item_price * item_quantity
                print(f"You upgraded your {item_data.name}! the {item_data.name} now has a length of {item_data.length:.1f} cm.")
            elif item_data.type == "bow":
                item_data.draw_length += 1
                item_data.max_draw_force += 1
                coins -= item_price * item_quantity
                print(f"You upgraded your bow! Your bow now has a draw length of {item_data.draw_length:.1f} cm and a max draw force of {item_data.max_draw_force:.1f} N.")
            elif item_data.type == "arrow":
                item_data.weight -= 0.1
                coins -= item_price * item_quantity
                print(f"You upgraded your arrow! Your arrow now weighs {item_data.weight:.1f} g.")
            print(f"You have {coins} coins left.")
            stats_dict["coins"] = coins
            upgraded = True
        elif answer.lower() == "n" or "no":
            print("You did not upgrade the item.")
            break

    return upgraded

    





# medieval_shop()



