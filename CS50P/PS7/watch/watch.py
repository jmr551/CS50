import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"src=\"https?://(:?www\.)?youtube\.com/embed/.+?\"", s):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
