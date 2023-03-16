def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    split = ip.split(".")
    if len(split) != 4:
        return False
    for number in split:
        if int(number) > 255 or int(number) < 0:
            return False
    return True


if __name__ == "__main__":
    main()
