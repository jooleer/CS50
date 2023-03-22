import re
import sys


def main():
    print(convert(input("Hours: ")))
    sys.exit()


def convert(s):
    # ampm regex for "0-12:00 AM/PM to 0-12:00 AM/PM" ':00' minutes are optional
    ampm = "^(\d{1,2}(?::\d{2})?)(?:\s+)?(AM|PM)\s+to\s+(\d{1,2}(?::\d{2})?)(?:\s+)?(AM|PM)$"
    verify = re.search(ampm, s)

    # check if input passes regex check
    if verify:
        morning, evening = s.split("to")

        # strip empty spaces from both values
        morning = morning.strip()
        evening = evening.strip()

        # convert each provided time to correct 24-hour time
        first = convert_time(morning.split(" ")[0], morning[len(morning)-2])
        second = convert_time(evening.split(" ")[0], evening[len(evening)-2])

        # output the converted 24-hour time
        output = first, " to ", second
        output = ''.join(output)
        return output

    # input does not match regex, raise ValueError
    else:
        raise ValueError


# time gets hours/minutes format (##:##) and ap gets AM/PM (value ap = A or P)
def convert_time(time, ap):
    # match ap value to A or P
    match ap:
        # handle AM time
        case "A":
            # handle if time was given with a colon
            if ":" in time:
                time = time.split(":")
                # raise ValueError if minutes is higher than 59
                if int(time[1]) > 59:
                    raise ValueError

                # raise ValueError if hour is higher than 12
                if int(time[0]) > 12:
                    raise ValueError

                # if hour value is less than 10 add a leading 0 and combine tuples into one string
                if int(time[0]) < 10:
                    time[0] = "0", time[0]
                    time[0] = [''.join(tups) for tups in time[0]]
                    time[0] = ''.join(time[0])

                # if it's 12 AM set time to midnight (00 hr)
                if int(time[0]) == 12:
                    time[0] = "00"

                # format time string (hh:mm)
                time = time[0] + ":" + time[1]

            # no colon in time
            else:
                # if hour is less than 10 add a leading 0
                if int(time) < 10:
                    time = "0" + str(time)

                # raise ValueError if hour is higher than 12
                if int(time) > 12:
                    raise ValueError

                # if it's 12 AM set time to midnight (00 hr)
                if int(time) == 12:
                    time = "00"

                # no minutes were given so add ":00" ending for 24-hour time formatting
                time = time + ":00"

            # return time string
            return time

        # handle PM time
        case "P":
            # handle if time was given with a colon
            if ":" in time:
                time = time.split(":")
                # raise ValueError if minutes is higher than 59
                if int(time[1]) > 59:
                    raise ValueError

                # raise ValueError if hour is higher than 12
                if int(time[0]) > 12:
                    raise ValueError

                # if hour value is less than 10 add a leading 0 and combine tuples into one string
                if int(time[0]) < 10:
                    time[0] = "0", time[0]
                    time[0] = [''.join(tups) for tups in time[0]]
                    time[0] = ''.join(time[0])

                # if it's not 12 PM (12:00 'lunch time' in 24-hour time), add 12 hours to change PM to 24-hour time
                if not int(time[0]) == 12:
                    time[0] = int(time[0]) + 12

                # format time string (hh:mm)
                time = str(time[0]) + ":" + time[1]

            else:
                # if hour higher than 12, raise ValueError
                if int(time) > 12:
                    raise ValueError

                # if it's not 12 PM (12:00 'lunch time' in 24-hour time), add 12 hours to change PM to 24-hour time
                if not int(time) == 12:
                    time = int(time) + 12

                # if hour is less than 10 add a leading 0
                if int(time) < 10:
                    time = "0" + str(time)

                # if hour = 24 set it to midnight (00 hr in 24-hour time)
                if int(time) == 24:
                    time = "00"

                # no minutes were given so add ":00" ending for 24-hour time formatting
                time = str(time) + ":00"

            # return time string
            return time


if __name__ == "__main__":
    main()
