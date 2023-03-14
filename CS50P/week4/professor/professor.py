import random
import sys


def main():

    correct = 0
    guesses = 0
    tries = 0

    level = get_level()

    while True:
        if tries == 0:
            first = generate_integer(level)
            second = generate_integer(level)
        try:

            guess = int(input(str(first) + " + " + str(second) + " = "))
            if guess == (first + second):
                correct += 1
                guesses += 1
                tries = 0
                if guesses == 10:
                    break
            else:
                raise ValueError

        except ValueError:
            print("EEE")
            tries += 1
            if guesses == 10:
                break
            if tries == 3:
                guesses += 1
                tries = 0
                print(str(first) + " + " + str(second) + " =", first + second)
                pass
            pass

    print("Score: ", (correct))


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    low = (10 ** (level - 1))
    if level == 1:
        low = 0
    high = (10 * 10 ** (level - 1)) - 1
    return random.randint(low, high)


if __name__ == "__main__":
    main()
