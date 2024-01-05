import cs50

while (True):
    h = cs50.get_int("Height: ")
    if h >= 1 and h <= 8:
        break

for fila in range(h):
    for columna in range(h):
        if fila + columna >= h - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print("  ", end="")
    for extra in range(fila + 1):
        print("#", end="")
    print()
