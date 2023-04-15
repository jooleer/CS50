# import get_string from cs50
from cs50 import get_string
import sys


# calculate sum of digits
def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


# ask input number from user and check if correct format entered
def cardcheck():
    while True:
        try:
            n = get_string("Number: ")
        except ValueError:
            print("Incorrect input.")
        else:
            if n != "" and len(n) >= 13 and len(n) <= 16:
                return n
            else:
                print("INVALID")
                sys.exit(1)


# calculate sum of double of digits starting from second from the back
def countDouble(n):
    total = 0
    length = len(n)

    while length > 1:
        tempn = int(n[length-2:length-1]) * 2
        total += getSum(tempn)
        length -= 2

    return total


# calculate sum of remaining digits
def countRemainder(n):
    total = 0
    length = len(n)

    while length >= 1:
        if length == 1:
            total += int(n[length-1:length])
            length = 0
        else:
            tempn = int(n[length-1:length])
            total += getSum(tempn)
            length -= 2

    return total


# main
def main():
    number = cardcheck()

    first = countDouble(number)
    second = countRemainder(number)
    total = first + second

    # check if remainder is 0 if not, card number is invalid
    if total % 10 != 0:
        print("INVALID")
        sys.exit(1)

    # case visa
    if len(number) == 13:
        if number[0:1] == "4":
            print("VISA")
            sys.exit(0)
    # case amex
    if len(number) == 15:
        if number[0:2] == "34" or number[0:2] == "37":
            print("AMEX")
            sys.exit(0)
    # check mc or visa
    if len(number) == 16:
        if number[0:2] == "51" or number[0:2] == "52" or number[0:2] == "53" or number[0:2] == "54" or number[0:2] == "55":
            print("MASTERCARD")
            sys.exit(0)
        elif number[0:1] == "4":
            print("VISA")
            sys.exit(0)

    print("INVALID")
    sys.exit(0)


# call main function
main()