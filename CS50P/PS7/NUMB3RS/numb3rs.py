import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    re.search("$d{1,3}\.\.\.^")


if __name__ == "__main__":
    main()
