import sys


def main():
    names = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            sys.exit()
        else:
            if name == "":
                printNames(names)
                names = []
            else:
                names.append(name)


def printNames(names):
    goodbye = "Adieu, adieu, to "
    for i in range(len(names)-1):
        goodbye += (names[i] +", to")
    print(goodbye)

if __name__ == "__main__":
    main()
