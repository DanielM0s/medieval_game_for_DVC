import random
from character_stats import stats_dict, inventory
# Define the MedievalShop class
class MedievalShop:
    """
    A class representing a medieval shop.
    """
    def __init__(self, name):
        # The name of the shop
        self.name = name
        # The items in the shop's inventory
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
        # Add the item to the list of items
        self.items.append(item)

    def get_item_price(self, item_name):
        """
        Returns the price of an item in the shop's inventory.
        """
        # Iterate over the items
        for item in self.items:
            # If the item's name matches the given item name
            if item.name == item_name:
                # Return the price of the item
                return item.price
    def get_item_type(self, item_name):
        # Iterate over the items
        for item in self.items:
            # If the item's name matches the given item name
            if item.name == item_name:
                # Return the type of the item
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
    def __init__(self, name, price, weight, type, **kwargs):
        # Set the name, price, weight, and type of the item
        self.name = name
        self.price = price
        self.weight = weight
        self.type = type
        # Add any additional attributes specified in the kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the item.
        """
        return f"{self.name}: {self.price} coins, {self.weight} lbs"
    
    # Define the Food class, which is a subclass of MedievalShopItem
class Food(MedievalShopItem):
    def __init__(self, name, price, weight, type, health_increase, strength_increase):
        # Call the superclass's constructor to set the name, price, weight, and type
        super().__init__(name, price, weight, type, health_increase=health_increase, strength_increase=strength_increase)

    def increase_health(self, player):
        """
        Increases the player's health by the amount specified in the food item.
        """
        # Increase the player's health
        player["health"] += self.health_increase

    def increase_strength(self, player):
        """
        Increases the player's strength by the amount specified in the food item.
        """
        # Increase the player's strength
        player["strength"] += self.strength_increase

class Sword(MedievalShopItem):
    def __init__(self, name, price, weight, type, length):
        # Call the superclass's constructor to set the name, price, weight, and type
        super().__init__(name, price, weight, type, length=length)

class Shield(MedievalShopItem):
    def __init__(self, name, price, weight, type, protection):
        # Call the superclass's constructor to set the name, price, weight, and type
        super().__init__(name, price, weight, type, protection=protection)

class Bow(MedievalShopItem):
    def __init__(self, name, price, weight, type, draw_length, max_draw_force):
        # Call the superclass's constructor to set the name, price, weight, and type
        super().__init__(name, price, weight, type, draw_length=draw_length, max_draw_force=max_draw_force)
class Arrow(MedievalShopItem):
    def __init__(self, name, price, weight, type):
        # Call the superclass's constructor to set the name, price, weight, and type
        super().__init__(name, price, weight, type)
# Create instances of the classes
# This dictionary contains all the items in the shop, with their respective info.
# The keys are the names of the items, and the values are dictionaries with the
# following keys: price, weight, type, health_increase, strength_increase,
# length, draw_length, max_draw_force, and protection.
items = {
    "Ilkwa (short spear)": {"price": 50, "weight": 3, "length": 0.9, "type": "sword"},
    "Assegai (spear)": {"price": 100, "weight": 0.5, "length": 1.97, "type": "sword"},
    "Knobkerrie (club)": {"price": 150, "weight": 5, "length": 0.52, "type": "sword"},
    "isihlangu (shield)": {"price": 20, "weight": 5, "protection": 5, "type": "shield"},
    "Bow": {"price": 50, "weight": 13.6, "draw_length": 76, "max_draw_force": 710, "type": "bow"},
    "arrow x10": {"price": 10, "weight": 0.1, "type": "arrow"},
    "mielie bread": {"price": 2, "weight": 0.5, "health_increase": 5, "strength_increase": 30, "type": "food"},
    "pap": {"price": 30, "weight": 0.5, "health_increase": 30, "strength_increase": 300, "type": "food"},
    "droeworse": {"price": 5, "weight": 0.2, "health_increase": 5, "strength_increase": 100, "type": "food"},
    "egg": {"price": 3, "weight": 0.1, "health_increase": 2, "strength_increase": 20, "type": "food"},
    "rusk": {"price": 10, "weight": 0.5, "health_increase": 15, "strength_increase": 40, "type": "food"},
    "apples": {"price": 10, "weight": 0.5, "health_increase": 10, "strength_increase": 20, "type": "food"},
}

# Create an instance of the MedievalShop class
shop = MedievalShop("The Medieval Shop")

# Loop through all the items in the items dictionary and add them to the shop
for name, item_info in items.items():
    item_type = item_info.get("type")
    if item_type == "food":
        # Create an instance of the Food class with the appropriate info
        food_item = Food(name, item_info["price"], item_info["weight"], item_info.get("type"), item_info["health_increase"], item_info["strength_increase"])
        # Add the food item to the shop
        shop.add_item(food_item)
    elif item_type == "shield":
        # Create an instance of the Shield class with the appropriate info
        shield_item = Shield(name, item_info["price"], item_info["weight"], item_info["protection"], item_info.get("type"))
    elif item_type == "sword":
        # Create an instance of the Sword class with the appropriate info
        sword_item = Sword(name, item_info["price"], item_info["weight"], item_info.get("type"), item_info["length"])
        # Add the sword item to the shop
        shop.add_item(sword_item)
    elif item_type == "bow":
        # Create an instance of the Bow class with the appropriate info
        bow_item = Bow(name, item_info["price"], item_info["weight"], item_info.get("type"), item_info["draw_length"], item_info["max_draw_force"])
        # Add the bow item to the shop
        shop.add_item(bow_item)
    elif item_type == "arrow":
        # Create an instance of the Arrow class with the appropriate info
        arrow_item = Arrow(name, item_info["price"], item_info["weight"], item_info.get("type"))
        # Add the arrow item to the shop
        shop.add_item(arrow_item)
    else:
        # Create an instance of the MedievalShopItem class with the appropriate info
        shop_item = MedievalShopItem(name, item_info["price"], item_info["weight"], item_info.get("type"))
        # Add the shop item to the shop
        shop.add_item(shop_item)


# Define the medieval_shop function

def medieval_shop():
    # This function is the main loop of the shop, it will continue to run until the player chooses to quit
    while True:
        # Print a message to the player indicating that they are in the shop
        print("-------------------------------------")
        print("Welcome to the medieval shop!")
        # Print the amount of coins the player has
        print(f"You have {stats_dict['coins']} coins.")
        print("-------------------------------------")
        # Ask the player what they want to do
        print("What would you like to do?")
        # Print the options
        print("1. Buy an item")
        print("2. Sell an item")
        print("3. Upgrade your inventory")
        print("4. Check your inventory")
        print("5. Exit")
        # Get the player's choice
        choice = input("Enter your choice: ")

        # If the player chooses to buy an item, call the buy_item function
        if choice == "1":
            buy_item(stats_dict["coins"], inventory, shop)
        # If the player chooses to sell an item, call the sell_item function
        elif choice == "2":
            sell_item(stats_dict["coins"], inventory, shop)
        # If the player chooses to upgrade their inventory, call the upgrade_inventory function
        elif choice == "3":
            upgrade_inventory(stats_dict["coins"], inventory, shop)
        # If the player chooses to check their inventory, loop through all the items in the inventory and print them
        elif choice == "4":
            for item in inventory:
                print(item)
        # If the player chooses to exit, print a goodbye message and break out of the loop
        elif choice == "5":
            print("Goodbye!")
            break
        # If the player enters an invalid choice, print an error message
        else:
            print("Invalid choice.")

# Define the buy_item function
def buy_item(coins, inventory, shop):
    # Print a message to the player
    print("Which item would you like to buy? (type 0 to exit)")
    # Generate a random discount based on the player's charisma
    discount = random.randint(1, stats_dict["charisma"])
    # Print a message to the player based on the discount
    if discount >= 30:
        discount_percentage = 20
        print("'Ah, you're back for more, eh? Well, I suppose you're not as poor as you look.' He chuckles and says, 'I'll give you a 20% discount on your next purchase, but just this once. Don't think you can come back here and take advantage of my generosity again.'")
    elif discount <= 15:
        discount_percentage = -5
        print("He scowls at you, 'early this morning someone stole my pap, until I find the culprit I am raising my prices by 5%.'")
    else:
        discount_percentage = 0

    # Print a list of all the items in the shop
    for i, item in enumerate(shop.items):
        price = item.price * (1 - discount_percentage / 100)
        print(f"{i+1}. {item.name}: {price:.2f} coins")
    # Ask the player which item they want to buy
    try:
        choice = int(input("Enter the number of the item you want: ")) - 1
        if 0 <= choice < len(shop.items):
            # Get the item that the player chose
            item = shop.items[choice]
            price = shop.get_item_price(item.name) * (1 - discount_percentage / 100)
            typ = shop.get_item_type(item.name)
            # Print a message to the player based on the item they chose
            print(f"You found a {item.name}!")
            print(f"Price: {price:.2f} coins")
            # Ask the player if they want to buy the item
            if item.price <= coins:
                answer = input(f"Do you want to buy the {item.name} for {price:.2f} coins? (y/n) ")
                if answer.lower() == "y":
                    # Take the money from the player
                    coins -= price
                    # Add the item to the player's inventory
                    inventory.append(item)
                    # Add the item's stats to the player's stats
                    for key, value in item.__dict__.items():
                        if isinstance(value, int):
                            stats_dict[f"{item.name}_{key}"] = value
                    # Print a message to the player
                    print(f"You bought the {item.name}!")
                    print(f"You have {coins:.2f} coins left.")
                    # Update the player's coins
                    stats_dict["coins"] = coins
                    # If the player bought a bow, remind them to buy arrows
                    if item.name == "Bow":
                        print("Remember to buy arrows with your bow")
                else:
                    # If the player doesn't want to buy the item, print a message
                    print("You did not buy the item")
            else:
                # If the player doesn't have enough money, print a message
                print("You do not have enough money for that item.")
        elif choice == 0:
            # If the player types 0, return without doing anything
            return
        else:
            # If the player types an invalid number, print an error message
            print("Invalid choice.")
    except ValueError:
        # If the player types something that isn't a number, print an error message
        print("Invalid choice.")


# Define the sell_item function
def sell_item(coins, inventory, shop):
    # Print out all the items in the player's inventory
    print("You have the following items:")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item}: {shop.get_item_price(item)} coins")
    try:
        # Ask the player which item they want to sell
        choice = int(input("Enter the number of the item you want to sell: ")) - 1
        if 0 <= choice < len(inventory):
            # Get the item they want to sell
            item = inventory[choice]
            # Get the price of the item
            price = shop.get_item_price(item.name)
            if price:
                # Add the money to the player
                coins += price
                # Remove the item from the player's inventory
                inventory[choice] = None
                inventory.remove(None)
                # Print a message to the player
                print(f"You sold the {item.name} for {price} coins!")
                print(f"You have {coins} coins now.")
                # Update the player's coins
                stats_dict["coins"] = coins
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")


# Define the upgrade_inventory function
def upgrade_inventory(coins, inventory, shop):
    # Check if the player has enough coins to upgrade the item
    upgraded = False
    # Print out all the items in the player's inventory
    print("You have the following items:")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item.name}")
        # Ask the player which item they want to upgrade
        while True:
            try:
                item_choice = int(input("Enter the name or number of the item you want to upgrade(type n to exit): "))
                if item_choice == 0:
                    break
                # Check if the item is in the player's inventory
                for i, item in enumerate(inventory, start=1):
                    if i == item_choice or item_choice == item.name:
                        item_data = item
                        item_quantity = sum(1 for i in inventory if i.name == item.name)
                        # Get the price of the item
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
        # Ask the player if they want to upgrade the item
        answer = input("Do you want to upgrade this item? (y/n) ")
        if answer.lower() == "y" or "yes":
            # If the player wants to upgrade the item, check if it is a sword, bow, or arrow
            if item_data.type == "sword":
                # Upgrade the sword
                item_data.length += 1
                coins -= item_price * item_quantity
                print(f"You upgraded your {item_data.name}! the {item_data.name} now has a length of {item_data.length:.1f} cm.")
            elif item_data.type == "bow":
                # Upgrade the bow
                item_data.draw_length += 1
                item_data.max_draw_force += 1
                coins -= item_price * item_quantity
                print(f"You upgraded your bow! Your bow now has a draw length of {item_data.draw_length:.1f} cm and a max draw force of {item_data.max_draw_force:.1f} N.")
            elif item_data.type == "arrow":
                # Upgrade the arrow
                item_data.weight -= 0.05
                coins -= item_price * item_quantity
                print(f"You upgraded your arrow! Your arrow now weighs {item_data.weight:.1f} g.")
            print(f"You have {coins} coins left.")
            stats_dict["coins"] = coins
            upgraded = True
        elif answer.lower() == "n" or "no":
            # If the player does not want to upgrade the item, print a message
            print("You did not upgrade the item.")
            break

    return upgraded


    





# medieval_shop()



