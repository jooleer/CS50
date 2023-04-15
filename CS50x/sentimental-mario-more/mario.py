# import get_int from cs50
from cs50 import get_int


# define main
def main():
    height = get_height()
    start = 0
    for i in range(height):
        start += 1
        print(" " * (height-1), end="")
        print("#" * start, end="")
        print("  ", end="")
        print("#" * start)
        height -= 1


# define height function
def get_height():
    while True:
        try:
            # ask user for height input
            n = get_int("Height: ")
        except ValueError:
            print("Incorrect value")
        else:
            if n > 0 and n < 9:
                return n


main()

