def main():
    gr = input("Greeting: ")
    print(f"${value(gr)}")

def value(gr):
    gr = gr.strip().lower()
    if "hello" in gr:
        return 0
    elif gr.startswith('h'):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
