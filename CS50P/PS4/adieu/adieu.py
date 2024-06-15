import sys
names = []

def main():
    while True:
        try:
            name = input("Name: ")
            print("pasé sin problemas")
        except EOFError:
            sys.exit()
        else:
            if name == "":
                printNames(names)
                names = []
            else:
                print("Ya entré en el else")
                names.append(name)


def printNames(names):
    goodbye = "Adieu, adieu, to "
    for i in range(len(names)-1):
        goodbye += (names[i] +", to")


if __name__ == "__main__":
    main()
