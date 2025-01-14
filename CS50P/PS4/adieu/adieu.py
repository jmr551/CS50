import sys


def main():
    names = []
    while True:
        try:
            name = input()
        except (EOFError, KeyboardInterrupt):
            printNames(names)
            sys.exit()
        else:
            names.append(name)


def printNames(names):
    goodbye = "Adieu, adieu, to " + names[0]

    for i in range(1, len(names)-1):
        goodbye += (", " + names[i])
    if len(names) > 1:
        goodbye += ", and " + names[-1]
    print(goodbye)

if __name__ == "__main__":
    main()
