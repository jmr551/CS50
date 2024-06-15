import re
def main():
    print(shorten(input("")))


def shorten(word):
    if re.search(r'[0-9]', word):
        raise ValueError("El texto no debe contener números")
    if re.search(r'[^\w\s]', word):
        raise ValueError("El texto no debe contener puntuación")

    z = "aeiouAEIOU"
    tabla = str.maketrans("", "", z)
    return word.translate(tabla)


if __name__ == "__main__":
    main()
