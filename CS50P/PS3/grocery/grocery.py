def imprimir(items):
    for item in sorted(items.keys()):
        print(f"{item}: {items[item]}")
items = {}
while True:
    try:
        item = input("").upper()
        items[item] += 1
    except EOFError:
        imprimir(items)
        break
    except KeyError:
        items[item] = 1


