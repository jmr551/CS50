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
    # 2 chars
    if not s[0].isaplha() or not s[1].isaplha():
        return False

    for c in s:
        c.isalnum()


main()
