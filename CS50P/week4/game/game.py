import sys
import random


def main():
    while True:
        try:
            # request user for number to base random number on
            first = int(input("Level: "))
            guess(first)
            break
        except ValueError:
            pass


def guess(number):
    # if number entered is too low, refuse it and reprompt
    if number <= 0:
        main()

    # randomize a number depending on provided number variable
    rand_number = random.randint(1, number)

    # start loop that keeps user guessing until they get the right number
    while True:
        try:
            # ask user for second number input
            second = int(input("Guess: "))
            if second <= 0:
                guess(number)
                break

            if rand_number > second:
                print("Too small!")
                pass
            elif rand_number < second:
                print("Too large!")
                pass
            # user guessed right number, exit
            else:
                sys.exit("Just right!")
        # if user enters a value that's not an int, refuse and reprompt
        except ValueError:
            pass


main()
