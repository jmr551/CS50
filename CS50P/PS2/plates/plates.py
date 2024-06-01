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
    num_phase = False
    for c in s:
        if not c.isalnum():
            return False

        if not num_phase and c.isnumeric():
            num_phase = True
            if c == "0":
                return False
            continue

        if num_phase and c.isalpha():
            return False
    return True


main()
