# -----
# example using while loop and boolean variables
# -----
import random

health = 10
princess_found = False
coins_collected = 1

while not princess_found:
    if health <= 0:
        print("You have died before rescuing the princess.")
        break
    elif coins_collected > 10:
        print("You can collect no more coins.")
        coins_collected = 10

    if random.randint(0, 10) < 5:
        print("You found the princess!")
        princess_found = True
    else:
        print("You got lost and stubbed your toe.")
        health -= 2
        coins_collected += 2
