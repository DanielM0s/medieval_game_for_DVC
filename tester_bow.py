import math
import random
import numpy as np
import cmath
bow = {
    "name": "long Bow",
    "maxpull force": 710,
    "maxpull distance": 0.762,
    
}
enemy = {
    "height": 2.5,
    "distance": random.randint(300, 400)}
cont = True
def square_root(number):
    sign = np.sign(number)
    result = np.sqrt(np.abs(number))
    return sign * result

def bow_calculator(f, X, M, angle):
    X = X / 100
    k = f / X
    ep = k/2 
    ep = ep * pow(X, 2)
    vi = 2 * ep/ M
    vi = square_root(vi)
    vix = vi * math.cos(math.radians(angle))
    viy = vi * math.sin(math.radians(angle))
    t = 0 - vix
    t = t / -9.8
    t = t * 2
    d = vix * t
    t = enemy["distance"]/ viy
    h = viy * t + -4.9 * pow(t, 2)
    height_of_arrow.append(h)
    if h < 0:
        return "your arrow falls short of the enemy"
    elif h > enemy["height"]:
        return "your arrow flies over the head of the enemy"
    else:
        return "your arrow hits the enemy"
while cont == True:
    height_of_arrow = []
    print(enemy["distance"], enemy["height"])
    force = int(input("how much force do you want to apply? hint: you do not need to apply more than 710N, or less than 400N"))
    if force > 710:
        print("your string snaps, you now need to replace it. Next time try with less force")
        exit()
    length = int(input("how far do you pull the string back in cm? "))
    if length > 76.2:
        print("your string snaps, you now need to replace it. Next time don't pull it back too far")
        exit()
    weightofarrow = 0.1
    angle = int(input("what angle do you want to shoot the arrow? "))
    if bow_calculator(force, length, weightofarrow, angle) == "your arrow falls short of the enemy":
        print("your arrow falls short of the enemy")
    elif bow_calculator(force, length, weightofarrow, angle) == "your arrow flies over the head of the enemy":
        print("your arrow flies over the head of the enemy")
    else:
        print("your arrow hits the enemy")
    print(f"the height of the arrow is: {height_of_arrow[0]}m")
    cont = input("do you want to continue? y/n ")
    if cont.lower() == "y":
        cont = True
    else:
        cont = False