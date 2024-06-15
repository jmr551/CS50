import sys
names = []

def main():
    while True:
        try:
            name = input("Name")
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
    

