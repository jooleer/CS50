from validator_collection import email
import sys


def main():
    validate_email(input("What's your email address? "))


def validate_email(e):
    # check input with email validator
    check = email(e)

    if check:
        print("Valid")
        sys.exit()
    else:
        print("Invalid")
        sys.exit()


if __name__ == "__main__":
    main()
