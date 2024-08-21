import random
main_character_inventory = {
    "melee_weapons": "short sword",
    "ranged_weapons": "longbow",
}
short_sword = {
    "blade length": 30,
}
main_character = {
    "name": "",
    "money": 10,
    "health": 100,
    "strength": 2,
    "defense": 2,
    "luck": 2,
    "charisma": 2
}
allies = {
    "health": 50,
    "amount": random.randint(5, 15),
}
enemy = {
    "health": 50,
    "enemy distance": random.randint(100, 366),
    "amount": random.randint(5, 15),
}
def amount_of_enemies():
    no_enemies = random.randint(1, 10)
    for i in range(no_enemies):
        enemy_distance = random.randint(1,10)
        return enemy_distance
print("you have a ", main_character_inventory["melee_weapons"], "and a ", main_character_inventory["ranged_weapons"])
weapon = input("what weapon do you want to use? ")
if "sword" or "axe" in weapon:
    print(f"you stand at the gate gazing out at the enemies. You have {allies['amount']} allies, and their is {enemy['amount']} enemies")
    battle_start = input("the gate starts to open, which enemy do you want to fight first")
    print("when attacking type: ")
    print("Slash: Cutting in a sweeping motion.")
    print("Stab: Thrusting with a pointed weapon.")
    print("Chop: A downward cut.")
    print("Deflect: Knock something off its intended trajectory.")
    print("Block: Prevent an attack from finding its mark.")
    print("Parry: Defend from an attack with a countermove.")
    print("Riposte: A quick counterattack after a parry")
    print("Feint: A fake, deceptive, or distracting strike to bait your opponent")
    print("move closer: you can move closer to attack, and depending on the type of sword, you will need to be close to the enemy.")
    amount_of_enemies()
    attack = input(f"your enemy is {enemy['enemy distance']}meters away, how do you want to attack him,")
    

    