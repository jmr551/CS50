def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        else:
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")
    return round(x / y * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
