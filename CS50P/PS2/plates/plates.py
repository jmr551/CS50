def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Len
    if 2 < len(s) or len(s) > 6:
        return False
    


main()
