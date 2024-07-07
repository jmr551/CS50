from validator_collection import validators, checkers, errors

def main():
    print(valid(input("What's your email address? ")))

def valid(ad):
    try:
        validators.email(ad)
        return "Valid"
    except InvalidEmailError:
        return "Invalid"

if __name__ == "__main__":
    main()
