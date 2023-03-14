months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


def main():
    while True:
        # get input date from user and send string to validate
        try:
            date = input("Date: ")
            validate(date)
            break
        # exception handling, let errors pass and reprompt user
        except ValueError:
            pass
        except KeyError:
            pass


def validate(date):
    # check if entered date is split by slashes
    if len(date.split("/")) == 3:
        split_date = date.split("/")

        # if month or day are out of range, reprompt
        if int(split_date[0]) > 12 or int(split_date[1]) > 31:
            main()

        else:
            # split up date
            day = split_date[1].strip()
            month = split_date[0].strip()
            year = split_date[2].strip()

            # if month or day are below 10 give them a leading 0
            if int(day) < 10:
                day = "0" + str(day)
            if int(month) < 10:
                month = "0" + str(month)

            # print out reformatted date
            print(year + "-" + month + "-" + day)

    # check if entered date is split with a comma
    elif len(date.split(",")) == 2:
        split_date = date.split(",")

        # split up date
        year = split_date[1].strip()
        split_date = split_date[0].split(" ")
        day = split_date[1].strip()
        month = split_date[0].strip()

        # call dict of months to get month number
        global months
        month_number = months[month]

        # if month or day are out of range, reprompt
        if int(month_number) > 12 or int(day) > 31:
            main()

        # if month or day are below 10 give them a leading 0
        if int(month_number) < 10:
            month_number = "0" + str(month_number)
        if int(day) < 10:
            day = "0" + str(day)

        # if month string is in the dict, print the reformatted date
        if month in months:
            print(year + "-" + str(month_number) + "-" + day)

        # if conditions are not met date is invalid, reprompt
        else:
            main()

    # entered date does not meet formatting conditions, reprompt
    else:
        main()


main()
