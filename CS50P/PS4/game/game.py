import random
import sys

while True:
    try:
        lev = int(input("Level: "))
    except ValueError:
        continue
    else:
        if lev > 0:
            break

num = random.randint(1, lev)
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    else:
        if guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            sys.exit("Just right!")
