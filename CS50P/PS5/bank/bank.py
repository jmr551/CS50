def main():
    ...


def value(greeting):
    gr = input("Greeting: ").strip().lower()

    if gr[:5] == "hello":
        return ("$0")
    elif gr[0] == 'h':
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()
