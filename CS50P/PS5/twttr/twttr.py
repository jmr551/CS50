def main():
    print(shorten(input("")))


def shorten(word):
    z = "aeiouAEIOU"
    tabla = str.maketrans("", "", z)
    return word.translate(tabla)


if __name__ == "__main__":
    main()
