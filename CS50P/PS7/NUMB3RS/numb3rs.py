import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"$d{1,3}\.d{1,3}\.d{1,3}\.d{1,3}^", ip)
    print(matches.group(1))
    print(matches.group(2))
    print(matches.group(3))
    print(matches.group(4))

if __name__ == "__main__":
    main()
