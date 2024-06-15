import random

while True:
    try:
        lev = int(input(""))
    except EOFError:
        print("eoferror")
    else:
        if lev > 0:
            break

num = random.randint(1, lev)
while True:
    guess = int(input(""))
