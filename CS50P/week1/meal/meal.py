def main():
    time = input("What time is it? ")
    number = convert(time.strip())

    if 7.0 <= number <= 8.0:
        print("breakfast time")
    elif 12.0 <= number <= 13.0:
        print("lunch time")
    elif 18.0 <= number <= 19.0:
        print("dinner time")


def convert(time):
    hour, minutes = time.split(":")

    if minutes.endswith("a.m.") or minutes.endswith("p.m."):
        minutes, ustime = minutes.split(" ")
        if ustime == "p.m.":
            hour = int(hour) + 12

    mins = float(minutes) / 60
    mins = round(mins, 2)

    converted = int(hour) + mins
    return converted


if __name__ == "__main__":
    main()
