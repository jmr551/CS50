import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"(^um[^]|um|um$|^um$)", s, flags=re.IGNORECASE)

if __name__ == "__main__":
    main()
