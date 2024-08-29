import random

import tester_beginning
import character_stats
player = character_stats.Stats
tester_beginning.charcter.set_stats

import shop
shop.MedievalShop("medieval shop")
shop_instance = shop.MedievalShop("medieval shop")
shop_instance.start_shop()
import character_stats
from final_fighting import fight_main
fight_main()
import bow_calculator


# Create shop instance and start shop
shop_instance = shop.MedievalShop("medieval shop")
shop_instance.start_shop()

# Attack enemy with archer
enemy = bow_calculator.Enemy(2.5, random.randint(300, 400))
bow = bow_calculator.Bow("long Bow", 710, 76)
arrow = bow_calculator.Arrow(0.1)
enemy = bow_calculator.Enemy(2.5, random.randint(300, 400))
archer = bow_calculator.Archer(bow, arrow, enemy, 100)

archer.attack()

# Run main function
fight_main()




