def main():
    while True:
        x, y = input("Fraction: ").split("/")
        try:
            x = int(x)
            y = int(y)
            f = round(x / y * 100)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        else:
            if f <= 1:
                print("E")
            elif f >= 99:
                print("F")
            else:
                print(f)
                break

main()

