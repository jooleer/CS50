def main():
    percentage = convert(input("Fraction: "))
    print(gauge(percentage))


def convert(fraction):
    percentage = 0
    try:
        percentage_split = fraction.split("/")
        percentage = (
            int(percentage_split[0]) / int(percentage_split[1])) * 100
        return int(percentage)
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    if int(percentage) >= 99 and int(percentage) <= 100:
        return "F"
    elif percentage <= 1:
        return "E"
    elif percentage > 100:
        return "F"
    else:
        percentage = round(percentage)
        return ("{}%".format(int(percentage)))


if __name__ == "__main__":
    main()
