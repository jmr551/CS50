import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"(^um[^a-z]|um|um$|^um$)", s, flags=re.IGNORECASE)
    return (matches)


if __name__ == "__main__":
    main()
