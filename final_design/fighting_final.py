import random
# from character_stats import stats_dict
from character_stats import inventory
from character_stats import stats_dict
#from enemy_stats import enemy_list
from enemy_stats import enemy_dict
from enemy_stats import inventory as enemy_inventory

class character:
    def __init__(self, stats_dict):
        self.name = stats_dict["name"]
        self.points = stats_dict["points"]
        self.coins = stats_dict["coins"]
        self.strength = stats_dict["strength"]
        self.dexterity = stats_dict["dexterity"]
        self.constitution = stats_dict["constitution"]
        self.intelligence = stats_dict["intelligence"]
        self.wisdom = stats_dict["wisdom"]
        self.health = stats_dict["constitution"] * 3
        self.sword = inventory["Ilkwa"]


    def attack(self,force):
        damage = force * self.sword["length"]
        self.strength -= force
        return damage

    def counter_attack(self, force):
        damage = force * self.sword["length"]
        self.strength -= damage
        return damage
    def check_health(self):
        if self.health <= 0:
            print(f"you have been defeated!")
            exit()
        else:
            return True
    
    




class Enemy:
    def __init__(self, enemy_name):
        stats = enemy_dict[enemy_name]
        self.name = enemy_name
        self.names = stats["name"]
        self.health = stats["health"]
        self.strength = stats["strength"]
        self.dexterity = stats["dexterity"]
        self.sword = enemy_inventory["Ilkwa"]

    def check_health(self):
        if self.health <= 0:
            del enemy_dict[self.name]
            return False
        else:
            return True

    def attack(self, force):
        damage = force * enemy_inventory.sword["length"]
        self.strength -= force
        return damage

    def end_turn(self):
        self.strength = 0


class Sword:
    def __init__(self, length):
        self.length = length


def fight():
    enemies = enemy_dict
    
    while True:
        if character.check_health == True:
            continue
        if Enemy.check_health == False:
            print("the enemy has been defeated, well done")
            enemies.pop(Enemy.name)
            break
        elif Enemy.check_health == True:
            print("the enemy has not been defeated yet")
        if not enemy_dict:
            print("You win!")
        
        

        
        while True:
            try:
                for i, (name, stats) in enumerate(enemy_dict.items()):
                    print(f"{i+1}. {name}")
                target = int(input("Which enemy do you want to attack? "))
                if target < 1 or target > len(enemies):
                    print("Invalid input")
                    continue
                enemy_name = list(enemies.keys())[target - 1]
                enemy = Enemy(enemy_name)
                dext = enemy.dexterity
                stre = enemy.strength
                enemy_chance_of_block = random.randint(1, dext)
                enemy_block_amount = random.randint(1, stre)  
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
                for att in attack_types:
                    print(att, attack_types[att])
                attack = input("Select an attack: ")
                while attack not in attack_types:
                    print("Invalid attack. Please select one from the following:")
                    for key, value in attack_types.items():
                        print(f"{key}. {value}")
                    attack = input("Select an attack: ")
                force = int(input(f"How much force do you want to hit them with? "))
                if force < 0 or force > cha.strength:
                    print("Invalid input")
                    continue
                force = cha.attack(force)
                if enemy_chance_of_block < 10:
                    enemy.health -= force
                    damage_string = f"You hit {enemy.name} for {force} damage"
                    if enemy.check_health == True:
                        damage_string += f", {enemy.name} has {enemy.health} health left"
                    else:
                        damage_string += f", {enemy.name} has been defeated"
                        Enemy.check_health(enemy)
                        continue
                    print(damage_string)
                    
                else:
                    if enemy_block_amount < force:
                        damage = force - enemy_block_amount
                        enemy.health -= damage
                        damage_string = f"You hit {enemy.name} for {damage} damage"
                        if Enemy.check_health(enemy) == True:
                            damage_string += f", {enemy.name} has {enemy.health} health left"
                        elif Enemy.check_health(enemy) == False:
                            damage_string += f", {enemy.name} has been defeated"
                            continue
                        else:
                            break
                        print(damage_string)
                    else:
                        print(f"{enemy.name} blocks the attack")
                if enemy.health > 0:
                    enemy_force = random.randint(1, enemy.strength)
                    chance_of_block = random.randint(1, stats_dict["constitution"])
                    enemy_attack = Enemy.attack(enemy, enemy_force)
                    if chance_of_block < 10:
                        print(f"{enemy.name} hits you for {enemy_attack} damage, you have {cha.health - enemy_attack} health left")
                        cha.health -= enemy_attack
                        character.check_health
                    else:
                        block_amount = random.randint(1, cha.dexterity)
                        if block_amount < enemy_attack:
                            damage = enemy_attack - block_amount
                            print(f"{enemy.name} hits you for {damage} damage, you have {cha.health - damage} health left")
                            cha.health -= damage
                        else:
                            print(f"You block {enemy.name}'s attack")
            except ValueError:
                print("Invalid input")
                continue
            if not Enemy.check_health:
                print(f"{enemy.name} has been defeated")
                enemies.pop(enemy_name)
                if not enemies:
                    print("You win!")
                    break
                continue    

            
        if cha.health <= 0:
            print("You died")
            break

        for enemy in enemies:
            Enemy.end_turn()

cha = character(stats_dict)
