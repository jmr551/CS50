def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Len
    if 2 > len(s) or len(s) > 6:
        #print(s)
        #print(len(s))
        #print("Falla en len")
        return False
    # 2 chars
    if not s[0].isalpha() or not s[1].isalpha():
        #print("No cumple los dos primeros alfa")
        return False
    num_phase = False
    for c in s:
        if not c.isalnum():
            #print("No Alpha Num")
            return False

        if not num_phase and c.isnumeric():
            num_phase = True
            if c == "0":
                #print("Num comienza con 0")
                return False
            continue

        if num_phase and c.isalpha():
            #print("Ya en num fase pero tiene un alfa luego")
            return False
    return True



if __name__ == "__main__":
    main()
