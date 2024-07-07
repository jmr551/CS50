import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.match(r"(?P<h1>\d\d?)(:(?P<m1>\d\d))? (?P<ampm1>A|P)M to (?P<h2>\d\d?)(:(?P<m2>\d\d))? (?P<ampm2>A|P)M$", s):
        h1, m1, ampm1 = int(matches.group("h1")), matches.group("m1"), matches.group("ampm1")
        h2, m2, ampm2 = int(matches.group("h2")), matches.group("m2"), matches.group("ampm2")

        if m1 == None:
            m1 = 0
        else:
            m1 = int(m1)
        if m2 == None:
            m2 = 0
        else:
            m2 = int(m2)

        if not (0 <= h1 <= 12) or not (0 <= h2 <= 12) or not (0 <= m1 <= 59) or not (0 <= m2 <= 59):
            raise ValueError


        if ampm1 == "P":
            h1 += 12
        if ampm2 == "P":
            h2 += 12


        return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

    else:
        raise ValueError




if __name__ == "__main__":
    main()
