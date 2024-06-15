import random


def main():
    lev = get_level()
    score = 0
    for i in range(2):
        a = generate_integer(lev)
        b = generate_integer(lev)
        correct = False
        for i in range(3):
            try:
                res = int(input(f"{a} + {b} = "))
            except ValueError:
                print("EEE")
                continue
            else:
                if res == a + b:
                    correct = True
                    score += 1
                    break
                else:
                    print("EEE")
        if not correct:
            print(f"{a} + {b} = {a + b}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            lev = int(input("Level: "))
        except ValueError:
            continue
        else:
            if lev in [1, 2, 3]:
                return lev


def generate_integer(level):
    return random.randint(0, 10**level - 1)

if __name__ == "__main__":
    main()
