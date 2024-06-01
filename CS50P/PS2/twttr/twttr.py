entrada = input("Input: ")
wrd = ""
for c in entrada:
    c_min = c.lower()
    if c_min != "a" and c_min != "e" and c_min != "i" and c_min != "o" and c_min != "u":
        wrd += c

print("Output:", wrd)
