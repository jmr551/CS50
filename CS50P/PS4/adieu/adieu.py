import sys
while True:
    try:
        input("Name")
    except EOFError:
        sys.exit()
