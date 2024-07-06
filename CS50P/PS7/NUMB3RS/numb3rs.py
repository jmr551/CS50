import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.match(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for i in range(1,5):
            if int(matches.group(i)) > 255:
                print(i+": "+ matches.group(i))
                return False
            return True
    else:
        return False


if __name__ == "__main__":
    main()
