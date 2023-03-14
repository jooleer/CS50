def main():
    calculate_fuel()


def calculate_fuel():
    while True:
        try:
            level = input("Fraction: ")
            percentage_split = level.split("/")
            percentage = (
                int(percentage_split[0]) / int(percentage_split[1])) * 100
            if int(percentage) >= 99 and int(percentage) <= 100:
                print("F")
            elif percentage <= 1:
                print("E")
            elif percentage > 100:
                calculate_fuel()
            else:
                percentage = round(percentage)
                print("{}%".format(int(percentage)))
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


if __name__ == "__main__":
    main()
