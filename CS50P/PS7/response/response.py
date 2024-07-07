import re

def main():
    print(valid(input("What's your email address? ")))

def valid(ad):
    m = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    if re.search(m, ad):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
