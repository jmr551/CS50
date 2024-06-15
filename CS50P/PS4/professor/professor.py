import random


def main():
    lev = get_level()
    print(generate_integer(lev))

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
