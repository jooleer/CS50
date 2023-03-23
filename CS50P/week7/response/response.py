from validator_collection import email, errors


def main():
    validate_email(input("What's your email address? "))


def validate_email(e):
    # check input with email validator
    try:
        email(e)
        print("Valid")

    # invalid email
    except errors.InvalidEmailError:
        print("Invalid")


if __name__ == "__main__":
    main()
