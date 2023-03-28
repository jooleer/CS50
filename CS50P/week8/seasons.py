from datetime import date
import re
import sys


def main():
    dob = input("What's your birth date? ")
    date_format = r"([1-2][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])"
    check = re.search(date_format, dob)

    if check:
        convert(dob)
    else:
        sys.exit("Invalid date")


def convert(dob):
    year, month, day = dob.split("-")
    daily = 1440
    


if __name__ == "__main__":
    main()
