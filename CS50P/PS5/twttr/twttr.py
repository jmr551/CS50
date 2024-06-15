import re
import sys

def main():
    print(shorten(input("")))


def shorten(word):
    if re.search(r'[0-9]', word):
        print("El texto no debe contener números")
        sys.exit(1)

    if re.search(r'[^\w\s]', word):
        print("El texto no debe contener puntuación")
        sys.exit(1)

    z = "aeiouAEIOU"
    tabla = str.maketrans("", "", z)
    return word.translate(tabla)


if __name__ == "__main__":
    main()
