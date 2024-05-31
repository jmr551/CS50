def main():
    inp = input("What time is it? ")
    time = convert(inp)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    return int(h) + int(m) / 60


if __name__ == "__main__":
    main()
