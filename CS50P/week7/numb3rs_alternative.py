# numb3rs using re
import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # use regular expressions op to check for valid ip
    # used regex from this answer: https://stackoverflow.com/a/106223
    check = re.search(
        r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip)

    # return true of false depending on check value
    if check == None:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
