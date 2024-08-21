
import random
option = input("what game do you want to play")
if option == "1":
    import bow_calculator
    import matplotlib.pyplot as plt
    archer = bow_calculator.Archer(bow_calculator.Bow("long Bow", 710, 0.762), bow_calculator.Arrow(0.1), None, 100)
    archer.attack()
    archer.plot_results(archer.enemy.distance, archer.enemy.height)
elif option == "2":
    import final_fighting
    final_fighting.fight_main()