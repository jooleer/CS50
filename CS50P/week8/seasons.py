import datetime
import inflect
import re
import sys

# set p as variable for inflect engine
p = inflect.engine()


def main():
    print(convert(input("Date of Birth: ")))


def convert(dob):
    # check if date follows yyyy-mm-dd format
    date_format = r"([1-2][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])"
    check = re.search(date_format, dob)

    # exit if date is not correctly formatted
    if not check:
        sys.exit("Invalid date")

    # subtract dob with today's date and convert the result to minutes
    daily = 1440
    today = datetime.date.today()
    dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
    days = today - dob
    minutes = daily * days.days

    # convert minutes number to words, capitalize and complete string
    words = p.number_to_words(minutes, andword="")
    output = words.capitalize() + " minutes"

    return (output)


if __name__ == "__main__":
    main()
