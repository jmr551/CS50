import random


def main():
    lev = get_level()


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
    

if __name__ == "__main__":
    main()
