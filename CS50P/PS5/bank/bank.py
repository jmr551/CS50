def main():
    gr = input("Greeting: ")
    print (value(gr))


def value(gr):
    gr = gr.strip().lower()
    if "hello" in gr:
        return ("$0")
    elif gr[0] == 'h':
        return ("$20")
    else:
        return ("$100")


if __name__ == "__main__":
    main()